class CBAdas:
    def __init__(self, ido, nev, adas):
        self.ido = ido
        self.nev = nev
        self.adas = adas
        


    def beolvasas(file_nev):
        with open(file_nev, 'r', encoding='utf-8') as file:
            fejlec = file.readline().strip()
            adatok = []
            for sor in file:
                sor_adatok = sor.strip().split(',')
                adatok.append(CBAdas(sor_adatok[0], sor_adatok[1], sor_adatok[2]))
        return adatok

    cb_adatok = beolvasas('cb.txt')
