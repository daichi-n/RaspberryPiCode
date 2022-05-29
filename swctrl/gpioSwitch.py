
#GPIOの初期設定
import RPi.GPIO as GPIO

class GpioSwitch():

    m_inputPin = 0

    def __init__(self, inputPin):
        # 初期化
        m_inputPin = inputPin
        GPIO.setmode(GPIO.BCM)
        #入力端子設定
        GPIO.setup(self.m_inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update(self):
        #スイッチ状態更新
        self.m_inputPin = GPIO.input(self.m_inputPin)

    def getPinStatus(self):
        #スイッチ状態取得
        return self.m_inputPin