import time 
import ait 

def check1():
    ait.move(784,277)
    time.sleep(3)
    c1,c2,c3 = ait.color()
    if (c1,c2,c3) == (233,86,35):
        return 'OK'
    else:
        return 'NotOK'
    
def check2():
    ait.move(807,806)
    time.sleep(3)
    c4,c5,c6 = ait.color()
    time.sleep(2)
    ait.click()
    time.sleep(2)
    c7,c8,c9 = ait.color()
    if (c4,c5,c6) == (c7,c8,c9):
        return 'NotOK'
    else:
        return 'OK'
    
def check3():
    ait.move(396,318)
    time.sleep(3)
    c10,c11,c12 = ait.color()
    if (c10,c11,c12) == (6,106,205):
        return 'OK'
    else:
        return 'NotOK'

ait.move(197,1052)
ait.click()
time.sleep(6)
ait.write('google')
time.sleep(3)
ait.press('Enter')
time.sleep(5)
ait.write('https://www.crazygames.com/game/smash-karts')
ait.press('Enter')
time.sleep(20)
ait.move(882,623)
ait.click()
time.sleep(10)
ait.move(1522,901)
ait.click()
time.sleep(10)
ait.move(1539,977)
check1()
check3()
check2()
