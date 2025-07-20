import asyncio
import os
import threading
import time

from google import genai
from google.genai.types import (
        Content,
        LiveConnectConfig,
        Modality,
        Part,
    )

# --- 설정 ---
# 요청에 명시된 프로젝트 및 위치 정보
GOOGLE_CLOUD_PROJECT = ""
GOOGLE_CLOUD_LOCATION = "us-central1"

# 사용할 모델 이름
MODEL_ID = "gemini-live-2.5-flash-preview-native-audio"

# 생성할 스레드(세션)의 수
NUM_THREADS = 5000

# 각 스레드 생성 사이의 대기 시간 (초)
THREAD_CREATION_DELAY = 1

# 세션 연결 후 대기 시간 (초) - 10분
SESSION_WAIT_TIME = 600

# --- SDK 설정 ---
# 환경 변수 설정
os.environ["GOOGLE_CLOUD_PROJECT"] = GOOGLE_CLOUD_PROJECT
os.environ["GOOGLE_CLOUD_LOCATION"] = GOOGLE_CLOUD_LOCATION

client = genai.Client(
        vertexai=True,
        project=GOOGLE_CLOUD_PROJECT,
        location=GOOGLE_CLOUD_LOCATION
    )

def create_session_task(thread_id: int):
    """
    Gemini Live API 세션을 비동기적으로 생성하고 연결을 유지하는 함수
    """
    #print(f"[Thread {thread_id:04d}] 세션 생성을 시작합니다.")
    try:
        async def connect_and_wait():
            """비동기 세션 연결 및 대기 작업을 수행하는 코루틴"""
            try:
                start_time = time.time()  # 세션 연결 시작 시간 측정
                # 지정된 모델로 Live 세션에 연결
                session = client.aio.live.connect(model=MODEL_ID,config=LiveConnectConfig(response_modalities=[Modality.AUDIO]),)
                end_time = time.time()  # 세션 연결 종료 시간 측정
                elapsed_time_ms = (end_time - start_time) * 1000  # 밀리초 단위로 계산
                print(f"✅ [Thread {thread_id:04d}] 세션 연결 성공! (소요 시간: {elapsed_time_ms:.2f} ms)")
                
                # 요청에 따라 10분간 대기하여 세션 유지
                await asyncio.sleep(SESSION_WAIT_TIME) 
                
                print(f"⌛ [Thread {thread_id:04d}] 10분 대기 완료. 세션을 종료합니다.")
                
            except Exception as e:
                print(f"❌ [Thread {thread_id:04d}] 비동기 작업 중 오류 발생: {e}")

        # 현재 스레드에서 비동기 함수 실행
        asyncio.run(connect_and_wait())

    except Exception as e:
        print(f"❌ [Thread {thread_id:04d}] 스레드 실행 중 오류 발생: {e}")


def main():
    """
    세션 생성을 위한 스레드를 관리하고 실행하는 메인 함수
    """
    threads = []
    print(f"총 {NUM_THREADS}개의 세션 생성 테스트를 시작합니다.")
    print("-" * 40)
    
    batch_size = 10

    for i in range(0, NUM_THREADS, batch_size):
        threads_batch = []
        for j in range(i, min(i + batch_size, NUM_THREADS)):
            # 각 작업을 수행할 스레드 생성
            thread = threading.Thread(target=create_session_task, args=(j,))
            threads_batch.append(thread)
            threads.append(thread)
            thread.start()
            #print(f"🚀 [Main] Thread {j:04d} 시작됨.")
            
        # 다음 스레드 생성 전 1초 대기
        time.sleep(THREAD_CREATION_DELAY)

    print("\n" + "-" * 40)
    print(f"✅ [Main] {len(threads)}개의 모든 스레드 생성을 완료했습니다.")
    print(f"각 스레드는 이제 독립적으로 세션을 10분간 유지합니다.")
    
    # 모든 스레드가 작업을 마칠 때까지 대기
    for thread in threads:
        thread.join()

    print("\n" + "-" * 40)
    print("✅ [Main] 모든 스레드의 작업이 완료되었습니다. 테스트를 종료합니다.")


if __name__ == "__main__":
    main()