import pyautogui
import time

time.sleep(5)
# 获取鼠标当前位置
current_mouse_x, current_mouse_y = pyautogui.position()

# 打印鼠标当前位置
print("Mouse position - x:", current_mouse_x, "y:", current_mouse_y)
