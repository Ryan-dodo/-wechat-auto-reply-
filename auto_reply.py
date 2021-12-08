#! python3
# Help you to reply wechat message!

import time,pyautogui
import datetime



def find_new_message(flag):
    try:
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\new_message.PNG')
        x,y=pyautogui.center(new_message_position)
        print('有新消息了，即将自动回复')
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        flag=True
        return flag
    except:
        print('没有新消息')
def auto_type(reply_words):
    new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\reply.PNG')
    x,y=pyautogui.center(new_message_position)
    pyautogui.click(x=x,y=y,clicks=1,button='left')
    time.sleep(0.5)
    pyautogui.typewrite(reply_words+' Time:')
    pyautogui.typewrite(str(datetime.datetime.now())[0:19])
    
def send():
    try:
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\send.PNG')
        x,y=pyautogui.center(new_message_position)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        print('已发送')
    except:
        pass

def rest():
    try:
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\rest.PNG')
        x,y=pyautogui.center(new_message_position)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
    except:
        pass
    try:
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\submi.PNG')
        x,y=pyautogui.center(new_message_position)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
    except:
        pass

def emoji():
    try:
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\emoji.PNG')
        x,y=pyautogui.center(new_message_position)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        print('发送表情')
        time.sleep(0.5)
        new_message_position=pyautogui.locateOnScreen(r'D:\Ryan\OneDrive - csu.edu.cn\snake\study\no_2\auto_reply\image\reply_emoji.PNG')
        x,y=pyautogui.center(new_message_position)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        print('完成！')
    except:
        pass

def Dont_sleep():
    pyautogui.moveRel(1,0)
    time.sleep(0.1)
    pyautogui.moveRel(-1,0)
                
def main():
    
    # find new message
    print('微信自动回复已启动')
    reply_words='Sorry , I am busy! (by python robot)'
    #  !!!! English only  !!!
    flag=False
    while True:
        flag=find_new_message(flag)
        time.sleep(0.5)
        Dont_sleep()
        time.sleep(0.5)
        while flag:
            auto_type(reply_words)
            time.sleep(0.1)
            send()
            time.sleep(0.5)
            emoji()
            rest()
            flag=False




if __name__ == '__main__':
    main()
    
