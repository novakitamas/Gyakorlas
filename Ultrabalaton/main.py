from Megoldás import Megoldás


def main() -> None:
    mo: Megoldás = Megoldás("ub2017egyeni.txt")

    print(f"3. feladat: Egyéni indulók: {mo.versenyzők_száma} fő")

    print(f"4. feladat: Célba érkező női sportolók: {mo.nők_célban} fő")

    név: str = input("5. feladat: Kérem a sportoló nevét: ")

    print(f"{mo.indult_egyéniben(név)}")


if __name__ == "__main__":
    main()
