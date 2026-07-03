rule [
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

	]
	right [
			 edge [ source 6 target 23 label "-" ]
			 edge [ source 9 target 12 label "=" ]
			node [ id 6 label "O" ]
			node [ id 9 label "C" ]

	]
]