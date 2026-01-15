# ============================================
# 📌 openai_colab_secrets.py
# 목적: Google Colab Secrets를 사용해 OpenAI API 키를 불러오고 모델 호출
# - google.colab.userdata 모듈을 통해 API 키를 안전하게 불러오기
# - 불러오기 실패 시 직접 입력 방법 안내
# - OpenAI 클라이언트 초기화 후 간단한 프롬프트 실행
# - 실제 프로젝트에서는 보안에 주의하여 사용
# ============================================

# 방법 1: Google Colab Secrets 사용 (상대적으로 안전)

try:
    from google.colab import userdata
    api_key = userdata.get('OPENAI_API_KEY')
    print("Colab Secrets에서 API 키를 성공적으로 불러왔습니다.")
except Exception as e:
    print("Colab Secrets를 사용할 수 없습니다.")
    print("대신 직접 입력 방법을 사용하세요.")
    api_key = None
model = "gpt-4.1-mini"  # 모델 설정

response = client.chat.completions.create(
        model=model,
        messages=[{"role":"user", "content":"너는 누구니?"}])   # 프롬프트

print(response)
