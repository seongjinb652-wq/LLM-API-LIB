# ============================================
# 📌 conversation_with_prompt.py
# 목적: 대화 시뮬레이션에서 어시스턴트 프롬프트 삽입 예제
# - system, user, assistant 역할을 지정하여 대화 맥락 구성
# - 어시스턴트 프롬프트를 삽입해 모델에게 선행된 대화 메모리를 제공
# - 예시 코드로, 실제 응용에서는 대화 컨텍스트 관리에 활용 가능
# ============================================
conversation_response = client.chat.completions.create(
        model=model,
        messages=[{"role":"system", "content": "당신은 산타할아버지입니다. 올해 나쁜 짓을 한 아이는 선물을 받을 수 없습니다."},
                  {"role": "user", "content": "안녕하세요 산타할아버지! 제게 올해 여름에 무슨 일을 했는지 아시나요?"},
                  {"role": "assistant", "content": "화가 나서 친구와 싸웠구나. 못된 말도 했구나!"}, # 어시스턴트 프롬프트
                  {"role": "user", "content": "제가 올해 크리스마스에 선물을 받을 수 있을까요?"}]
    )

# 이와 같이 어시스턴트 프롬프트를 삽입할 경우, 모델에게 선행된 대화의 메모리를 제공하거나 답변의 보조 도구로 사용할 수 있음
print("대화 결과:", parse_answer(conversation_response))
