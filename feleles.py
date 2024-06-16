import random  

def main() -> None:

    diakok: list = ["Bence", "Tamás", "Benedek", "Gyula", "Ábel"]
    felelokszama = int(input("Adja meg hány diák felel ma: "))

    if felelokszama > len(diakok):
        print("Nincs ennyi diák az osztályban")
    else:

        if felelokszama == 1:

            felelo = random.choice(diakok)
            print(f"A mai felelő: {felelo}")

        else:

            felelok = random.sample(diakok, felelokszama)
            felelok_str = ", ".join(felelok)
            print(f"A mai felelők: {felelok_str}")

if __name__ == "__main__":
    main()
