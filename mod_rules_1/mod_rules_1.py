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
ch3oo_vitc_PATH_10_13 = """rule [
	ruleID " ch3oo_vitc_PATH_10_13"
	left [
			 edge [ source 13 target 25 label "-" ]
			node [ id 6 label "O." ]
			node [ id 13 label "C" ]

	]
	context [
			node [ id 12 label "C" ]
			node [ id 16 label "O" ]
			node [ id 25 label "H" ]
			node [ id 26 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 12 target 13 label "-" ]
			 edge [ source 13 target 16 label "-" ]
			 edge [ source 13 target 26 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 25 label "-" ]
			node [ id 13 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_10_13)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_10_13, invert=True)
ch3oo_vitc_PATH_11_14 = """rule [
	ruleID " ch3oo_vitc_PATH_11_14"
	left [
			 edge [ source 13 target 26 label "-" ]
			node [ id 6 label "O." ]
			node [ id 13 label "C" ]

	]
	context [
			node [ id 12 label "C" ]
			node [ id 16 label "O" ]
			node [ id 25 label "H" ]
			node [ id 26 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 12 target 13 label "-" ]
			 edge [ source 13 target 16 label "-" ]
			 edge [ source 13 target 25 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 26 label "-" ]
			node [ id 13 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_11_14)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_11_14, invert=True)
ch3oo_vitc_PATH_2_3 = """rule [
	ruleID " ch3oo_vitc_PATH_2_3"
	left [
			 edge [ source 9 target 10 label "=" ]
			node [ id 6 label "O." ]
			node [ id 10 label "C" ]

	]
	context [
			node [ id 9 label "C" ]
			node [ id 8 label "C" ]
			node [ id 15 label "O" ]
			node [ id 11 label "C" ]
			node [ id 19 label "O" ]
			node [ id 2 label "O" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 15 label "-" ]
			 edge [ source 10 target 11 label "-" ]
			 edge [ source 10 target 19 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 9 label "-" ]
			 edge [ source 9 target 10 label "-" ]
			node [ id 10 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_2_3)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_2_3, invert=True)
ch3oo_vitc_PATH_3_5 = """rule [
	ruleID " ch3oo_vitc_PATH_3_5"
	left [
			 edge [ source 9 target 10 label "=" ]
			node [ id 6 label "O." ]
			node [ id 9 label "C" ]

	]
	context [
			node [ id 8 label "C" ]
			node [ id 10 label "C" ]
			node [ id 15 label "O" ]
			node [ id 11 label "C" ]
			node [ id 19 label "O" ]
			node [ id 2 label "O" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 15 label "-" ]
			 edge [ source 10 target 11 label "-" ]
			 edge [ source 10 target 19 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 10 label "-" ]
			 edge [ source 9 target 10 label "-" ]
			node [ id 9 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_3_5)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_3_5, invert=True)
ch3oo_vitc_PATH_4_7 = """rule [
	ruleID " ch3oo_vitc_PATH_4_7"
	left [
			 edge [ source 15 target 18 label "-" ]
			node [ id 6 label "O." ]
			node [ id 15 label "O" ]

	]
	context [
			node [ id 9 label "C" ]
			node [ id 18 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 9 target 15 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 18 label "-" ]
			node [ id 15 label "O." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_4_7)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_4_7, invert=True)
ch3oo_vitc_PATH_5_8 = """rule [
	ruleID " ch3oo_vitc_PATH_5_8"
	left [
			 edge [ source 19 target 20 label "-" ]
			node [ id 6 label "O." ]
			node [ id 19 label "O" ]

	]
	context [
			node [ id 10 label "C" ]
			node [ id 20 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 10 target 19 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 20 label "-" ]
			node [ id 19 label "O." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_5_8)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_5_8, invert=True)
ch3oo_vitc_PATH_8_11 = """rule [
	ruleID " ch3oo_vitc_PATH_8_11"
	left [
			 edge [ source 11 target 23 label "-" ]
			node [ id 6 label "O." ]
			node [ id 11 label "C" ]

	]
	context [
			node [ id 10 label "C" ]
			node [ id 12 label "C" ]
			node [ id 14 label "O" ]
			node [ id 23 label "H" ]
			node [ id 2 label "O" ]
			 edge [ source 10 target 11 label "-" ]
			 edge [ source 11 target 12 label "-" ]
			 edge [ source 11 target 14 label "-" ]
			 edge [ source 2 target 6 label "-" ]

	]
	right [
			 edge [ source 6 target 23 label "-" ]
			node [ id 11 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_8_11)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_8_11, invert=True)
