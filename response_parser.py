# ============================================
# 📌 response_parser.py
# 목적: LLM API 호출 결과에서 응답 정보 출력 및 답변 파싱 함수 정의
# - 사용된 모델명, 답변 내용, 입력/출력 토큰 수 출력
# - parse_answer 함수: 응답 객체에서 GPT 답변 텍스트만 추출
# - 교육/데모용 예시 코드로, 실제 프로젝트에서는 응답 로깅/모니터링 모듈로 확장 가능
# ============================================

print(f"사용된 모델 : {response.model}")
print(f"답변 : {response.choices[0].message.content}")
print(f"입력 토큰 수 : {response.usage.prompt_tokens}")
print(f"출력 토큰 수 : {response.usage.completion_tokens}")
# API 호출 결과 중 GPT의 답변을 파싱하는 함수
def parse_answer(response):
    return response.choices[0].message.content
