ch3oo_mol_6_PATH_1_2 = """rule [
	ruleID " ch3oo_mol_6_PATH_1_2"
	left [
			 edge [ source 12 target 23 label "-" ]
			 edge [ source 9 target 12 label "-" ]
			node [ id 6 label "O." ]
			node [ id 9 label "C." ]

	]
	context [
			node [ id 12 label "O" ]
			node [ id 23 label "H" ]
			node [ id 8 label "C" ]
			node [ id 11 label "C" ]
			node [ id 2 label "O" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 11 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 23 label "-" ]
			 edge [ source 9 target 12 label "=" ]
			node [ id 6 label "O" ]
			node [ id 9 label "C" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_mol_6_PATH_1_2)
rule1_B = Rule.fromGMLString(ch3oo_mol_6_PATH_1_2, invert=True)
