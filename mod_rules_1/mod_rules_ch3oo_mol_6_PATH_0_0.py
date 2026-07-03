ch3oo_mol_6_PATH_0_0 = """rule [
	ruleID " ch3oo_mol_6_PATH_0_0"
	left [
			node [ id 6 label "O." ]
			node [ id 9 label "C." ]

	]
	context [
			node [ id 2 label "O" ]
			node [ id 8 label "C" ]
			node [ id 11 label "C" ]
			node [ id 12 label "O" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 11 label "-" ]
			 edge [ source 9 target 12 label "-" ]

	]
	right [
			 edge [ source 6 target 9 label "-" ]
			node [ id 6 label "O" ]
			node [ id 9 label "C" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_mol_6_PATH_0_0)
rule1_B = Rule.fromGMLString(ch3oo_mol_6_PATH_0_0, invert=True)
