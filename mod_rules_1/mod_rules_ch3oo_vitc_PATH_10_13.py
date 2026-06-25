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
