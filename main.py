zhongliang = input()
num = float(zhongliang[:-2])
if zhongliang[-2:] == "kg" :
    jieguo = num * 2.2046
    print(f"这个重量{jieguo:.3f}")
elif zhongliang[-2:] == "pd" :
    jieguo = num/2.2046
    print(f"这个重量是{jieguo:.3f}")
else :
    print("kg还是pd")
# 老师这肯定没错啊
