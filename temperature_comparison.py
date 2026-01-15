# ============================================
# 📌 temperature_comparison.py
# 목적: LLM Temperature 파라미터에 따른 응답 비교 실험
# - Temperature=0: 결정적(deterministic) 응답
# - Temperature=0.7: 균형 잡힌 창의성
# - Temperature=2.0: 매우 다양하고 창의적인 응답
# - 동일한 프롬프트에 대해 Temperature 값에 따른 결과 차이를 확인
# ============================================
# 2. Temperature 비교
temperatures = [0, 0.7, 2.0]

for temp in temperatures:
    response = generate_with_params(temperature=temp)
    result = parse_answer(response)

    print(f"\nTemperature: {temp}")
    print(f"결과: {result}")
    print("-" * 50)
    time.sleep(1)
