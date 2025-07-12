import matplotlib.pyplot as plt
import numpy as np

# --- 1. 데이터 생성 ---
# 연도 데이터 (예: 100년)
years = np.arange(1, 101)

# 가상 인구 데이터 (초기 인구 1000명, 매년 10%씩 증가)
# 지수 함수적으로 증가하는 데이터를 만듭니다.
initial_population = 1000
growth_rate = 0.10
population = initial_population * (1 + growth_rate)**(years - 1)

# --- 2. 그래프 시각화 ---
plt.figure(figsize=(14, 6)) # 전체 그림의 크기 설정

# 2-1. 일반 스케일 그래프
plt.subplot(1, 2, 1) # 1행 2열 중 첫 번째 플롯
plt.plot(years, population, marker='o', markersize=4, linestyle='-')
plt.title('일반 스케일 인구 증가 (Linear Scale)', fontsize=14)
plt.xlabel('연도', fontsize=12)
plt.ylabel('인구 수', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) # 그리드 라인 추가
plt.ticklabel_format(style='plain', axis='y') # y축 지수표기법 방지

# 2-2. 로그 스케일 그래프
plt.subplot(1, 2, 2) # 1행 2열 중 두 번째 플롯
plt.plot(years, population, marker='o', markersize=4, linestyle='-')
plt.title('로그 스케일 인구 증가 (Log Scale)', fontsize=14)
plt.xlabel('연도', fontsize=12)
plt.ylabel('인구 수 (로그 스케일)', fontsize=12)
plt.yscale('log') # y축을 로그 스케일로 설정하는 핵심 부분
plt.grid(True, linestyle='--', alpha=0.7) # 그리드 라인 추가

# 레이아웃 조정 및 그래프 표시
plt.tight_layout() # 서브플롯 간의 간격 자동 조절
plt.show()
