import math

def solve_log_problem():
    """
    사용자 입력을 받아 로그 함수 관련 문제를 해결합니다.
    - 밑과 진수를 입력받아 로그 값을 계산합니다.
    - 밑변환 공식 예시를 보여줍니다.
    """
    print("--- 로그 함수 문제 해결기 ---")
    print("1. 기본 로그 값 계산 (log_b(a))")
    print("2. 밑변환 공식 예시 보기")
    print("--------------------------")

    choice = input("원하는 작업의 번호를 입력하세요 (1 또는 2): ")

    if choice == '1':
        try:
            base_str = input("로그의 밑(b)을 입력하세요: ")
            base = float(base_str)

            if base <= 0 or base == 1:
                print("오류: 로그의 밑은 0보다 크고 1이 아니어야 합니다.")
                return

            argument_str = input("로그의 진수(a)를 입력하세요: ")
            argument = float(argument_str)

            if argument <= 0:
                print("오류: 로그의 진수는 0보다 커야 합니다.")
                return

            # math.log(x, base)는 x를 밑이 base인 로그로 계산합니다.
            # 밑이 생략되면 자연로그(ln)를 계산합니다.
            result = math.log(argument, base)
            print(f"\nlog_{base}({argument}) = {result:.4f}") # 소수점 4자리까지 표시

        except ValueError:
            print("오류: 유효한 숫자를 입력해주세요.")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

    elif choice == '2':
        print("\n--- 밑변환 공식 (Change of Base Formula) ---")
        print("공식: log_b(a) = log_c(a) / log_c(b)")
        print("여기서 'c'는 어떤 양수이든 될 수 있으며, 보통 10(상용로그) 또는 e(자연로그)를 사용합니다.")
        print("\n예시: log_2(8)을 상용로그(log_10)로 계산해 봅시다.")
        print("log_2(8) = log_10(8) / log_10(2)")

        try:
            log10_8 = math.log10(8)
            log10_2 = math.log10(2)
            calculated_result = log10_8 / log10_2
            actual_log2_8 = math.log2(8) # math.log2는 밑이 2인 로그를 직접 계산

            print(f"log_10(8) = {log10_8:.4f}")
            print(f"log_10(2) = {log10_2:.4f}")
            print(f"계산 결과 (log_10(8) / log_10(2)): {calculated_result:.4f}")
            print(f"실제 log_2(8) 값 (math.log2 사용): {actual_log2_8:.4f}")
            print("\n밑변환 공식을 통해 동일한 값을 얻을 수 있습니다!")

        except Exception as e:
            print(f"예시 계산 중 오류가 발생했습니다: {e}")

    else:
        print("유효하지 않은 선택입니다. 1 또는 2를 입력해주세요.")

# 프로그램 실행
solve_log_problem()
