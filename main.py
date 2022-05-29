from swctrl import gpioSwitch
import time
import sys

def main():

    sw = gpioSwitch.GpioSwitch()

    while True:

        sw.update()

        print("PinStatus : " + str(sw.getChangeSwStatus()))

        if sw.getExitSwStatus() == gpioSwitch.SW_ON:
            print("Exit Application.")
            return

        #少し待つ
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except:
        print("Exception Occured!!")
        print(sys.exc_info())