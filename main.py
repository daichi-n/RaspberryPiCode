from swctrl import gpioSwitch
import time
import sys

# ボタン
INPUT_PIN_PORT = 26

def main():

    changeSw = gpioSwitch.GpioSwitch(INPUT_PIN_PORT)

    while True:

        changeSw.update()

        print("PinStatus : " + str(changeSw.getPinStatus()))

        #少し待つ
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except:
       print(sys.exc_info())