
folder = "."

with open(folder+"/react.inp", "r") as inp:
    lines = inp.readlines()
    for line in lines:
        if line.split()[0] == "T":
            temp = line.split("=")[1].strip("\n").replace(" ", "")
        elif line.split()[0] == "sp_method":
            sp_method = line.split("=")[1].strip("\n").replace(" ", "")
        elif line.split()[0] == "solvent_name":
            solvent_name = line.split("=")[1].strip("\n").replace(" ", "")
        elif line.split()[0] == "molar":
            molar = line.split("=")[1].strip("\n").replace(" ", "")
    method = temp+"_"+sp_method+"_"+solvent_name+"_"+molar
    print(method)

import json
with open(folder+"/relations.json", "r") as file:
    relations = json.load(file)

# load data from current MOD_DB
import json
with open("./mod_DB_1.json", "r") as file:
    mod_db = json.load(file)

for key in mod_db.keys():
    for gml_rule in mod_db[key].keys():
        Rule.fromGMLString(gml_rule)

# for first entry into mod_DB:
include(folder+"/mod_rules_1/mod_rules_1.py")

start = inputRules[0]
if "inverse" in start.name:
    try:
        G_A_solv_1 = relations[start.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
        G_R_solv_1 = relations[start.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_R_solv"]
        G_A_final_1 = G_A_solv_1 - G_R_solv_1
    except:
        G_A_final_1 = "N.A."
else:
    try:
        G_A_final_1 = relations[a.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
    except:
        G_A_final_1 = "N.A."

final_rules = [inputRules[0]]
final_rules_G = [[start, G_A_final_1]]

#final_rules = []
#final_rules_G = []
#G_A = "N.A."

#for rule in inputRules:
#    final_rules.append(rule)
#    final_rules_G.append([rule, G_A])

###############################

# can we somehow add the new rules not to inputRules, but another rule set? like this, we compare the rules in the DB with itself...takes time

for a in inputRules:
    do_not_append = False
    if a not in final_rules:
        for rule in final_rules:
            same = a.monomorphism(rule) == 1
            if "inverse" in a.name:
                try:
                    G_A_solv_1 = relations[a.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
                    G_R_solv_1 = relations[a.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_R_solv"]
                    G_A_final_1 = G_A_solv_1 - G_R_solv_1
                except:
                    G_A_final_1 = "N.A."
            else:
                try:
                    G_A_final_1 = relations[a.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
                except:
                    G_A_final_1 = "N.A."
            if "inverse" in rule.name:
                try:
                    G_A_solv_2 = relations[rule.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
                    G_R_solv_2 = relations[rule.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_R_solv"]
                    G_A_final_2 = G_A_solv_2 - G_R_solv_2
                except:
                    G_A_final_2 = "N.A."
            else:
                try:
                    G_A_final_2 = relations[rule.name.replace(" ","").replace("_PATH","/PATH").replace("-","_").replace(",inverse", "")]["G"][temp][solvent_name][sp_method]["G_A_solv"]
                except:
                    G_A_final_2 = "N.A."
            if same == True:
                print("Same rules:", a.name, rule.name)
                print(G_A_final_1, G_A_final_2)
                do_not_append = True
        if not do_not_append:
            final_rules.append(a)
            final_rules_G.append([a, G_A_final_1])

#print(final_rules)
relations_new = mod_db

for b, G_A in final_rules_G:
    gml = b.getGMLString()
    name = gml.split("\"")[1].strip("\t").strip("\n")
    if name not in relations_new.keys(): # needs to be changed!!!
        relations_new[name] = {gml: {method: G_A}} # add computational method

json_formatted_str = json.dumps(relations_new, indent=4)
with open("mod_DB_1_new.json", "w") as json_formatted:
    json_formatted.write(json_formatted_str)

    #for b in inputRules:
    #    same = a.monomorphism(b) == 1
    #    print(a, b, same)

