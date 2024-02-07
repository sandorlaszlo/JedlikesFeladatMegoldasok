class Versenyzo:
    def __init__(self, sor:str) -> None:
        splitted = sor.strip().split(';')
        self.nev = splitted[0]
        self.szuletes = splitted[1]
        self.nemzetiseg = splitted[2]
        self.rajtszam = splitted[3]
        ev, honap, nap = self.szuletes.split('.')
        self.szuletesi_ev = int(ev)