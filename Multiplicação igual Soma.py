#Tabuada python 6 Multiplicação sendo igual a soma de num em n vezes - melhorar e fazer também para potenciação
l = []
# R é igual ao 1ºNº (N vezes) da multiplicação - Define quantas vezes o 2ºNº será repetido numa soma;
# N é igual ao 2Nº da multiplicação, equivalendo a soma repetidas vezes de 2ºNº definida por 1ºN;
R = int(input("1ºNº da multiplicação [repetir quantas vezes]:"))
N = int(input("2ºNº da multiplicação [número para repetir]:"))
for i in range(R):
    l.append(N)
    s = sum (l)
print("="*50)
print(f"A multilpicação dos Números escolhicos é: {R} x {N} = {R*N}.")
print(f"Essa multiplicação também pode ser expressa por meio da\nsoma de N vezes({R}x) um número definido N({N}), gerando as parcelas:\n{l}\ne obtendo resultando: {s}.")
print("="*50)
print(f"Conclui - se que:\n{R} x {N} = {R*N}.\nÉ igual a soma de:\n{l}\nresultando em {s}.")
