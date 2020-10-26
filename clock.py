"""
Digital clock
Coded by Kuba Siekierzynski (c) 2018

Please rotate your device (landscape view)

UPDATE 1: styles added
UPDATE 2: random styles
"""

import sys, codecs
sys.stdout = codecs.getwriter('utf_16')(sys.stdout.buffer, 'strict')

from datetime import datetime as dt
from random import sample as s

# the number of style samples should be < 6
# to avoid "Time limit exceeded"
samples = 5

# styles below 👇 you may add your own
px = (
(chr(11035), chr(11036)), # classic
(chr(11036), chr(11035)), # classic negative
(chr(11035), chr(8419)),  # classic blue
(chr(8419), chr(11035)),  # classic blue neg
(chr(11036), chr(8419)),  # modern
(chr(8419), chr(11036)),  # modern negative
(chr(9898), chr(128308)), # red-on-white
(chr(128308), chr(9898)), # white-on-red
(chr(9898), chr(9899)),   # black-on-white
(chr(9899), chr(9898)),   # white-on-black
(chr(128308), chr(9899)), # black-on-red
(chr(9899), chr(128308)), # red-on-black
)

digits = [

[ # zero
[0,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]],

[ # one
[0,0,1,0,0],
[0,1,1,0,0],
[1,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[1,1,1,1,1]],

[ # two
[0,1,1,1,0],
[1,0,0,0,1],
[0,0,0,0,1],
[0,0,0,1,0],
[0,0,1,0,0],
[0,1,0,0,0],
[1,1,1,1,1]],

[ # three
[0,1,1,1,0],
[1,0,0,0,1],
[0,0,0,0,1],
[0,0,1,1,0],
[0,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]],

[ # four
[0,0,0,1,0],
[0,0,1,1,0],
[0,1,0,1,0],
[1,0,0,1,0],
[1,1,1,1,1],
[0,0,0,1,0],
[0,0,0,1,0]],

[ # five
[1,1,1,1,1],
[1,0,0,0,0],
[1,0,0,0,0],
[1,1,1,1,0],
[0,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]],

[ # six
[0,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,0],
[1,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]],

[ # seven
[1,1,1,1,1],
[1,0,0,0,1],
[0,0,0,1,0],
[0,0,1,0,0],
[0,1,0,0,0],
[0,1,0,0,0],
[0,1,0,0,0]],

[ # eight
[0,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]],

[ # nine
[0,1,1,1,0],
[1,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,1],
[0,0,0,0,1],
[1,0,0,0,1],
[0,1,1,1,0]]]

# clock preparation
clock = list([0 for i in range(32)] for j in range(9))

# colon is fixed
clock[2][15] = 1
clock[2][16] = 1
clock[3][15] = 1
clock[3][16] = 1
clock[5][15] = 1
clock[5][16] = 1
clock[6][15] = 1
clock[6][16] = 1

now = dt.now() # GMT time
hr, mn = now.hour, now.minute

# the real hour in HH:MM format
h = ('0' + str(hr))[-2:] + ('0' + str(mn))[-2:]

# put the digits on the clock display
for i in range(len(h)):
    d = int(h[i])
    for j in range(len(digits[d])):
        for k in range(len(digits[d][0])):
            clock[j+1][1+(i//2*4)+k+i*7] = digits[d][j][k]

print(f'Timezone: Zulu\nTurn to landscape mode if illegible.\n')

# remember to tilt the device to landscape
for style in s(range(len(px)), samples):
    for line in clock:
        for pixel in line:
            print(px[style][pixel], end='')
        print()
    print()
