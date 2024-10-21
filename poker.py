import random
''' a[0][0] -> TYPE
    a[0][1] -> ZAHL
    '''
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

            royal == True
            if a[i][1] == 1 or a[i][1] >= 10 and royal == True:
                royal = True
            else: royal = False
        else:
            royal = False

    return royal
def checkFlush(a):

    b = a[0][0]

    i = 0
    if a[i][0] == b and a[i+1][0] == b and a[i+2][0] == b and a[i+3][0] == b and  a[i+4][0] == b:
        flush = True
    else:
        flush = False

    return flush


def checkEvents():
    royalFlushes = 0
    flushes = 0

    for i in range(anzahl):
        a = draw()

        if checkRoyalFlush(a) == True:
            royalFlushes += 1
            
        if checkFlush(a) == True:
            flushes += 1

    print(flushes/anzahl * 100, "% der Hände hatten einen Flush")
    print(royalFlushes/anzahl*100 , "% der Hände hatten einen Royal Flush!")

def main():

        checkEvents()



if __name__ == '__main__':
    main()

