n = int(input("digite um valor: "))
for i in range(1, 11):
    print("%.2d X %.2d = %.2d" % (n, i, i * n))
print("~/~" * 10)
for i in range(1, 11):
    print("%.2d + %.2d = %.2d" % (n, i, i + n))
print("~/~" * 10)
for i in range(1, 11):
    for j in range (1, 11):
        print("%.2d + %.2d = %.2d" % (i, j, i + j))
    print("-" * 20)
for i in range(1, 11):
    for j in range (1, 11):
        print("%.2d X %.2d = %.2d" % (i, j, i * j))
    print("-" * 20)
