matrix=[[1,2,3,4],[5,6,7,8]]
#print(matrix[1][0])
x=matrix[0]
y=matrix[1]
#print(x,y)
p=0
h=0
while p<len(matrix):
         #print(len(matrix[p]))
         while h<len(matrix[p]):
                 print(matrix[p][h],end='')    
                 h=h+1 
         print()
         p=p+1
         h=0
# while h>0:
#         #print(h)
#         while p<h:
#                 print('*',end="")
#                 p=p+1
#         print()
#         h=h-1
#         p=0


p=5
h=0
# while p>0:
#         #print('*')
#         while h<p:
#                 print(h,end='')
#                 h=h+1 
#         print()
#         p=p-1
#         h=2
size = 5
for i in range(size):
    for j in range(1, size - i):
        print("j=",j, end="")
    for k in range(0, i + 1):
        print("*", end="")
    print('i=',i)
# i=0
# j=1
# k=0
# while i<=5:
#         while j<=5-1:
#                 print('j=',j,end='')
#                 j=j+1
#         while k<=i+1:
#                 print('k=',k,end='')
#                 k=k+1
#         print('i=',i) 
#         i=i+1
#         j=1
#         k=0

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

i=0
j=1
k=0
l=0
while i<=5:
        while j<=5-i:
                print("*",end='')
                j=j+1
        while k<=i+1:
                print(' ',end='')
                k=k+1
        while l<=i+1:
                print(' ',end='')
                l=l+1
        print()
        i=i+1
        j=1
        k=0
        l=0
