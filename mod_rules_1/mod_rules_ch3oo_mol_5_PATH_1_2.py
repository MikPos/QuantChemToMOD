ch3oo_mol_5_PATH_1_2 = """rule [
	ruleID " ch3oo_mol_5_PATH_1_2"
	left [
			 edge [ source 11 target 13 label "-" ]
			 edge [ source 13 target 16 label "-" ]
			node [ id 6 label "O." ]
			node [ id 11 label "C." ]

	]
	context [
			node [ id 14 label "O" ]
			node [ id 9 label "C" ]
			node [ id 13 label "C" ]
			node [ id 10 label "O" ]
			node [ id 15 label "C" ]
			node [ id 16 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 11 target 14 label "-" ]
			 edge [ source 9 target 11 label "-" ]
			 edge [ source 10 target 13 label "-" ]
			 edge [ source 13 target 15 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 11 target 13 label "=" ]
			 edge [ source 6 target 16 label "-" ]
			node [ id 6 label "O" ]
			node [ id 11 label "C" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_mol_5_PATH_1_2)
rule1_B = Rule.fromGMLString(ch3oo_mol_5_PATH_1_2, invert=True)
