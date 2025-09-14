weight_input = input()
unit = weight_input[-2:] 
value = float(weight_input[:-2]) 
if unit == 'kg':
    result = value * 2.2046
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == 'pd':
    result = value / 2.2049
    print(f"对应的公制重量为{result:.3f}公斤")
else:
    print("输入格式错误，请使用'kg'或'pd'作为单位（如10kg、5pd）")
