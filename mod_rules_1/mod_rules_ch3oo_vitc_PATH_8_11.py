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
