ch3oo_vitc_PATH_10_13 = """rule [
	ruleID " ch3oo_vitc_PATH_10_13"
	left [
			 edge [ source 13 target 25 label "-" ]
			node [ id 6 label "O." ]
			node [ id 13 label "C" ]

	]
	context [
			node [ id 12 label "C" ]
			node [ id 11 label "C" ]
			node [ id 17 label "O" ]
			node [ id 24 label "H" ]
			node [ id 16 label "O" ]
			node [ id 22 label "H" ]
			node [ id 25 label "H" ]
			node [ id 26 label "H" ]
			node [ id 2 label "O" ]
			node [ id 1 label "C" ]
			 edge [ source 12 target 13 label "-" ]
			 edge [ source 13 target 16 label "-" ]
			 edge [ source 13 target 26 label "-" ]
			 edge [ source 11 target 12 label "-" ]
			 edge [ source 12 target 17 label "-" ]
			 edge [ source 12 target 24 label "-" ]
			 edge [ source 16 target 22 label "-" ]
			 edge [ source 2 target 6 label "-" ]
			 edge [ source 1 target 2 label "-" ]

	]
	right [
			 edge [ source 6 target 25 label "-" ]
			node [ id 13 label "C." ]
			node [ id 6 label "O" ]

	]
]"""
rule1_F = Rule.fromGMLString(ch3oo_vitc_PATH_10_13)
rule1_B = Rule.fromGMLString(ch3oo_vitc_PATH_10_13, invert=True)
