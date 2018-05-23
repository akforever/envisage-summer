import random
avengers = ["cap america", "dr strange", "thor", "hulk", "iron man", "starlord", "spiderman", "black panther", "scarlet witch" ]
ThanosPower = 95


def game(k):
    if k == 0:
        return 92
    elif k == 1:
        return 96
    elif k == 2:
        return 99
    elif k == 3:
        return 98
    elif k == 4:
        return 97
    elif k == 5:
        return 91
    elif k == 6:
        return 92
    elif k == 7:
        return 92
    elif k == 8:
        return 95


trig = 'y'
while trig == ( 'y' ) :
    print('START THE GAME')
    avgpow = 0
    sumpow = 0
    a = []
    for x in range(2):
         a.append(random.randint(1, 8))
    i=a[0]
    j=a[1]
    print('Select your two heroes')
    print('select\t0-CAPTAIN AMERICA\n 1-DOCTOR STRANGE\n 2-THOR\n 3-HULK\n 4-IRON MAN\n 5-PETER QUILL\n 6-SPIDERMAN\n 7-BLACK PANTHER\n 8-SCARLET WITCH')
    m = int(input('Enter your first choice: '))
    n = int(input('enter your second choice: '))
    sumpow = sumpow + game(i) + game(j) + game(m) + game(n)
    avgpow = sumpow / 4.0
    print('your superheroes are')
    print(avengers[i])
    print(avengers[j])
    print(avengers[m])
    print(avengers[n])
    if (avgpow > 95):
        print('AVENGERS WON')
    else:
        print('THANOS WON')
    s = input('Do you wanna try again?Y/N:')
    trig = s.lower()

    if trig == 'n':
        exit
