# Készítsen fg-t, ami általános célú inputot valósít meg egész számokhoz!
# Paraméterek:
# - Az inputtal kiirandó szöveg (str)
# - A bevihető legkisebb érték (int)
# - A bevihető legnagyobb érték (int)
# Az adatbekérét mindaddíg ismételje, amíg az érték a határok között van.
# Jelenítse meg az ismétlés okát!

import math
from Epulet import Epulet


def my_input(szöveg: str, min_érték: int, max_érték: int) -> int:
    while True:
        x: int = int(input(f"{szöveg}: "))
        if x >= min_érték and x <= max_érték:
            return x
        else:
            if x < min_érték:
                print(f"Az input érték nem lehet kisebb, mint {min_érték}")
            else:
                print(f"Az input érték nem lehet nagyobb, mint {max_érték}")


def e_betűk_száma(szöveg: str) -> int:
    e_db: int = 0
    for b in szöveg:
        # if b == 'e' or b == 'E':
        # if b in ['e', 'E']:
        if b.upper() == "E":
            e_db += 1
    return e_db


def main() -> None:
    # Saját függvény készítése
    hónap: int = my_input("Kérem a hónap számát", 1, 12)
    print(hónap)

    # Kiírás két tizedesjegyre "kerekítve"
    pi: float = math.pi
    print(f"A kerekített kiírás: {pi:.2f}")

    # 3. feladat:
    # - szöveges (akár csv) állomány beolvasása
    # - saját osztály létrehozása
    # - saját osztály típusú lista inicializálása
    # - osztálypéldányok appen-je a listába
    # - első sor kihagyása
    # - osztálypéldányok száma (len(my_lista))
    # - megszámlálás (1 vagy több feltétel)
    # - összegzés: összeg += valami (akár feltételekhez kötve)
    # - átlagszámítás (összegzés és megszámlálás)
    # - eldöntés (ha a válasz megadható, akkor fejezzük be a keresést (break))
    # - statisztika

    épületek: list[Epulet] = []
    with open("legmagasabb.txt", "r", encoding="utf-8") as file:
        for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
            épületek.append(Epulet(sor))

    print(f"Az épületek száma: {len(épületek)}")

    # Londoni épületek száma:
    londoni_épületek_száma: int = 0
    for e in épületek:
        if e.város == "London":
            londoni_épületek_száma += 1
    print(f"A londoni épületek száma: {londoni_épületek_száma}")

    # Hány e-betű van az épületek neveiben?
    e_db: int = 0
    for e in épületek:
        e_db += e_betűk_száma(e.név)
    print(f'Az épületek neveiben az "e" betűk száma: {e_db} db')

    # Található-e 200m-nél magasabb épület az adatok között?
    van200m: bool = False
    for e in épületek:
        if e.magasság > 200:
            van200m = True
            break
    # if van200m:
    #     print("Van 200m-nél magasabb épületet.")
    # else:
    #     print("Nincs 200m-nél magasabb épületet.")
    print(f'{"Van" if van200m else "Nincs"} 200m-nél magasabb épületet.')

    # Városok szerinti épületek száma statisztika
    # Írjuk ki azokat a várokat és az épületek számát,
    # ahol több, mint 5 épület található
    print('Városokkénti épületek száma:')
    stat: dict[str, int] = dict() # szótár inicializálása!!!
    for e in épületek:
        if e.város in stat:
            stat[e.város] += 1
        else:
            stat[e.város] = 1
    
    # szótár bejárása:
    for k, v in stat.items():
        if v > 5:
            print(f'\t{k} - {v}db')





if __name__ == "__main__":
    main()
