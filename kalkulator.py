def get_info():
    print("Witaj to jest kalkulator")

def dodaj(a, b):
    wynik = a + b
    return wynik


a = int(input())
b = int(input())
get_info()
print(dodaj(a, b))