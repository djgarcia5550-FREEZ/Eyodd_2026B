"""
escrbir un programa que calcule 
la suma de los "n" numeros naturales.
por elemplo si n= 100, el progama 
calculara la suma de 1 al 100
42

"""
# Importamos biblioteca
import time
def sum_of_n(n):
    total_sum = 0
    # sumando los "n" numeros
    # Ciclo for
    for number in range(1, n + 1):
        total_sum = total_sum + number
    return total_sum
dataset = [] 
for repetition in range(1,11):
    timestamp_01 = time.time()
    n = repetition*500
    result = sum_of_n(n)
    timestamp_02 = time.time()
    elapsed_time =  round((timestamp_02 - timestamp_01) * 1e6,2)
    dataset.append( (n,elapsed_time,result) )
for tup in dataset:
    print(tup)
n = 500
total_sum = 0
total_sum = sum_of_n(n)
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01) * 1e6:.2f} µs")