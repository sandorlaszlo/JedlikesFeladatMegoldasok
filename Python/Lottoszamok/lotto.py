from heti_szamok import Heti_szamok

osszes_szam : list[Heti_szamok] = []

def main():
    print('1. feladat: az 52. hét számai')
    szamok_52 = []
    for i in range(5):
        szamok_52.append(input(f'\t{i+1} szám: '))
    szamok_52.sort()
    print('2. feladat')
    szamok_52_str = ''
    for sz in szamok_52:
        print(f'\t{sz}', end='')
        szamok_52_str += str(sz) + ' '
    print(szamok_52_str)

    beolvas('lottosz.txt')
    print('3. feladat')
    het = int(input('\tKérem a hetet: '))
    print('4. feladat: A 5 hét nyerőszámai:')
    nyeroszamok(het)

    print('5. feladat')
    if (volt_ki_nem_huzott_szam()):
        print('Volt(ak) olyan szám(ok), ami(ke)t nem húztak ki.')
    else:
        print('Minden számot kihúztak legalább egyszer.')

    print('6. feladat')
    print(f'\t{paratlan_darab()} db páratlan számot húztak ki')

    osszes_szam.append(Heti_szamok(szamok_52_str))

    mentes('lotto52.txt')

def mentes(fajlnev):
    file = open(fajlnev, 'w', encoding='utf-8')
    for egy_het in osszes_szam:
        for szam in egy_het.szamok:
            file.write(f'{szam} ')
        file.write('\n')
    file.close()

def paratlan_darab() -> int:
    darab = 0
    for egy_het in osszes_szam:
        for szam in egy_het.szamok:
            if szam % 2 == 1:
                darab += 1
    return darab 

def nyeroszamok(het: int) -> None:
    for szam in osszes_szam[het].szamok:
        print(f'\t{szam}', end='')
    print()

def volt_ki_nem_huzott_szam() -> bool:
    kihuzott_szamok = []
    for egy_het in osszes_szam:
        for szam in egy_het.szamok:
            if szam not in kihuzott_szamok:
                kihuzott_szamok.append(szam)
    return len(kihuzott_szamok) < 90

def beolvas(fajlnev: str) -> None:
    file = open(fajlnev, 'r', encoding='utf-8')
    for sor in file:
        osszes_szam.append(Heti_szamok(sor.strip()))
    file.close()

main()