import mod
import json
from generate_chemical_space import find_energies

NODE_ID_INDEX = 3
SOURCE_ID_INDEX = 3
TARGET_ID_INDEX = 5

user_input = input("How many iterations would you like to run?\n")
ITEREATION_LIMIT = int(user_input)

use_full_context = None
while use_full_context == None:
    user_input = input("Use full context versions of rules? (Y/N)\n")
    if user_input == "Y" or user_input == "y":
        use_full_context = True
    elif user_input == "N" or user_input == "n":
        use_full_context = False

reaction_info = {}
input_graphs = []
input_rules = []

with open("molecules.json", "r") as json_file:
    mol_json = json.load(json_file)

mol_names = mol_json.keys()
for mol in mol_names:
    if "mol_" not in mol:
        graph = mod.Graph.fromGMLFile("mod_molecules/"+mol+".gml")
        input_graphs.append(graph)

reaction_info = find_energies("relations.json")

for key in reaction_info.keys():
    if "mol" in key:
        break
    e_a = reaction_info[key][0]
    e_r = reaction_info[key][1]
    educts_names = reaction_info[key][2]
    products_names = reaction_info[key][3]

    rule_name = key.split("/")[1]
    altered_name = rule_name.replace("_", "-")
    new_rule_name = f"{altered_name}, E_A: {round(e_a, 2)}, E_R: {round(e_r,2)}"
    altered_key = key.replace("/", "_")
    if use_full_context:
        new_rule = mod.Rule.fromGMLFile(f"full_context_rules/qnet_rule_{altered_key}.gml", name=new_rule_name)
    else:
        new_rule = mod.Rule.fromGMLFile(f"no_context_rules/qnet_rule_{altered_key}.gml", name=new_rule_name)
    input_rules.append(new_rule)


strat = (
   addUniverse(input_graphs)
   >> addSubset(input_graphs)
   >> repeat[ITEREATION_LIMIT](
         input_rules
      )
)
dg = mod.DG(graphDatabase=input_graphs)
dg.build().execute(strat)
dg.print()