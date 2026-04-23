"""
Demo entry point - simple example using the calculator module.
"""
from src.calculator import add, subtract, multiply, divide, power


def main():
    print("=== GitHub Actions CI/CD Demo ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"2^8 = {power(2, 8)}")
    print("=================================")


if __name__ == "__main__":
    main()
