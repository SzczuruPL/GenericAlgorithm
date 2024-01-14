import random
import math

# Dane wejściowe
pary_rozwiazn_poprawnych = [(-5, -150), (-4, -77), (-3, -30), (-2, 0), (-1, 10), (1/2, 131/8), (1, 18), (2, 25), (3, 32), (4, 75), (5, 130)]

# Funkcja celu
def funkcja_celu(a, b, c, d):
    pary_wynikow = []
    for x, y in pary_rozwiazn_poprawnych:
        f = a * pow(x, 3) + b * pow(x, 2) + c * x + d
        pary_wynikow.append((f, y))
    return pary_wynikow

# Algorytm genetyczny
def algorytm_genetyczny(rozmiar_populacji, liczba_generacji, wspolczynnik_mutacji):
    populacja = []

    # Inicjalizacja populacji
    for _ in range(rozmiar_populacji):
        osobnik = [random.randint(-15, 15) for _ in range(4)]
        populacja.append(osobnik)

    print("Początkowa populacja:")
    for i, osobnik in enumerate(populacja, 1):
        print(f"Osobnik {i}: {osobnik}")

    # Główna pętla algorytmu genetycznego
    for generacja in range(liczba_generacji):
        oceny = []
        chromosomy = [1, 2, 3]
        for osobnik in populacja:
            a, b, c, d = osobnik
            wyniki = funkcja_celu(a, b, c, d)
            suma_kwadratow_bledow = sum((math.pow(f - y, 2) for f, y in wyniki))
            oceny.append((suma_kwadratow_bledow, osobnik))

        oceny.sort()
        print(f"Funkcja celu:", min(oceny)[0])

        # Wybór najlepszych osobników używając metody ruletki
        suma_dopasowan = sum(1/ocena[0] for ocena in oceny)
        prawdopodobienstwa = [1/ocena[0] / suma_dopasowan for ocena in oceny]
        najlepsi = random.choices(oceny, weights=prawdopodobienstwa, k=int(0.2 * rozmiar_populacji))

        print(f"\nGeneracja {generacja + 1}:")
        for i, (ocena, osobnik) in enumerate(oceny, 1):
            print(f"Osobnik {i}: {osobnik}, Ocena: {ocena}")

        print("Prawdopodobieństwa wyboru:")
        for i, prawdopodobienstwo in enumerate(prawdopodobienstwa, 1):
            print(f"Osobnik {i}: {prawdopodobienstwo}")

        # Krzyżowanie
        nowa_populacja = []
        for _ in range(rozmiar_populacji - len(najlepsi)):
            rodzic1, rodzic2 = random.choices(najlepsi, k=2)
            punkt_krzyzowania = random.randint(0, len(chromosomy))
            potomek = rodzic1[1][:punkt_krzyzowania] + rodzic2[1][punkt_krzyzowania:]
            nowa_populacja.append(potomek)

        # Mutacja
        for osobnik in nowa_populacja:
            if random.random() < wspolczynnik_mutacji:
                indeks_mutacji = random.randint(0, len(chromosomy))
                osobnik[indeks_mutacji] += random.randint(-1, 1)

        # Aktualizacja populacji
        populacja = [osobnik[1] for osobnik in najlepsi] + nowa_populacja

    # Wybór najlepszego osobnika
    najlepszy_osobnik = min(oceny)
    return najlepszy_osobnik

# Parametry algorytmu genetycznego
rozmiar_populacji = 50
liczba_generacji = 100
wspolczynnik_mutacji = 0.2

# Uruchomienie algorytmu genetycznego
najlepszy_osobnik = algorytm_genetyczny(rozmiar_populacji, liczba_generacji, wspolczynnik_mutacji)

# Wyświetlenie wyników
print("\nNajlepsze współczynniki (a, b, c, d):", najlepszy_osobnik[1], "Funkcja celu:", najlepszy_osobnik[0])