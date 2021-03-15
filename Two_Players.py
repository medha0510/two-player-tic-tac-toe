
from fn import *
a=['1','2','3']         #Row 1
b=['4','5','6']         #Row 2
c=['7','8','9']         #Row 3

print (a,'\n',b,'\n',c,'\n')
i=0

while True:                                                             
    if i%2==0:
        print ("X player's turn")
    else:
        print ("O player's turn")
    
    x=int(input("enter location "))                                    #Taking a input

    if x not in range(1,10):
        print ("invalid input")
        continue
    
    if i%2==0:                                                          #chance of player X
        if x<=3:
            if a[x-1]=='x' or a[x-1]=='o':
                print ("invalid input")
                continue
            a[x-1]='x'
        elif x<=6:
            if b[x-4]=='x' or b[x-4]=='o':
                print ("invalid input")
                continue
            b[x-4]='x'
        elif x<=9:
            if c[x-7]=='x' or c[x-7]=='o':
                print ("invalid input")
                continue
            c[x-7]='x'
        print (a,'\n',b,'\n',c,'\n')
        i+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):          #checking  for  winner
            break

    else:                                                               #chance of player O
        if x<=3:
            if a[x-1]=='x' or a[x-1]=='o':
                print ("invalid input")
                continue
            a[x-1]='o'
        elif x<=6:
            if b[x-4]=='x' or b[x-4]=='o':
                print ("invalid input")
                continue
            b[x-4]='o'
        elif x<=9:
            if c[x-7]=='x' or c[x-7]=='o':
                print ("invalid input")
                continue
            c[x-7]='o'
        print (a,'\n',b,'\n',c,'\n')
        i+=1
        if check_c(a,b,c) or check_r(a,b,c) or check_d(a,b,c):          #checking  for  winner
            break
    if i==9:                                                            #checking for draw of match
        print ("Match is draw ")
        break


