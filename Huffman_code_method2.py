ex44 = { '1': 0.49, '2': 0.26, '3': 0.12, '4': 0.04, '5': 0.04, '6': 0.03, '7': 0.02}
#ex44 = { '1': 0.49, '2': 0.26}
def huffman_method2(prob):

    temp = prob.copy()
    new_prob = dict()
    temp1 = dict()

    while len(prob) > 1:
        sorted_prob = sorted(prob.items(), key=lambda prob:prob[1])
        get_zero = sorted_prob[0][0]
        get_one = sorted_prob[1][0]
        new_prob[get_zero] = "0"
        new_prob[get_one] = "1"
        del prob[get_one], prob[get_zero]
        prob[get_zero + get_one] = sorted_prob[0][1] + sorted_prob[1][1]

    new_prob1 = [(x,new_prob[x]) for x in new_prob]
    print(new_prob1)
    length = len(new_prob1) + 1
    for item in temp:
        a = item[0]
        while


        # if a in new_prob1[length-1][0]:
        #     if temp1[a] in None: temp1[a] = new_prob1[length][1]
        #     else: temp1[a] += new_prob1[length][1]
        # length -= 1

    return new_prob

print(huffman_method2(ex44))

