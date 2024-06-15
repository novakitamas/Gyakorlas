class Epulet:
    # elhagyható, elég csak a konstruktorban megadni az osztály adattagjait
    név: str

    def __init__(self, sor: str) -> None:
        név, város, ország, magasság, emelet, épült = sor.split(";")
        self.név: str = név
        self.város: str = város
        self.ország: str = ország
        self.magasság: float = float(magasság.replace(",", "."))
        self.emelet: int = int(emelet)
        self.épült: int = int(épült)
