import sys
import keyboard
import time
import threading

# 用于表示脚本是否应该继续运行
continue_running = False

# 预设游戏键位
up = 'w'
down = 's'
left = 'a'
right = 'd'
    
# 控制蛇转圈刷分
def rotate_snake():
    keyboard.press(right)
    time.sleep(0.11)
    keyboard.release(right)
    keyboard.press(down)
    time.sleep(0.44)
    keyboard.release(down)
    keyboard.press(left)
    time.sleep(0.11)
    keyboard.release(left)
    keyboard.press(up)
    time.sleep(0.44)
    keyboard.release(up)



def start_script(e):
    global continue_running
    print("脚本开始运行！")
    continue_running = True

def stop_script(e):
    global continue_running
    print("脚本暂停运行！")
    continue_running = False

# 当 F10 键被按下时，调用 start_script 函数
keyboard.on_press_key("f10", start_script)

# 当 F11 键被按下时，调用 stop_script 函数
keyboard.on_press_key("f11", stop_script)

def click_loop():
    # 循环点击，直到 F11 键被按下
    while True:
        if continue_running:
            rotate_snake()

# 在一个新的线程中运行 click_loop 函数
threading.Thread(target=click_loop, daemon=True).start()

# 运行程序
keyboard.wait()