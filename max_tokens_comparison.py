# ============================================
# 📌 max_tokens_comparison.py
# 목적: LLM Max Tokens 파라미터에 따른 응답 비교 실험
# - Max Tokens=50: 짧은 응답, 요약 중심
# - Max Tokens=200: 긴 응답, 세부 설명 포함
# - 동일한 프롬프트에 대해 토큰 제한 값에 따른 결과 차이를 확인
# ============================================
# 1. Max Tokens 비교
token_limits = [50, 200]

for max_tokens in token_limits:
    response = generate_with_params(max_tokens=max_tokens)
    result = parse_answer(response)

    print(f"\nMax Tokens: {max_tokens}")
    print(f"출력된 토큰 수: {response.usage.completion_tokens}")
    print(f"결과: {result}")
    print("-" * 50)
    time.sleep(1)
