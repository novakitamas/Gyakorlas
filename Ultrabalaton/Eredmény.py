class Eredmény(object):
    # Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
    # Acsadi Lajos;1;Ferfi;30:28:42;100
    _név: str
    _rajtszám: int
    _kategória: str
    _idő: str
    _táv_százalék: int

    @property
    def név(self) -> str:
        return self._név

    @property
    def kategória(self) -> str:
        return self._kategória

    @property
    def táv_százalék(self) -> int:
        return self._táv_százalék

    def __init__(self, sor: str) -> None:
        név, rajtszám, kategória, idő, táv_százalék = sor.split(";")
        # m: list[str] = sor.split(";")
        # self._név = m[0]
        # ...
        self._név = név
        self._rajtszám = int(rajtszám)
        self._kategória = kategória
        self._idő = idő
        self._táv_százalék = int(táv_százalék)