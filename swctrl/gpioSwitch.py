
#GPIOの初期設定
import RPi.GPIO as GPIO

SW_ON = 0
SW_OFF = 1

class GpioSwitch():

    m_chageSwPin = 0
    m_exitSwPin = 0
    m_chageSwStatus = 0
    m_exitSwStatus = 0

    def __init__(self, chageSwPin, exitSwPin):
        self.m_chageSwPin = chageSwPin
        self.m_exitSwPin = exitSwPin

        # 初期化
        GPIO.setmode(GPIO.BCM)
        #入力端子設定
        GPIO.setup([self.m_chageSwPin, self.m_exitSwPin], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __del__(self):
        GPIO.cleanup()

    def update(self):
        #スイッチ状態更新
        self.m_chageSwStatus = GPIO.input(self.m_chageSwPin)
        self.m_exitSwStatus = GPIO.input(self.m_exitSwPin)

    def getChangeSwStatus(self):
        #スイッチ状態取得
        return self.m_chageSwStatus

    def getExitSwStatus(self):
        #スイッチ状態取得
        return self.m_exitSwStatus