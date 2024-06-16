import random  

def main() -> None:

    diakok: list = ["Bence", "Tamás", "Benedek", "Gyula", "Ábel"]
    felelokszama = int(input("Adja meg hány diák felel ma: "))

    if felelokszama > len(diakok): #tul sok felelő meghatározása
        print("Nincs ennyi diák az osztályban")
    else:

        if felelokszama == 1:

            felelo = random.choice(diakok) #egy diák kiválasztása
            print(f"A mai felelő: {felelo}")

        else:

            felelok = random.sample(diakok, felelokszama) #több diák kiválasztása
            felelok_str = ", ".join(felelok) 
            print(f"A mai felelők: {felelok_str}")

if __name__ == "__main__":
    main()
