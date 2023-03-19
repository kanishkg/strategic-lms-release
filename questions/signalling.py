template = """Q:Bob and Gopher are playing a game. Bob can signal Gopher the action that he intends to play. Bob can say the truth or lie about his intentions. They get rewards with the following rules:
1. Bob:b1 and Gopher:a1, then; Bob's reward br11={payoff_matrix[0][0][1]}; Gopher's reward gr11={payoff_matrix[0][0][0]}
2. Bob:b1 and Gopher:a2, then; Bob's reward br12={payoff_matrix[1][0][1]}; Gopher's reward gr12={payoff_matrix[1][0][0]}
3. Bob:b2 and Gopher:a1, then; Bob's reward br21={payoff_matrix[0][1][1]}; Gopher's reward gr21={payoff_matrix[0][1][0]}
4. Bob:b2 and Gopher:a2, then; Bob's reward br22={payoff_matrix[1][1][1]}; Gopher's reward gr22={payoff_matrix[1][1][0]}
Bob and Gopher want to maximize their rewards. Bob tells Gopher that he's going to play b{op_act}. Bob assumes that Gopher will believe whatever he says. Gopher needs to infer from the rewards if Bob is telling the truth. What action should Gopher play?\nA"""