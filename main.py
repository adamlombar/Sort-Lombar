#vložení modulu random
import random

#bogo sort

#vytvoření pole
arraya=[78, 63, 2, 54, 96, 33, 41, 20 ,15, 7]
#definování třídění
def is_sorted(arraya):
    for i in range(1, len(arraya)):
        if arraya[i]<arraya[i-1]:
            return False
    return True
#definování bogo sortu
def bogosort(arraya):
    count = 0
    while not is_sorted(arraya):
        random.shuffle(arraya)
        count += 1
        print("Pokus", count, ":", arraya)
    print("seznam seřazen po (count) pokusech.")

bogosort(arraya)
print("bogo:", arraya)

#bubble sort

arrayb = [4, 87, 31, 70, 96, 11, 2, 42, 63, 28]
#definování bubble sortu
def bubble_sort():
    n=len(arrayb)
    for i in range(n-1): #cyklus na vrácení na začátek
        for j in range (0, n-i-1):
            if arrayb[j]>arrayb[j+1]: #porovnání čísel
                arrayb[j], arrayb[j+1]=arrayb[j+1],arrayb[j] #vyměňování pozic
    return arrayb

print("bubble:", bubble_sort()) 

#selection sort
arrayc = [55, 12, 67, 43, 8, 32, 25, 90, 19, 5]
#definování selection sortu
def selection_sort():
    n = len(arrayc)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arrayc[j] < arrayc[min_idx]: #porovnání čísel
                min_idx = j
        arrayc[i], arrayc[min_idx] = arrayc[min_idx], arrayc[i]
    return arrayc

print("selection:", selection_sort())

#insertion sort

arrayd = [4, 53, 82, 1, 91, 74, 89, 43, 17, 31]

#definování insertion sortu
def insertion_sort():
    n = len(arrayd) 
    for i in range(1, n): 
        current_value = arrayd[i] 
        insert_index = i          
        for j in range(i - 1, -1, -1): 
            if arrayd[j] > current_value: 
                arrayd[j + 1] = arrayd[j] #posun hodnoty doprava
                insert_index = j  
            else:
                break  
        arrayd[insert_index] = current_value #vložení čísla na správné místo
        print(arrayd)

insertion_sort()
print("insertion:", arrayd)