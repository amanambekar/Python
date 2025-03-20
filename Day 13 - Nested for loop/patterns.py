# Left increamental Triangle
'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()
'''

'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for j in range(i,row+1):
        print("*",end=" ")
    print()
'''
'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
'''

'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for j in range(i):
        print(i,end=" ")
    print()
'''


'''
row=int(input("Enter number="))
count=0
for i in range(1,row+1):
    for j in range(i):
        count+=1
        print(count,end=" ")
    print()
'''



'''
row=int(input("Enter number="))
count=1
for i in range(1,row+1):
    count=i
    for j in range(1,i+1):
           print(count,end=" ")
           count=count+(row-j)
    print()
'''
'''row=int(input("Enter number="))
for i in range(1,row+1):
    for k in range(row-i):
      print(end="  ")
    for j in range (i):
       print("*",end=" ")
    print()'''

'''
row=int(input("Enter number="))
for i in range(row,0,-1):
    for k in range(row-i):
      print(end="  ")
    for j in range (i):
       print("*",end=" ")
    print()
'''
'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for k in range(row-i):
      print(end=" ")
    for j in range (i):
       print("*",end=" ")
    print()
'''
'''
row=int(input("Enter number="))
for i in range(row,0,-1):
    for k in range(row-i):
      print(end=" ")
    for j in range (i):
       print("*",end=" ")
    print()
'''
'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for k in range(row-i):
      print(end=" ")
    for j in range (i):
       print("*",end=" ")
    print()
for i in range(row-1,0,-1):
    for k in range(row-i):
      print(end=" ")
    for j in range (i):
       print("*",end=" ")
    print()
'''
'''
row=int(input("Enter number="))
for i in range(1,row+1):
    for k in range(row-i):
      print(end="  ")
    for j in range (2*i-1):
       print("*",end=" ")
    print()
'''
'''
for i in range(8):
    for j in range(8):
        if i==j:
           print("1" ,end=" ")
        else:
          print("0",end=" ") 
    print()
'''
'''
count=1
for i in range(1,7):
    for j in range(1,6):
        if i%2==0:
            if j%2==0:
             print(count,end=" ") 
             count+=1
            else:
                print("*",end=" ")
        else:
            if j%2==0:
                print("*",end=" ")
            else:
                print(count,end=" ") 
                count+=1
    print()
'''
'''
for i in range(1,4):
    for j in range(1,4):
        if i==1 or i==3 or j==1 or j==3:
           print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
'''

'''
row=int(input("Enter row="))
col=int(input("Enter col="))
for i in range(1,row+1):
    for j in range(1,col+1):
        if i==1 or i==row or j==1 or j==col:
           print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
'''

'''
row=int(input("Enter row="))
count=0
for i in range(1,row+1):
    for j in range(1,row+1):
        if i%2==0:
           print(count,end=" ")
           count-=1
        else:
         count+=1
         print(count,end=" ")
    count+=row
    print()
'''

row=int(input("Enter row=")) 
a=0
b=1
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==1 and j==1:
           print(a,end=" ")
        elif i==1 and j==2:
           print(b,end=" ")
        else:
           c=a+b
           print(c,end=" ")
           a=b
           b=c
    print()
            
          
       


