liczba = int(input("Liczba uczniow: "))
suma = 0

for i in range(liczba):
    wynik = int(input())
    while wynik < 0 or wynik > 100:
        print("wynik niepoprawny")
        wynik = int(input())

    suma = suma + wynik

print(suma)

