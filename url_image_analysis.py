# ============================================
# 📌 url_image_analysis_demo.py
# 목적: 공개 URL 이미지를 불러와 다양한 관점에서 분석하는 예제
# - analyze_image_from_url 함수를 사용해 기본 분석 수행
# - 추가 질문을 통해 색상, 분위기, 자연 요소 등 세부 분석 진행
# - 교육/데모용 예시 코드
# ============================================
# 예제 이미지 분석 (공개 URL 사용)
sample_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/1280px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

print("이미지 분석 중...")
analysis = analyze_image_from_url(sample_image_url)
print("이미지 분석 결과:")
print(analysis)

# 다양한 분석 질문 예제
analysis_questions = [
    "이 이미지의 주된 색상은 무엇인가요?",
    "이 장소는 어떤 느낌을 주나요?",
    "이 이미지에서 볼 수 있는 자연 요소들을 나열해주세요."
]

print("다양한 관점에서의 이미지 분석:")

for i, question in enumerate(analysis_questions, 1):
    print(f"\n{i}. {question}")
    result = analyze_image_from_url(sample_image_url, question)
    print(f"답변: {result}")
    time.sleep(1)
