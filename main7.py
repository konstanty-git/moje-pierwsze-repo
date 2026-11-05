first = int(input("Ile dni liczy tydzień? "))
if first == 7:
    print("Poprawna odpowiedz")
elif first != 7:
    print("Zła odpowiedz")
    first = int(input("Ile dni liczy tydzień?"))
    if first == 7:
        print("Poprawna odpowiedz")
    elif first != 7:
        print("Druga zła odpowiedz")