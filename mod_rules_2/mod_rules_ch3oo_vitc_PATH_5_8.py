ch3oo_vitc_PATH_5_8 = """rule [
	ruleID " ch3oo_vitc_PATH_5_8"
	left [
			 edge [ source 19 target 20 label "-" ]
			node [ id 6 label "O." ]
			node [ id 19 label "O" ]

	]
	context [
			node [ id 10 label "C" ]
			node [ id 9 label "C" ]
			node [ id 11 label "C" ]
			node [ id 20 label "H" ]
			node [ id 2 label "O" ]
			node [ id 1 label "C" ]
			 edge [ source 10 target 19 label "-" ]
			 edge [ source 9 target 10 label "=" ]
			 edge [ source 10 target 11 label "-" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 1 target 2 label "-" ]

	]
	right [
			 edge [ source 6 target 20 label "-" ]
			node [ id 19 label "O." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_5_8)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_5_8, invert=True)
