import random as r
n=int(input('insert your n '))

a=[0]*n


for i in range(n):
    a[i]=r.randrange(1,100,1)

    print(a[i], end=' ')






 










































































































print()



print()

for i in range(n):
    key=a[i]
    for j in range(i):
        if a[j]<key:
            continue
        elif a[j]==key:
            continue
        else:
            c=a[i]
            a[i]=a[j]
            a[j]=c


           # tmp1=a[i]
           # tm2=a[j]
            """a[i]=tm2
            a[j]=tmp1
            a[i],a[j]=tm2,tmp1
            a[i]
            """ 
            #a[i],a[j]=a[j],a[i]


    




#for 
for i in range(n):
    print(a[i], end=' ')



def search_array(a:list, n:int, x:int):
    """
    Линейный поиск элемента x в массиве a длиной н.
    Если не найден: -1
    Возвращает индекс найденного элемента
    """
 
    key=-1
    i=0
    while i<n:
        if a[i]==x:
            key=i
            return key
        i+=1
    return key


print(search_array(a,n,x=int(input('i' ))))
