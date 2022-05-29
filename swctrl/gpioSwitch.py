import RPi.GPIO as GPIO

# PIN配
CHANGE_BUTTON_PIN = 26
EXIT_BUTTON_PIN = 4
# 入力値判定
SW_ON = 0
SW_OFF = 1

class GpioSwitch():

    m_chageSwPin = CHANGE_BUTTON_PIN
    m_chageSwStatus = EXIT_BUTTON_PIN

    m_exitSwPin = 0
    m_exitSwStatus = 0

    def __init__(self):
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