import time
from playsound import playsound

def pomodoro_timer():
    print("开始专注时间25分钟！")
    for i in range(5, 0, -1):
        time.sleep(60)
        if i == 1:
            playsound('path/to/alarm/sound.wav') # 播放警报音效
            print("休息时间到！")
        else:
            print(f"{i-1}分钟后进入休息时间")
    
    print("开始休息时间5分钟！")
    for i in range(5, 0, -1):
        time.sleep(60)
        if i == 1:
            playsound('path/to/alarm/sound.wav') # 播放警报音效
            print("专注时间到！")
        else:
            print(f"{i-1}分钟后重新开始专注时间")
            
while True:
    pomodoro_timer()
    user_input = input("你想重新开始专注时间吗？（输入 Y 开始专注，其他任意键退出程序）：")
    if user_input.lower() == 'y':
        continue
    else:
        break
