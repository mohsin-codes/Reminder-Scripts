import time
from plyer import notification

if __name__=='__main__':
    while True :
        notification.notify(
            title = "Take a Break!",
            message = " You've been working hard. Give yourself a break and take a walk.",
            app_icon="E:\Projects\Python\Reminder Scripts\Take a Break Script\icon.ico",
            timeout = 5
        )
        time.sleep(20*60)
