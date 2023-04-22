import RPi.GPIO as GPIO
import time
import random

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 사용할 핀 설정
LED_PIN_1 = 17
LED_PIN_2 = 27
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

# LED 켜고 끄는 함수
def blink_LED(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)  # LED 켜기
    time.sleep(random.uniform(1, 3)) # 1~3초 대기
    GPIO.output(led_pin, GPIO.LOW)   # LED 끄기

# 키보드 입력 대기 함수
def wait_for_key_press():
    start_time = time.time()  # 현재 시간 저장
    input("LED가 꺼지면 Enter 키를 눌러주세요.")
    return time.time() - start_time  # 입력한 후 걸린 시간 계산

# 반응속도 테스트 실행 함수
def run_reaction_time_test():
    # 대기 메시지 출력
    print("반응속도 테스트를 시작합니다.")

    # 첫 번째 LED 깜빡이기
    blink_LED(LED_PIN_1)

    # 첫 번째 키보드 입력 대기
    reaction_time_1 = wait_for_key_press()

    # 대기 메시지 출력
    print("두 번째 테스트를 위해 대기합니다...")

    # 두 번째 LED 깜빡이기
    blink_LED(LED_PIN_2)

    # 두 번째 키보드 입력 대기
    reaction_time_2 = wait_for_key_press()

    # 결과 출력
    print("첫 번째 반응속도: %.3f초" % reaction_time_1)
    print("두 번째 반응속도: %.3f초" % reaction_time_2)

# 반응속도 테스트 실행
run_reaction_time_test()

# GPIO 리소스 정리
GPIO.cleanup()
