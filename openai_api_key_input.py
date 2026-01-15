# ============================================
# 📌 openai_api_key_input.py
# 목적: OpenAI API 키를 직접 입력받아 클라이언트 초기화 및 연결 테스트
# - getpass 모듈을 사용해 API 키를 안전하게 입력
# - OpenAI 클라이언트 초기화 후 간단한 대화 요청으로 연결 확인
# - 모델 설정 및 기본 프롬프트 실행 예제 포함
# - 실제 프로젝트에서는 보안에 주의하여 사용
# ============================================
# 방법 2: 직접 입력
# 보안에 주의! 실제 프로젝트에서는 사용에 주의하세요.

import getpass
api_key = getpass.getpass("OpenAI API 키를 입력하세요: ")
print("API 키가 입력되었습니다.")

# OpenAI 클라이언트 초기화
from openai import OpenAI

client = OpenAI(api_key=api_key)

# API 연결 테스트
try:
    test_response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": "안녕하세요! 거기 누구 있나요?"}],
        max_tokens=20
    )
    print("OpenAI API 연결 성공!")
    print(f"테스트 응답: {test_response.choices[0].message.content}")
except Exception as e:
    print(f"API 연결 실패: {e}")

model = "gpt-4.1-mini"  # 모델 설정

response = client.chat.completions.create(
        model=model,
        messages=[{"role":"user", "content":"너는 누구니?"}])   # 프롬프트

print(response)

