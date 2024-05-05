"""
input　→ユーザーが、入力した結果を表示させる

input("")　→結果は、strの値

int(input(""))　→結果は、intの値

note　→音符(音)を発生させる

noteの種類
C: ド
D: レ
E: ミ
F: ファ
G: ソ
A: ラ
B: シ

 drone.drone_buzzer(音符の種類, 再生秒数)
"""
from codrone_edu.drone import *

import time

drone = Drone()

drone.pair()





"""
ドレミファソラシドと音を鳴らす
"""
notes = [Note.C3, Note.D3, Note.E3, Note.F3, Note.G3, Note.A3, Note.B3, Note.C4]

duration = [500, 500, 500, 500, 500, 500, 500, 500]

for i in range(len(notes)):
    drone.drone_buzzer(notes[i], duration[i])

time.sleep(0.5)

# 逆順に音を鳴らす
notes_reversed = notes[::-1]

for i in range(len(notes_reversed)):
    drone.drone_buzzer(notes_reversed[i], duration[i])

time.sleep(0.1)

drone.close()
