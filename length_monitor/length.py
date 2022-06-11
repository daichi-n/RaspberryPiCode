import time, pigpio

TEMP = 20

TRIG_PIN = 23
ECHO_PIN = 24

s_speed = 331.5 + 0.6 * TEMP

pi = pigpio.pi()

pi.set_mode( TRIG_PIN, pigpio.INPUT )
pi.set_mode( ECHO_PIN, pigpio.INPUT )
pi.set_pull_up_down( ECHO_PIN, pigpio.PUD_OFF )

pi.write( TRIG_PIN, pigpio.LOW )
time.sleep( 1 )

def mesure():
    pi.write( TRIG_PIN, pigpio.HIGH )
    time.sleep(0.00001)
    pi.write( TRIG_PIN, pigpio.LOW )

    while ( pi.read( ECHO_PIN ) == pigpio.LOW ):
        sigoff = time.time()
    while ( pi.read( ECHO_PIN ) == pigpio.HIGH ):
        sigon = time.time()
    
    dist = ( sigon - sigoff ) * s_speed / 2 * 100
    return dist

def main():
    while True:
        distance = mesure()
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