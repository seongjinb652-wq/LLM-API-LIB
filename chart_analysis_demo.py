# ============================================
# 📌 chart_analysis_demo.py
# 목적: 차트/그래프 이미지 생성 및 분석 예제
# - matplotlib을 사용해 월별 매출 데이터를 시각화
# - 생성된 이미지를 base64로 변환하여 분석 함수에 전달
# - 분석 프롬프트를 통해 차트 종류, 트렌드, 주요 인사이트 확인
# - 교육/데모용 예시 코드
# ============================================
# 차트/그래프 이미지 생성 및 분석 예제
def create_sample_chart():
    # 데이터 생성
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [135, 120, 108, 92, 130, 195]

    # 차트 생성
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, marker='o', linewidth=2, markersize=8)
    plt.title('Monthly sales', fontsize=16, fontweight='bold')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sold ($1M)', fontsize=12)
    plt.grid(True, alpha=0.2)
    plt.tight_layout()

    # 이미지를 base64로 변환
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.show()

    return image_base64

# 차트 생성 및 분석
print("차트 생성 중...")
chart_base64 = create_sample_chart()

# 차트 분석
chart_analysis_prompt = """
이 차트를 분석해서 다음 내용을 알려주세요:
1. 차트의 종류와 표현하는 데이터
2. 트렌드나 패턴
3. 주요 인사이트나 발견사항
"""

print("차트 분석 중...")
chart_analysis = analyze_image_base64(chart_base64, chart_analysis_prompt)
print("차트 분석 결과:")
print(chart_analysis)
