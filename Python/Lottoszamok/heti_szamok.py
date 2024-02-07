class Heti_szamok:
    def __init__(self, row: str) -> None:
        splitted = row.split(' ')
        # ['37', '42', '44', '61', '62']
        # self.szam1 = int(splitted[0])
        self.szamok = []
        for szam in splitted:
            self.szamok.append(int(szam))
