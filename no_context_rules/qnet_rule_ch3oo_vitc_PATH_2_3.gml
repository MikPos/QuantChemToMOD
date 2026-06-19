rule [
	ruleID " ch3oo_vitc_PATH_2_3"
	left [
			 edge [ source 9 target 10 label "=" ]
			node [ id 6 label "O." ]
			node [ id 10 label "C" ]

	]
	context [
			node [ id 9 label "C" ]
			node [ id 10 label "C" ]
			node [ id 6 label "O" ]

	]
	right [
			 edge [ source 6 target 9 label "-" ]
			 edge [ source 9 target 10 label "-" ]
			node [ id 10 label "C." ]
			node [ id 6 label "O" ]

	]
]