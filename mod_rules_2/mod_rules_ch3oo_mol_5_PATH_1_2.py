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
			node [ id 25 label "H" ]
			node [ id 9 label "C" ]
			node [ id 8 label "C" ]
			node [ id 12 label "O" ]
			node [ id 13 label "C" ]
			node [ id 10 label "O" ]
			node [ id 15 label "C" ]
			node [ id 17 label "C" ]
			node [ id 18 label "O" ]
			node [ id 19 label "H" ]
			node [ id 16 label "H" ]
			node [ id 2 label "O" ]
			node [ id 1 label "C" ]
			 edge [ source 11 target 14 label "-" ]
			 edge [ source 9 target 11 label "-" ]
			 edge [ source 14 target 25 label "-" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 12 label "=" ]
			 edge [ source 10 target 13 label "-" ]
			 edge [ source 13 target 15 label "-" ]
			 edge [ source 8 target 10 label "-" ]
			 edge [ source 15 target 17 label "-" ]
			 edge [ source 15 target 18 label "-" ]
			 edge [ source 15 target 19 label "-" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 1 target 2 label "-" ]

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
