import threading
import time

def burn_cpu():
    a = 0
    while True:
        a += 1
        pass  # 계속 무한 루프

# CPU 코어 수만큼 스레드 생성
num_threads = 32  # 필요에 따라 조절하세요

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=burn_cpu)
    t.start()
    threads.append(t)

# 일정 시간 동안 실행 (예: 10초)
time.sleep(3600)

# 스크립트는 수동으로 종료해야 함
