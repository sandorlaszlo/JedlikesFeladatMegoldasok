from versenyzo import Versenyzo
import math

versenyzok_listaja : list[Versenyzo] = []

def main():
    beolvas('pilotak.csv')
    print(f'3. feladat: {len(versenyzok_listaja)}')
    print(f'4. feladat: {versenyzok_listaja[-1].nev}')
    print('5. feladat:')
    korabban_szuletett_mint(1901)
    print(f'6. feladat: {legkisebb_rajtszam().nemzetiseg}')
    rajtszam_statisztika()

def beolvas(fajlnev: str):
    file = open(fajlnev, 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        versenyzok_listaja.append(Versenyzo(sor.strip()))
    file.close()

def korabban_szuletett_mint(ev: int):
    for v in versenyzok_listaja:
        if v.szuletesi_ev < ev:
            print(f'\t{v.nev} ({v.szuletes})')

def legkisebb_rajtszam() -> Versenyzo:
    legkisebb_versenyzo = None
    legkisebb_rajtszam = math.inf
    for v in versenyzok_listaja:
        if v.rajtszam != '' and int(v.rajtszam) < legkisebb_rajtszam:
            legkisebb_rajtszam = int(v.rajtszam)
            legkisebb_versenyzo = v
    return legkisebb_versenyzo

def rajtszam_statisztika():
    stat = {}
    for v in versenyzok_listaja:
        if v.rajtszam in stat.keys():
            stat[v.rajtszam] += 1
        else:
            stat[v.rajtszam] = 1

    for key, value in stat.items():
        if (key != '' and value > 1):
            print(key, end=', ')
        
main()