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



row=int(input("Enter number="))
count=1
for i in range(1,row+1):
    for j in range(i):
        print(count,end=" ")
    count+=1
    print()