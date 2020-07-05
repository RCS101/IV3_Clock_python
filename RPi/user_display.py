from IV3 import IV3, numberWang
from time import sleep

ivClock = IV3()
numbs = numberWang()

cnt = 0

while True:
    sleep(0.01)
    ivClock.user_display(numbs.Wanger(cnt))
    cnt += 1
    if cnt == 10000:
        cnt = 0
