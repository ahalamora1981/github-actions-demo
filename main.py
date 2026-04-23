"""
演示入口 - 使用 calculator 模块的简单示例。
"""
from src.calculator import add, subtract, multiply, divide, power


def main():
    print("=== GitHub Actions CI/CD 演示 ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"2^8 = {power(2, 8)}")
    print("================================")


if __name__ == "__main__":
    main()
