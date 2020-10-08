import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!",
            message = 'It has been two hours since you have drank water. Please Drink Water and take care of yourself❤.',
            app_icon ="E:\Projects\Python\Reminder Scripts\Reminder-Scripts\Water Reminder\Icon.ico.ico",
            timeout=10
        )
        time.sleep(2*(60*60))
