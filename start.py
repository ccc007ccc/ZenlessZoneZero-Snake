import keyboard
import time
import threading
import pyautogui as pyg
import os

# 用于表示脚本是否应该继续运行
continue_running = False
# 极速模式
fast = False
pag_running = False
timer_thread = None
timer_lock = threading.Lock()
rounds = 0

# 去左上角 
def go_to_top_left():
    global continue_running
    keyboard.press('a')
    time.sleep(1.532)
    keyboard.release('a')
    
    keyboard.press('w')
    time.sleep(3.832)
    keyboard.release('w')
    
    continue_running = True    
# 控制蛇转圈
def rotate_snake():
    if fast: 
        keyboard.press('d')
        time.sleep(0.07)
        keyboard.release('d')
        keyboard.press('s')
        time.sleep(0.179)
        keyboard.release('s')
        keyboard.press('a')
        time.sleep(0.07)
        keyboard.release('a')
        keyboard.press('w')
        time.sleep(0.179)
        keyboard.release('w')
        if fast == False:
            time.sleep(0.261)
    else:
        keyboard.press('d')
        time.sleep(0.07)
        keyboard.release('d')
        keyboard.press('s')
        time.sleep(0.44)
        keyboard.release('s')
        keyboard.press('a')
        time.sleep(0.07)
        keyboard.release('a')
        keyboard.press('w')
        time.sleep(0.44)
        keyboard.release('w')

def start_script(e):
    global continue_running, timer_thread, fast, pag_running
    print("脚本开始运行！")
    # keyboard.press("j")
    # fast = True
    # continue_running = True
    # 启动自动重开
    pag_running = True
    threading.Thread(target=click_over_img, daemon=True).start()

    # # 启动计时线程
    # with timer_lock:
    #     if timer_thread is None or not timer_thread.is_alive():
    #         timer_thread = threading.Thread(target=timer)
    #         timer_thread.start()

def stop_script(e):
    global continue_running, pag_running
    print("脚本暂停运行！")
    # keyboard.release("j")
    continue_running = False
    pag_running = False

def timer():
    global fast
    time.sleep(10)
    keyboard.release("j")
    fast = False
    

def click_over_img():
    global rounds,continue_running
    height, width = pyg.size()
    # print(height, width)
    #左上角
    left_top_x = int(width/3)
    left_top_y = int(height/3)
    #右下角
    right_bottom_x = int(width - width/3)
    right_bottom_y = int(height - height/3)
    # print(left_top_x, left_top_y, right_bottom_x, right_bottom_y)
    
    while pag_running:
        try:
            img = pyg.locateCenterOnScreen("image.png", confidence=0.8, region=(left_top_x, left_top_y, right_bottom_x, right_bottom_y))
            if img != None:
                continue_running = False
                pyg.click(img)
                time.sleep(1.5)
                go_to_top_left()
                rounds += 1
            elif rounds == 0:
                # continue_running = True
                go_to_top_left()
                rounds = 1 
        except pyg.ImageNotFoundException:
            # print("图片未找到")
            continue
        finally:
            time.sleep(1)
                

# 当 F10 键被按下时，调用 start_script 函数
keyboard.on_press_key("f10", start_script)

# 当 F11 键被按下时，调用 stop_script 函数
keyboard.on_press_key("f11", stop_script)

def click_loop():
    # 循环点击，直到 F11 键被按下
    while True:
        if continue_running:
            rotate_snake()
        else:
            time.sleep(0.1)  # 避免空转

# 在一个新的线程中运行 click_loop 函数
threading.Thread(target=click_loop, daemon=True).start()

print("F10 键启动")
print("F11 键暂停")
print("Ctrl+C 键退出")

# 运行程序
keyboard.wait()
