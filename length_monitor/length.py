import time
import RPi.GPIO as GPIO

TEMP = 20

TRIG_PIN = 23
ECHO_PIN = 24

s_speed = 331.5 + 0.6 * TEMP

class LengthMonitor():
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup( TRIG_PIN, GPIO.OUT)
        GPIO.setup( ECHO_PIN, GPIO.IN)
        
        time.sleep( 1 )

    def __del__(self):
        GPIO.cleanup()

    def mesure(self):
        GPIO.output(TRIG_PIN,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN,GPIO.LOW)

        while ( GPIO.input( ECHO_PIN ) == GPIO.LOW ):
            sigoff = time.time()
        while ( GPIO.input( ECHO_PIN ) == GPIO.HIGH ):
            sigon = time.time()
        
        dist = ( sigon - sigoff ) * s_speed / 2 * 100
        return dist
        
def main():
    monitor = LengthMonitor() 
    while True:
        distance = monitor.mesure()
        print ( "Discance : {:.1f} cm".format( distance ) )
        time.sleep( 1 )

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f"Unexpected {ex}, {type(ex)}")
    except:
        print("Exception Occured!!")
        print(sys.exc_info())