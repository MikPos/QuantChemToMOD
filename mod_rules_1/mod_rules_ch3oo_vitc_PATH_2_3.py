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
