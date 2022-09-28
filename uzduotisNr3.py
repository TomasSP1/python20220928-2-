import math

numOne = int(input("Iveskite prizmes pagrindo krastines ilgi: "))
numTwo = int(input("Iveskite prizmes auksti: "))

# Cilindro/Ritinio tūrio formulė yra: V = π*r2*h

numThree = math.pi * ((numOne / 2) * 2) * numTwo

def truncate_float(n, places):
    return int(n * (10 ** places)) / 10 ** places




print(truncate_float(numThree, 1))

