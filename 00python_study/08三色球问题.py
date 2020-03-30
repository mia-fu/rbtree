# encoding:utf-8

red = 3
yellow = 3
green = 6

for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print (str(red) + ' ' + str(yellow) + ' ' + str(green))

