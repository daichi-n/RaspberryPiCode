from swctrl import gpioSwitch
from stepperMoter import stepperMoter
from length_monitor import length
import time
import sys

def main():

    sw = gpioSwitch.GpioSwitch()
    StepMoter = stepperMoter.C28BYJ48(IN1=5, IN2=6, IN3=13, IN4=19)

    flag = False

    while True:

        sw.update()

        sw_status = sw.getChangeSwStatus()

        print("PinStatus : " + str(sw_status))

        if sw.getExitSwStatus() == gpioSwitch.SW_ON :
            print("Exit Application.")
            return

        if sw_status == gpioSwitch.SW_ON :
            if flag :
                StepMoter.Step_CW(4096,0.001)
                flag = False
            else :
                StepMoter.Step_CCW(4096,0.001)
                flag = True

        distance = length.mesure()
        print ( "Discance : {:.1f} cm".format( distance ) )

        #少し待つ
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f"Unexpected {ex}, {type(ex)}")
    except:
        print("Exception Occured!!")
        print(sys.exc_info())