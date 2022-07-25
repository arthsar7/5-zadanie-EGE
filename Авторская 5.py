import math
for N2 in range(1,1000):
    N1 = 120
    chet = [int(i) for i in (str(N1) + str(N2)) if int(i)%2==0 and i != '0']
    nechet = [int(i) for i in (str(N1) + str(N2)) if int(i)%2!=0]
    M1 = math.prod(chet) 
    M2 = math.prod(nechet)
    R = abs(M1-M2) 
    if R == 29:
            print(N2)
            


