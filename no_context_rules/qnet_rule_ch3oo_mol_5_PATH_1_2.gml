rule [
	ruleID " ch3oo_mol_5_PATH_1_2"
	left [
			 edge [ source 11 target 13 label "-" ]
			 edge [ source 13 target 16 label "-" ]
			node [ id 6 label "O." ]
			node [ id 11 label "C." ]

	]
	context [
			node [ id 11 label "C" ]
			node [ id 13 label "C" ]
			node [ id 16 label "H" ]
			node [ id 6 label "O" ]

	]
	right [
			 edge [ source 11 target 13 label "=" ]
			 edge [ source 6 target 16 label "-" ]
			node [ id 6 label "O" ]
			node [ id 11 label "C" ]

	]
]