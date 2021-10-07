array = input("Пожалуйста,введите значения массива (через пробел):").split()
for r in range(len(array)):
    array[r]=int(array[r])
delta=int(input("Введите значение Delta:"))
minimum=array[0]
for q in range(len(array)):
    if array[q] < minimum:
        minumum=array[q]
f=0
for q in range(len(array)):
    if array[q]==minimum + delta:
        f=f+1
print(f)
        


        
    
    
