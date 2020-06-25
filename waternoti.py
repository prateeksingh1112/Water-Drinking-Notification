import time
from plyer import notification

if __name__ == "__main__":
    # while True:
        notification.notify(
            title="Please Drink Water!!",
            message="Piyo bhai shanti se",
            # app_icon= "D:\icon.ico",
            timeout=6
    )
    # time.sleep(10)