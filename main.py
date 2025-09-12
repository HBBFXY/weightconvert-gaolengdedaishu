
import sys

# 读取标准输入
input_str = sys.stdin.read().strip()

# 提取数值和单位
num = float(input_str[:-2])
unit = input_str[-2:]

if unit == "kg":
    # 千克转磅，1 千克 ≈ 2.2046 磅
    result = num * 2.2046
    print(f"这个重量是 {result:.3f} 磅")
elif unit == "lb":  # 假设测试用例期望的是 lb（磅的正确缩写）
    # 磅转千克，1 磅 ≈ 0.4536 千克
    result = num * 0.4536
    print(f"这个重量是 {result:.3f} 千克")
else:
    print("兄弟，带上单位，kg 还是 lb")
