# ============================================
# 📌 generate_with_params.py
# 목적: LLM 텍스트 생성 시 기본 프롬프트와 파라미터를 설정하는 함수 예제
# - 기본 프롬프트: "로봇, 꽃, 비밀" 단어로 짧은 이야기 생성
# - 기본 파라미터: temperature=0, max_tokens=150
# - generate_with_params 함수: 전달된 파라미터로 기본 설정을 업데이트 후 응답 생성
# - 교육/데모용 예시 코드
# ============================================
import time

# 파라미터 효과를 비교하기 위한 기본 프롬프트
default_prompt = "다음 단어들로 창의적인 짧은 이야기를 만들어주세요: 로봇, 꽃, 비밀"

# 기본 파라미터 설정 함수
def generate_with_params(**params):
    """파라미터를 받아서 텍스트를 생성하는 함수"""
    default_params = {
        'model': model,
        'messages': [{"role": "user", "content": default_prompt}],
        'temperature': 0,
        'max_tokens': 150
    }

    # 파라미터 업데이트
    default_params.update(params)

    response = client.chat.completions.create(**default_params)
    return response
