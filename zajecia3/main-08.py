liczba = int(input())
poprawne = 0

for i in range(1, liczba+1):
    print(f"Podaj kwadrat liczby {i}")
    wynik = int(input())
    proby = 1

    while wynik != i*i and proby < 3:
        print("Błędna")
        wynik = int(input())
        proby = proby + 1
    if wynik == i*i:
        print("Poprawna")
        poprawne = poprawne + 1
    else:
        print("Błędna")
print(f"Poprawnie rozwiazane {poprawne}")