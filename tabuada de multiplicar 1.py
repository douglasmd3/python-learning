import time
while True:
 a = int(input("~> "))
 b = int(input("~> "))
 print ("."*12)
 for i in range(a,b+1):
    print ("{:2} X {:2} = {:2}".format(a,i,i*a))
    time.sleep(1)
 print ("."*12)
