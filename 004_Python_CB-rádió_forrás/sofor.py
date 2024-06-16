
class sofor:
    def __init__(self, sor: str) -> None:
        ora, perc, adasok, nev = sor.split(";")
        self.ora: int = int(ora)
        self.pec: int = int(perc)
        self.adasok: int = int(adasok)
        self.nev: str = str(nev)