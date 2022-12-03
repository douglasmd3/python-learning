n = int(input("digite um valor: "))
for i in range(1, 11):
    print("%.2d X %.2d = %.2d" % (n, i, i * n))
print("~/~" * 15)
for i in range(1, 11):
    print("%.2d + %.2d = %.2d" % (n, i, i + n))
