
s_2_p_2_a_2 = """Q:Bob and Gopher are playing a game. The world can be in state s1 or s2. Only Bob can see the state that the world is in. Gopher can see what Bob plays but cannot see the state of the world. They get rewards with the following rules:
1. World: s1 then Bob:b1 then Gopher:a1, then; Bob's reward br111={payoff_matrix[0][0][0][1]}; Gopher's reward gr111={payoff_matrix[0][0][0][0]}
2. World: s1 then Bob:b1 then Gopher:a2, then; Bob's reward br112={payoff_matrix[0][0][1][1]}; Gopher's reward gr112={payoff_matrix[0][0][1][0]}
3. World: s1 then Bob:b2 then Gopher:a1, then; Bob's reward br121={payoff_matrix[0][1][0][1]}; Gopher's reward gr121={payoff_matrix[0][1][0][0]}
4. World: s1 then Bob:b2 then Gopher:a2, then; Bob's reward br122={payoff_matrix[0][1][1][1]}; Gopher's reward gr122={payoff_matrix[0][1][1][0]}
5. World: s2 then Bob:b1 then Gopher:a1, then; Bob's reward br211={payoff_matrix[1][0][0][1]}; Gopher's reward gr211={payoff_matrix[1][0][0][0]}
6. World: s2 then Bob:b1 then Gopher:a2, then; Bob's reward br212={payoff_matrix[1][0][1][1]}; Gopher's reward gr212={payoff_matrix[1][0][1][0]}
7. World: s2 then Bob:b2 then Gopher:a1, then; Bob's reward br221={payoff_matrix[1][1][0][1]}; Gopher's reward gr221={payoff_matrix[1][1][0][0]}
8. World: s2 then Bob:b2 then Gopher:a2, then; Bob's reward br222={payoff_matrix[1][1][1][1]}; Gopher's reward gr222={payoff_matrix[1][1][1][0]}
Bob and Gopher want to maximize their rewards. Bob does not think about their opponent and only plays the action with the highest expected reward. Gopher thinks about other players' reasoning. What action should Gopher play?"""

s_3_p_2_a_2 = """Q:Bob and Gopher are playing a game. The world can be in state s1, s2 or s3. Only Bob can see the state that the world is in. Gopher can see what Bob plays but cannot see the state of the world. They get rewards with the following rules:
1. World: s1 then Bob:b1 then Gopher:a1, then; Bob's reward br111={payoff_matrix[0][0][0][1]}; Gopher's reward gr111={payoff_matrix[0][0][0][0]}
2. World: s1 then Bob:b1 then Gopher:a2, then; Bob's reward br112={payoff_matrix[0][0][1][1]}; Gopher's reward gr112={payoff_matrix[0][0][1][0]}
3. World: s1 then Bob:b2 then Gopher:a1, then; Bob's reward br121={payoff_matrix[0][1][0][1]}; Gopher's reward gr121={payoff_matrix[0][1][0][0]}
4. World: s1 then Bob:b2 then Gopher:a2, then; Bob's reward br122={payoff_matrix[0][1][1][1]}; Gopher's reward gr122={payoff_matrix[0][1][1][0]}
5. World: s2 then Bob:b1 then Gopher:a1, then; Bob's reward br211={payoff_matrix[1][0][0][1]}; Gopher's reward gr211={payoff_matrix[1][0][0][0]}
6. World: s2 then Bob:b1 then Gopher:a2, then; Bob's reward br212={payoff_matrix[1][0][1][1]}; Gopher's reward gr212={payoff_matrix[1][0][1][0]}
7. World: s2 then Bob:b2 then Gopher:a1, then; Bob's reward br221={payoff_matrix[1][1][0][1]}; Gopher's reward gr221={payoff_matrix[1][1][0][0]}
8. World: s2 then Bob:b2 then Gopher:a2, then; Bob's reward br222={payoff_matrix[1][1][1][1]}; Gopher's reward gr222={payoff_matrix[1][1][1][0]}
9. World: s3 then Bob:b1 then Gopher:a1, then; Bob's reward br311={payoff_matrix[2][0][0][1]}; Gopher's reward gr311={payoff_matrix[2][0][0][0]}
10. World: s3 then Bob:b1 then Gopher:a2, then; Bob's reward br312={payoff_matrix[2][0][1][1]}; Gopher's reward gr312={payoff_matrix[2][0][1][0]}
11. World: s3 then Bob:b2 then Gopher:a1, then; Bob's reward br321={payoff_matrix[2][1][0][1]}; Gopher's reward gr321={payoff_matrix[2][1][0][0]}
12. World: s3 then Bob:b2 then Gopher:a2, then; Bob's reward br322={payoff_matrix[2][1][1][1]}; Gopher's reward gr322={payoff_matrix[2][1][1][0]}

Bob and Gopher want to maximize their rewards. Bob does not think about their opponent and only plays the action with the highest expected reward. Gopher thinks about other players' reasoning. What action should Gopher play?"""

s_2_p_2_a_3 = """Q:Bob and Gopher are playing a game. The world can be in state s1 or s2. Only Bob can see the state that the world is in. Gopher can see what Bob plays but cannot see the state of the world. They get rewards with the following rules:
1. World: s1 then Bob:b1 then Gopher:a1, then; Bob's reward br111={payoff_matrix[0][0][0][1]}; Gopher's reward gr111={payoff_matrix[0][0][0][0]}
2. World: s1 then Bob:b1 then Gopher:a2, then; Bob's reward br112={payoff_matrix[0][0][1][1]}; Gopher's reward gr112={payoff_matrix[0][0][1][0]}
3. World: s1 then Bob:b2 then Gopher:a1, then; Bob's reward br121={payoff_matrix[0][1][0][1]}; Gopher's reward gr121={payoff_matrix[0][1][0][0]}
4. World: s1 then Bob:b2 then Gopher:a2, then; Bob's reward br122={payoff_matrix[0][1][1][1]}; Gopher's reward gr122={payoff_matrix[0][1][1][0]}
5. World: s1 then Bob:b3 then Gopher:a1, then; Bob's reward br131={payoff_matrix[0][2][0][1]}; Gopher's reward gr131={payoff_matrix[0][2][0][0]}
6. World: s1 then Bob:b3 then Gopher:a2, then; Bob's reward br132={payoff_matrix[0][2][1][1]}; Gopher's reward gr132={payoff_matrix[0][2][1][0]}
7. World: s2 then Bob:b1 then Gopher:a1, then; Bob's reward br211={payoff_matrix[1][0][0][1]}; Gopher's reward gr211={payoff_matrix[1][0][0][0]}
8. World: s2 then Bob:b1 then Gopher:a2, then; Bob's reward br212={payoff_matrix[1][0][1][1]}; Gopher's reward gr212={payoff_matrix[1][0][1][0]}
9. World: s2 then Bob:b2 then Gopher:a1, then; Bob's reward br221={payoff_matrix[1][1][0][1]}; Gopher's reward gr221={payoff_matrix[1][1][0][0]}
10. World: s2 then Bob:b2 then Gopher:a2, then; Bob's reward br222={payoff_matrix[1][1][1][1]}; Gopher's reward gr222={payoff_matrix[1][1][1][0]}
11. World: s2 then Bob:b3 then Gopher:a1, then; Bob's reward br231={payoff_matrix[1][1][0][1]}; Gopher's reward gr231={payoff_matrix[1][2][0][0]}
12. World: s2 then Bob:b3 then Gopher:a2, then; Bob's reward br232={payoff_matrix[1][1][1][1]}; Gopher's reward gr232={payoff_matrix[1][2][1][0]}
Bob and Gopher want to maximize their rewards. Bob does not think about their opponent and only plays the action with the highest expected reward. Gopher thinks about other players' reasoning. What action should Gopher play when Bob plays b1 or b2 or b3?"""


a_222_0 = [
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ]
        ],
    [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ]
    ]
]

a_222_1 = [
    [
        [
            [3, 3], [-1, 5]
            ],
        [
            [1, 1], [-2, 1]
        ]
        ],
    [
        [
            [1, 1], [-2, 1]
            ],
        [
            [3, 3], [-1, 5]
        ]
    ]
]

a_222_2 = [
    [
        [
            [0, 0], [5, 0]
            ],
        [
            [-5, 5], [5, 7]
        ]
    ],
    [
        [
            [0, 5], [5, 7]
            ],
        [
            [-5, 0], [-3, 0]
        ]
        ],
]

a_222_3 = [
   [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ]
    ],
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ]
        ]
]

a_222_4 = [

    [
        [
            [-3, 1], [2, 4]
            ],
        [
            [1, -1], [-2, 2]
        ]
        ],
    [
        [
            [1, -1], [2, 2]
            ],
        [
            [5, 1], [1, 1]
        ]
    ]
]


a_322_0 = [
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ]
        ],
    [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ]
    ],
    [
        [
            [1, -1], [4, -4]
            ],
        [
            [3, 3], [1, 1]
        ]
    ]
]

a_322_1 = [
    [
        [
            [3, 3], [-1, 5]
            ],
        [
            [1, 1], [-2, 1]
        ]
        ],
    [
        [
            [1, 1], [-2, 1]
            ],
        [
            [3, 3], [-1, 5]
        ]
    ],
       [
        [
            [4, -4], [1, -1]
            ],
        [
            [1, 1], [4, -4]
        ]
    ] 
]

a_322_2 = [
    [
        [
            [0, 0], [5, 0]
            ],
        [
            [-5, 5], [5, 7]
        ]
    ],
    [
        [
            [0, 5], [5, 7]
            ],
        [
            [5, 0], [-3, 0]
        ]
        ],
    [
        [
            [1, 1], [-2, 1]
            ],
        [
            [3, 3], [-1, 5]
        ]
    ]
]

a_322_3 = [
   [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ]
    ],
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ]
    ],
    [
       [
            [3, 3], [-1, 5]
        ],
    [
            [1, 1], [-2, 1]
            ],
     
    ],
]

a_322_4 = [

    [
        [
            [5, 1], [-2, 4]
            ],
        [
            [1, -1], [-2, 2]
        ]
        ],
    [
        [
            [1, -1], [2, -2]
            ],
        [
            [5, 1], [1, -1]
        ]
    ],
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ]
    ]
]


a_223_0 = [
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ],
        [
            [5, 1], [1, -1]
        ]
        ],
    [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ],
        [
            [1, -1], [-4, 4]
        ]
    ]
]

a_223_1 = [
    [
        [
            [3, 3], [-1, 5]
            ],
        [
            [1, 1], [-2, 1]
        ],
        [
            [4, -4], [1, -1]
            ],

        ],
    [
        [
            [1, 1], [-2, 1]
            ],
        [
            [3, 3], [-1, 5]
        ],
        [
            [1, 1], [4, -4]
        ]
    ]
]

a_223_2 = [
    [
        [
            [0, 0], [5, 0]
            ],
        [
            [-5, 5], [5, 7]
        ],
        [
            [3, 3], [-1, 5]
        ]
    ],
    [
        [
            [0, 5], [5, 7]
            ],
        [
            [-5, 0], [-3, 0]
        ],
        [
            [1, 1], [-2, 1]
            ],
        ],
]

a_223_3 = [
   [
        [
            [1, -1], [2, -2]
            ],
        [
            [3, -3], [1, -1]
        ],
        [
            [1, 1], [-2, 1]
        ]
    ],
    [
        [
            [-2, 2], [-3, 3]
            ],
        [
            [1, -1], [-4, 4]
        ],
        [
            [0, 1], [-1, 3]
        ]
        ]
]

a_223_4 = [

    [
        [
            [-3, 1], [2, 4]
            ],
        [
            [1, -1], [-2, 2]
        ],
        [
            [-2, 1], [1, 0]
            ]
        ],
    [
        [
            [1, -1], [2, 2]
            ],
        [
            [5, 1], [1, 1]
        ],
        [
            [1, 2], [-3, 1]
        ]
    ]
]