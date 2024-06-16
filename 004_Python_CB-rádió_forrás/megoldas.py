from sofor import sofor

class megoldas:
    _soforok: list[sofor]
    
    @property
    def bejegyzesek_szama(parameter_list) ->int:
        return len(self._soforok)
    
    def __init__(self, allomany: str):
        self._soforok = []
        with open("cb.txt", "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._soforok.append(sofor(sor))