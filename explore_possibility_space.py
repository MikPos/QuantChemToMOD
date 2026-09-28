import mod
import json
import itertools
from generate_chemical_space import find_energies

NODE_ID_INDEX = 3
SOURCE_ID_INDEX = 3
TARGET_ID_INDEX = 5

ITEREATION_LIMIT = 2

class RuleNode:
    def __init__(self, rule):
        self.rule = rule
        self.used = False
        self.child = None
    
    def add_child(self, child):
        self.child = child


####################
# HELPER FUNCTIONS #
####################

###
# Read in full context rules:
###
def generate_full_rules():
    rules = []
    reaction_dict = find_energies("relations.json")
    for key in reaction_dict.keys():
        if "mol" in key:
            break
        e_a = reaction_dict[key][0]
        e_r = reaction_dict[key][1]

        rule_name = key.split("/")[1]
        altered_name = rule_name.replace("_", "-")
        new_rule_name = f"full-{altered_name}, E_A: {round(e_a, 2)}, E_R: {round(e_r,2)}"
        altered_key = key.replace("/", "_")
        new_rule = mod.Rule.fromGMLFile(f"full_context_rules/qnet_rule_{altered_key}.gml", name=new_rule_name)
        rules.append(new_rule)
    return rules


###
# Create middle rules:
###
def find_no_context_vertices(rule):
    list_of_vertices = []
    gml = rule.getGMLString()
    gml_list = gml.split("\n")
    left_seen = False
    context_seen = False
    right_seen = False
    for line in gml_list:
        if "left" in line:
            left_seen = True
        if "context" in line:
            context_seen = True
        if "right" in line:
            right_seen = True
        if (left_seen == True and context_seen == False) or (context_seen == True and right_seen == True):
            if "node" in line:
                list_of_vertices.append(line.split(" ")[NODE_ID_INDEX])
            if "edge" in line:
                line_items = line.split(" ")
                list_of_vertices.append(line_items[SOURCE_ID_INDEX])
                list_of_vertices.append(line_items[TARGET_ID_INDEX])
    return list(set(list_of_vertices))

def create_full_list(rule):
    result = []
    for v in rule.left.vertices:
        result.append(str(v.id))
    return result

def find_further_context_vertices(full_list, no_context_list, rule):
    result = {0: no_context_list}
    last_list = no_context_list
    i = 1
    while set(last_list) != set(full_list):
        new_list = last_list.copy()
        for num in last_list:
            for v in rule.left.vertices:
                if num == str(v.id):
                    for edge in v.incidentEdges:
                        if str(edge.target.id) not in new_list:
                            new_list.append(str(edge.target.id))
        result[i] = new_list
        last_list = new_list
        i += 1
    return result

def create_new_rules(context_lists, rule):
    new_gml_strings = {}
    for i, vlist in context_lists.items():
        new_gml = ""
        for line in rule.getGMLString().split("\n"):
            if "ruleID" in line:
                new_gml += line.replace("full", f"{i}-context") + "\n"
            elif "node" not in line and "edge" not in line:
                new_gml += line + "\n"
            else:
                line_parts = line.split(" ")
                if "node" in line and line_parts[NODE_ID_INDEX] in vlist:
                    new_gml += line + "\n"
                elif "edge" in line and line_parts[SOURCE_ID_INDEX] in vlist and line_parts[TARGET_ID_INDEX] in vlist:
                    new_gml += line + "\n"
        new_gml_strings[i] = new_gml
    return new_gml_strings

def create_rule_tree(r, gml_string_map):
    root_rule = RuleNode(r)
    current = root_rule
    for i in range(len(gml_string_map)-2, 0, -1): # -2 since we don't want the complete rule twice!
        new_rule_node = RuleNode(mod.Rule.fromGMLString(gml_string_map[i]))
        current.add_child(new_rule_node)
        current = new_rule_node
    return root_rule

# Functions for generating DG
def do_iteration(rule_tree_list, build):
    graphDB = build.dg.graphDatabase
    for root_rule in rule_tree_list:
        res = [list(itertools.combinations(graphDB, r)) for r in range(1, len(graphDB) + 1)]  
        all_subsets = [list(sublist) for g in res for sublist in g] 
        for subset in all_subsets:
            apply_rule(subset, root_rule, build)
            # Should continue with the same rule after the first succesful application.

        # new_set = build.execute(root_rule.rule)
        # print(root_rule.rule.name)
        # print(root_rule.rule.getGMLString())
        # print(new_set.universe)
        # print(new_set.subset)
        # break
    return None

def apply_rule(graphs, rule_node, dg_build):
    result = dg_build.apply(graphs, rule_node.rule)
    if not result and rule_node.child is not None:
        result = apply_rule(graphs, rule_node.child, dg_build)
    if result:
        rule_node.used = True

def print_used_rules(rule_nodes):
    for node in rule_nodes:
        print_rule_node(node)

def print_rule_node(rule_node):
    if rule_node.used == True:
        rule_node.rule.print()
    if rule_node.child != None:
        print_rule_node(rule_node.child)


if  __name__=="__main__":
    input_graphs = []

    ###
    # Import molecules and set as universe and subset
    ###
    with open("molecules.json", "r") as json_file:
        mol_json = json.load(json_file)
        mol_names = mol_json.keys()
        for mol in mol_names:
            if "mol" in mol:
                continue
            graph = mod.Graph.fromGMLFile("mod_molecules/"+mol+".gml")
            input_graphs.append(graph)


    input_rules = generate_full_rules()
    rule_trees = []
    for r in input_rules:
        vertex_list = find_no_context_vertices(r)
        complete_list = create_full_list(r)
        new_lists = find_further_context_vertices(complete_list, vertex_list, r)
        new_gmls = create_new_rules(new_lists, r)
        root_rule = create_rule_tree(r, new_gmls)
        rule_trees.append(root_rule)


    ###
    # Expand DG
    ###
    dg = mod.DG(graphDatabase=input_graphs)
    reaction_network = dg.build()
    reaction_network.execute(mod.addSubset(input_graphs))
    for i in range(ITEREATION_LIMIT):
        print(f"Doing iteration {ITEREATION_LIMIT}, with {len(reaction_network.dg.graphDatabase)} graphs")
        do_iteration(rule_trees, reaction_network)
        print(f"{len(reaction_network.dg.graphDatabase)} graphs found")

    print_used_rules(rule_trees)


    with open("graph_db.txt", "w") as file:
        for graph in dg.createdGraphs:
            file.write(f"{graph.name};{graph.smilesWithIds};\n")
        

    del reaction_network
    dg.dump("simple_dg")
