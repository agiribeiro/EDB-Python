moedas = [100, 50, 5, 1]
sol = []
soma = 0
troco = 60

i = 0
while i < len(moedas) and soma != troco:
    if soma + moedas[i] <= troco:
        sol.append(moedas[i])
        soma += moedas[i]
    else:
        i += 1

print(sol)
