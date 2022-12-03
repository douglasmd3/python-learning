num = [0,1,2,3,4,5,6,7,8,9,10]
print ("TABUADA DE MULTIPLICAÇÃO DE 0 A 10:\n")
for i in range(11):
    print("Tabuada de {}:".format(i+0))
    for j in num:
        print ("{:} x {:2} = {}".format(i,j,i*j))
    print("-" * 10)
