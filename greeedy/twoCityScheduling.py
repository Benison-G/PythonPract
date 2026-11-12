def twoCityScheduling(costs):
    costs = sorted(costs, key=lambda cost: cost[0] - cost[1])

    n = len(costs) // 2
    ans = 0

    for i in range(n):
        ans = ans + costs[i][0];
        ans = ans + costs[i + n][1]

    return ans

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

print(twoCityScheduling(costs))
