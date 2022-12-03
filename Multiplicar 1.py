nome = input("Olá, para começar informe um nome: ")
opcao = int(input(f"""
01 - Estudar tabuada.
02 - Resolver tabuada. 
{nome} informe uma  das opções acima: """))

print("-"*50)

if opcao == 1:
    
    opcao2 = int(input(f"""
01 - Estudar a tabuada completa [1-10].
02 - Estudar a tabuada por valor definido.
{nome} informe uma  das opções de estudo acima: """))

    if opcao2 == 1:
        
        for i in range(1, 11):
            for j in range (1, 11):
                print("%.2d X %.2d = %.2d" % (i, j, i * j))
            print("-" * 20)
        
    if opcao2 == 2:
        
        n = int(input("digite um valor: "))
        for i in range(1, 11):
            print("%.2d X %.2d = %.2d" % (n, i, i * n))
        print("~/~" * 10)
        
if opcao == 2:
    
    opcao3 = int(input(f"""
    01 - resolver a tabuada completa [1-10] por Nº definido.
    02 - resolver a tabuada por 2 valores definido.
    {nome} informe uma  das opções de resolução acima: """))
    
    if opcao3 == 1:
        
        numero = int(input(f"{nome} defina um número para resolver as multiplicações:"))
    
        for i in range (11):
            resoluc = i * numero
            user = int(input("%d x %d = " % (numero,i)))
            
            if user == resoluc:
                print(f"Acertou, Miseravi ;) - valeu {nome} !")
            
            else:
                print(f" Que dó, que dó :( - {nome}, você Errou. ")
        
    if opcao3 == 2:
        
        print(f"{nome} defina abaixo os dois valores que deseja resolver:")
        a = int(input("1ºNº ~> "))
        b = int(input("2ºNº ~> "))
        print ("."*12)
        
        soluc = int(input(f"{a} X {b} = "))
        
        if soluc == b*a:
            print(f"Acertou, Miseravi ;) - valeu {nome} !")
        
        else:
            print(f"""Que dó, que dó :( - {nome}, você Errou. 
            resolução é {a:2} X {b:2} = {a*b:2}""")
