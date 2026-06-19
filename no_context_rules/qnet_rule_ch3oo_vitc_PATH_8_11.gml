rule [
	ruleID " ch3oo_vitc_PATH_8_11"
	left [
			 edge [ source 11 target 23 label "-" ]
			node [ id 6 label "O." ]
			node [ id 11 label "C" ]

	]
	context [
			node [ id 11 label "C" ]
			node [ id 23 label "H" ]
			node [ id 6 label "O" ]

	]
	right [
			 edge [ source 6 target 23 label "-" ]
			node [ id 11 label "C." ]
			node [ id 6 label "O" ]

	]
]