import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


PIN_PORT = 18

#GPIO18を入力端子設定
GPIO.setup(PIN_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    #スイッチ状態取得
    sw_status = GPIO.input(PIN_PORT)

    #画面出力
    if sw_status == 0:
        print('スイッチON!')
    else:
        print('')

    #少し待つ
    time.sleep(0.3)     