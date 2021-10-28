n=int(input())
val=input()
array=val.split(" ")
final=list()
for i in range(50,n+50):
    final.append(i)
min_n=min(array)
ind=array.index(min(array))
final[ind]=0
i=0
count=1
while i<n:
    j=0
    temp='50'
    while j<n:
        '''print("array[j] :",i,array[j])
        print("temp :",temp)
        print("min :",min_n)'''
        #value=eval(array[j])
        if array[j]<temp and array[j]>min_n:
            temp=array[j]
        else:
            print("Else :")
            print("array[j] :",array[j])
            print("temp :",temp)
            print("min :",min_n)
        j+=1
    min_n=temp
   # print("min :",min_n)
    ind=array.index(min_n)
    final[ind]=count
    count+=1
    i+=1
print(*final,sep=" ")