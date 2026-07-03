ch3oo_vitc_PATH_4_7 = """rule [
	ruleID " ch3oo_vitc_PATH_4_7"
	left [
			 edge [ source 15 target 18 label "-" ]
			node [ id 6 label "O." ]
			node [ id 15 label "O" ]

	]
	context [
			node [ id 9 label "C" ]
			node [ id 8 label "C" ]
			node [ id 10 label "C" ]
			node [ id 18 label "H" ]
			node [ id 2 label "O" ]
			node [ id 1 label "C" ]
			 edge [ source 9 target 15 label "-" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 10 label "=" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 1 target 2 label "-" ]

	]
	right [
			 edge [ source 6 target 18 label "-" ]
			node [ id 15 label "O." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_4_7)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_4_7, invert=True)
