# ============================================
# 📌 image_analysis_utils.py
# 목적: 이미지 분석 함수 모음
# - analyze_image_from_url: 공개 URL 이미지를 분석
# - analyze_image_base64: Base64 인코딩된 이미지를 분석
# - 내부적으로 client.chat.completions API를 호출하여
#   프롬프트와 이미지를 함께 전달하고 응답을 파싱
# - 교육/데모용 예시 코드
# ============================================
# 이미지 분석 함수
def analyze_image_from_url(image_url, prompt="이 이미지를 자세히 설명해주세요."):
    """URL의 이미지를 분석합니다"""

    response = client.chat.completions.create(
        model=model,
        messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }],
        max_tokens=300)
    return parse_answer(response)

def analyze_image_base64(base64_image, prompt="이 이미지를 자세히 설명해주세요."):
    """Base64 인코딩된 이미지를 분석합니다"""

    response = client.chat.completions.create(
        model=model,
        messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"}
                    }
                ]
            }],
        max_tokens=300)
    return parse_answer(response)
