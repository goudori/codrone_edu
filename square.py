# これは「Co Drone EDU」のサンプルファイルです。
# Co Drone EDU
"""
正方形移動
"""
from codrone_edu.drone import *
import time

# ドローンオブジェクトを作成
drone = Drone()

# ペアリング
drone.pair()

# トリム値の確認
print(drone.get_trim())

"""
ドローンが、右にドリフトを防ぐため、左にトリム調整
(drone.set_trimの時は、必ずtime.sleepとtake offを必ず設定する。)
"""
# drone.set_trim(-5, 0)

#time.sleep(1)

# 離陸
drone.takeoff()

# hoverする
drone.hover(3)

# ピッチ３０度
drone.set_pitch(30)

# ドローンを動かす
drone.move(1.5)

# 　ピッチを０度にする(※0度にしないと斜めに移動する)
drone.set_pitch(0)

# ロール３０度
drone.set_roll(30)

# ドローンを動かす
drone.move(1.5)

# ロール０度
drone.set_roll(0)

# 後ろ移動
drone.set_pitch(-30)

# ドローンを動かす
drone.move(1)

# 　ピッチを０度にする(※0度にしないと斜めに移動する)
drone.set_pitch(0)

# 　左移動
drone.set_roll(-30)

# ドローンを動かす
drone.move(1.5)

# 着陸
drone.land()

# 緊急着陸
# drone.emergency_stop()

# 接続を閉じる
drone.close()

"""
逆正方形移動
"""
# ドローンオブジェクトの作成
#drone = Drone()

# ペアリング
#drone.pair()

# 離陸
#drone.takeoff()

# ホバリング
#drone.hover(3)

# 後進
#drone.set_pitch(-30)

# 移動
#drone.move(1)

# ピッチ0度
#drone.set_pitch(0)

#　右
#drone.set_roll(30)

# 移動
#drone.move(2)

# ロール０度
#drone.set_roll(0)

# 前進
#drone.set_pitch(30)

# 移動
#drone.move(2)

# ピッチ０度
#drone.set_pitch(0)

# 左
#drone.set_roll(-35)

# 移動
#drone.move(1)

# ロール０度
#drone.set_roll(0)

# 着陸
#drone.land()

# 閉じる
#drone.close()

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。


# def print_hi(name):
# スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
# print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


# ガター内の緑色のボタンを押すとスクリプトを実行します。
# if __name__ == '__main__':
# print_hi('PyCharm')
