import random

anzahl = 100000

def karten():
    anz = 52

    herz = []
    karo = []
    kreuz = []
    pik = []
    spiel = {'herz' :herz, 'karo':karo,'kreuz':kreuz,'pik':pik}

    for i in range(1, anz + 1):
        if i <= 13:
            herz.append(i)
        elif 14 <= i <= 26:
            karo.append(i - 13)
        elif 27 <= i <= 39:
            kreuz.append(i - 26)
        elif 40 <= i <= 52:
            pik.append(i - 39)

    return spiel

def draw ():
    z = []
    for i in range (5):
        a = karten()
        i = random.randint(1,4)
        j = random.randint(0,12)

        x = ''
        if i == 1:
            x = 'herz'
        elif i == 2:
            x = 'karo'
        elif i == 3:
            x = 'kreuz'
        elif i == 4:
            x ='pik'
        z.append([x, a[x][j]])
    return z

def checkFlush(a):

    b = a[0][0]
    flush = False
    i = 0
    if a[i][0] == b and a[i+1][0] == b and a[i+2][0] == b and a[i+3][0] == b and  a[i+4][0] == b:
        flush = True
    else:
        flush = False

    return flush




if __name__ == '__main__':
    for i in range(100000):
        a = draw()
        if checkFlush(a) == True:
            print(a)
            print(checkFlush(a))

