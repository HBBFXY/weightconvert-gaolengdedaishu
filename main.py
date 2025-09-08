zhongliang = input("输入重量")
num = float(zhongliang[:-2])
if zhongliang[-2:] == "kg" :
    print(f"这个重量{num*2.2046}")
elif zhongliang[-2:] == "pd" :
    print(f"这个重量是{num/2.2046}")
else :
    print("兄弟，带上单位，kg还是pd")
# 老师这肯定没错啊
