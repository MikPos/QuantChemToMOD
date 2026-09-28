# QuantChemToMOD
This project offers a process for converting Quantum Chemistry Calculation into MØD. It allows you to take the calculations, which offer little help in generating a visual overview, and visually compare each reaction mechanism in a chemical space. Additionally, the project allows for further exploration of the chemical possibility space, reachable from the educts of the reaction mechanisms and the mechanisms themselves.

Project Overview:
- Conversion of Quantum Chemical Calculations to a Rule Based Graph model of chemistry
- Construction of a chemical space using the converted data (including thermodynamics)
- Exploration of additional possible products, by applying the mechanisms repeatedly over a user-specified amount of iterations

### generate_mod_rules.py
This file handles the conversion from XYZ files used as input and generated as output from TurboMole. The files are typically stored in a molecules folder and then distinct folders containing the different reaction mechanisms (not present in current project folder structure). *generate_mod_rules.py* imports the xyz files and converts them to SD Files. From there, it converts the molecules into GML Strings and exports those as individual files, with matching names to the molecule XYZ files. For the reaction Mechanisms, it converts the associated *educts.xyz* and *products.xyz* files into a single reaction GML string, and exports it with a name matching the reaction mechanism folder (eg.: **vitc-ch3oo-PATH-0-0**).
When importing the chemical reactions the code also generates two versions of each reaction: *full_context* and *no_context*, referring to the chemical context surrounding the reaction core of the rules.

### generate_chemical_space.py
This file handles the generation of the original chemical space, explored in the quantum chemical calculations. It imports the newly generated GML files for the molecules, as well as rules, and then creates a Derivation Graph, to which it adds the specific derivations from the calculations. When the rules are loaded from the GML file, they are also renamed, to match the original folder name similar to their file name from *generate_mod_rules.py* file generation. Additionally, the names of the rules are padded out with the Energy of Activation and Energy of Reaction from the thermodynamics file *relations.json*.

### explore_possibility_space.py
This file allows the user to seperately use the chemical space exploration feature from MØD on their converted molecules and rules. The Derivation Graph is created similarly to in *generate_chemical_space.py* but now withoput adding specific derivations. Instead, the original educts are loaded into the graph database of the derivation graph, and the rules are applied iteratively to a growing graph database space. The user defined the amount of iterations, and also whether they wish to use the rules with complete chemical context or ones with no chemical context.