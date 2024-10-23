import random
''' a[0][0] -> TYPE
    a[0][1] -> ZAHL
    '''
anzahl = 1000000

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


def draw():

    z = []
    while len(z) < 5:
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

        if [x,a[x][j]] not in z:

            z.append([x, a[x][j]])
    return z


def checkRoyalFlush(a):

    b = a[0][0]
    royal = True
    ''' a[0-4 also die 5 karten][0 für type 1 für zahl] '''

    for i in range(5):
        if a[i][0] == b and royal == True:
            if a[i][1] == 1 or a[i][1] >= 10 and royal == True:
                royal = True
            else: royal = False
        else:
            royal = False

    return royal


def checkStraight(a):

    straight = True
    c = sorted(card[1] for card in a)
    for i in range(4):
        if c[i + 1] != c[i] + 1:
            straight = False

    return straight
def checkFlush(a):

    b = a[0][0]

    i = 0
    if a[i][0] == b and a[i+1][0] == b and a[i+2][0] == b and a[i+3][0] == b and  a[i+4][0] == b:
        flush = True
    else:
        flush = False

    return flush

def checkPairs(a):
    anz = 0
    for i in range(5):
        for j in range(5):
            if i != j:
                if a[i][1] == a[j][1]:
                    anz += 1
    return anz

def checkThree(a):
    c = sorted(card[1] for card in a)
    if (c[0] == c[1] and c[1] == c[2]) or (c[1] == c[2] and c[2] == c[3]) or (c[2] == c[3] and c[3] == c[4]):
            return True
    return False

def checkFour(a):
    c = sorted(card[1] for card in a)
    if c[0] == c[3] or c[1] == c[4]:
        return True
    return False

def checkFull(a):
    c = sorted(card[1] for card in a)
    if checkThree(a) == True:
        if c[0] == c[1] and c[3] == c[4]:
            return True
    return False
def checkEvents():
    royalFlushes = 0
    straightFlushes = 0
    straight= 0
    flushes = 0
    four = 0
    three = 0
    twoPair = 0
    pair = 0
    fullHouse = 0

    for i in range(anzahl):
        a = draw()


        if checkRoyalFlush(a) == True:
            royalFlushes += 1

        elif checkStraight(a) == True and checkFlush(a) == True:
            straightFlushes += 1

        elif checkFour(a) == True:
            four += 1

        elif checkFull(a) == True:
            fullHouse += 1

        elif checkStraight(a) == True:
            straight += 1

        elif checkFlush(a) == True :
            flushes += 1
        elif checkThree(a) == True:
            three += 1
        elif checkPairs(a) == 4:
            twoPair += 1
        elif checkPairs(a) == 2:
            pair += 1

    print(round(royalFlushes/anzahl * 100, 4), "% der Hände hatten einen Royal Flush!")
    print(round(straightFlushes / anzahl * 100, 4), "% der Hände hatten einen Straight Flush")
    print(round(four / anzahl * 100, 4), "% der Hände hatten einen Vierling")
    print(round(fullHouse / anzahl * 100, 4), "% der Hände hatten ein Full House")
    print(round(flushes / anzahl * 100, 4), "% der Hände hatten einen Flush")
    print(round(straight / anzahl * 100, 4), "% der Hände hatten einen Straight")
    print(round(three/ anzahl * 100, 4), "% der Hände hatten einen Drilling")
    print(round(twoPair / anzahl * 100, 4), "% der Hände hatten ein TwoPair")
    print(round(pair / anzahl * 100, 4), "% der Hände hatten ein Pair")

def main():
    checkEvents()


if __name__ == '__main__':
    main()

