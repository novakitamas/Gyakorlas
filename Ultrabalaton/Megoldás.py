from Eredmény import Eredmény


class Megoldás(object):
    _eredmények: list[Eredmény] = []

    @property
    def versenyzők_száma(self) -> int:
        return len(self._eredmények)

    @property
    def nők_célban(self) -> int:
        nők100: int = 0
        for e in self._eredmények:
            if e.kategória == "Noi" and e.táv_százalék == 100:
                nők100 += 1
        return nők100

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:
                self._eredmények.append(Eredmény(sor))

    def indult_egyéniben(self, név: str) -> str:
        válasz: str = "Nem"
        vissza: str = ""
        for e in self._eredmények:
            if e.név == név:
                válasz = "Igen"
                break
        vissza = "\tIndult egyéniben a sportoló? " + válasz
        if válasz == "Igen":
            vissza += f"\n\tTeljesítette a teljes távot? {"???"}"
        return vissza
