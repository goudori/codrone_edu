"""
triangle()→ triangle(speed, seconds, direction)
速度: ドローンが移動する速度であるオプションのパラメーター。 0〜100の整数。デフォルト値は60です。
秒: 三角形の両側でドローンが飛ぶ秒単位の期間であるオプションのパラメーター。デフォルト値は1です。
方向: 三角形の方向を決定するオプションのパラメーター。 1は右、-1は左です。デフォルト値は1です。
"""
from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
drone.hover(1)
drone.triangle(20, 2, 1)

drone.land()
drone.close()
