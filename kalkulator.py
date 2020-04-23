def get_info():
    print("Witaj to jest kalkulator")

def dodaj(a, b):
    wynik = a + b
    return wynik

def odejmij(a,b):
    return a - b

a = int(input())
b = int(input())
get_info()
print(dodaj(a, b))
print(odejmij(a,b))

print("Koniec programu")