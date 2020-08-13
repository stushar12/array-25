import sys

n=int(input("Enter number of elements of array1: "))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)


dir=0
if(sum(arr)==arr[0]*n):
        print("It is constant ")
        exit()

if(arr[1]>=arr[0]):
        for i in range(1,n-1):
                if(arr[i+1]>=arr[i]):
                        dir=1
                else:
                        dir=0
                        break




if(arr[1]<=arr[0] and dir==0):
        for i in range(1,n-1):
                if(arr[i+1]<=arr[i]):
                        dir=-1
                else:
                        dir=0
                        break


if dir==0:
        print("Not Monotonic")
elif dir==1:
        print("Strictly increasing")
elif dir==-1:
        print("Strictly decreasing")