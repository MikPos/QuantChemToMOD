ch3oo_vitc_PATH_3_5 = """rule [
	ruleID " ch3oo_vitc_PATH_3_5"
	left [
			 edge [ source 9 target 10 label "=" ]
			node [ id 6 label "O." ]
			node [ id 9 label "C" ]

	]
	context [
			node [ id 8 label "C" ]
			node [ id 7 label "O" ]
			node [ id 14 label "O" ]
			node [ id 10 label "C" ]
			node [ id 11 label "C" ]
			node [ id 19 label "O" ]
			node [ id 15 label "O" ]
			node [ id 18 label "H" ]
			node [ id 12 label "C" ]
			node [ id 23 label "H" ]
			node [ id 20 label "H" ]
			node [ id 2 label "O" ]
			node [ id 1 label "C" ]
			 edge [ source 8 target 9 label "-" ]
			 edge [ source 9 target 15 label "-" ]
			 edge [ source 7 target 8 label "=" ]
			 edge [ source 8 target 14 label "-" ]
			 edge [ source 10 target 11 label "-" ]
			 edge [ source 10 target 19 label "-" ]
			 edge [ source 15 target 18 label "-" ]
			 edge [ source 11 target 12 label "-" ]
			 edge [ source 11 target 14 label "-" ]
			 edge [ source 11 target 23 label "-" ]
			 edge [ source 19 target 20 label "-" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 1 target 2 label "-" ]

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
