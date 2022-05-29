
#GPIOの初期設定
import RPi.GPIO as GPIO

SW_ON = 0
SW_OFF = 1
GPIO.setmode(GPIO.BCM)

class GpioSwitch():

    m_inputPin = 0

    def __init__(self, chageSwPin, exitSwPin):
        # 初期化
        m_chageSwPin = chageSwPin
        m_exitSwPin = exitSwPin
        #入力端子設定
        GPIO.setup([self.m_inputPin, self.m_exitSwPin], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __del__(self):
        GPIO.cleanup()

    def update(self):
        #スイッチ状態更新
        self.m_inputPin = GPIO.input(self.m_inputPin)

    def getChangeSwStatus(self):
        #スイッチ状態取得
        return self.m_inputPin

    def getChangeSwStatus(self):
        #スイッチ状態取得
        return self.m_inputPin