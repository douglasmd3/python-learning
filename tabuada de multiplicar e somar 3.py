n = int(input("digite um valor: "))
for i in range(1, 11):
    print("%.2d X %.2d = %.2d" % (n, i, i * n))
print("~/~" * 10)
for i in range(1, 11):
    print("%.2d + %.2d = %.2d" % (n, i, i + n))
n = int(input("digite um valor: "))
print ("-" * 20)
# Tabuada de adição:
c = 1
while c <= 10 :
    print("%.2d + %.2d = %.2d" % (n, c, n + c))
    c = c + 1
print ("." * 20)
# Tabuada de multiplicação:
c = 1
while c <= 10 :
    print("%.2d x %.2d = %.2d" % (n, c, n * c))
    c = c + 1
print("Fim!")
