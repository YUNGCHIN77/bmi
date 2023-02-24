height = float(input("請輸入您的身高(公分)\n"))
weight = float(input("請輸入您的體重(公斤)\n"))

height /= 100
BMI = round(weight/height**2 ,1)

if BMI>=35:
    print(f"您的BMI是:{BMI} (重度肥胖)")
elif BMI>=30:
    print("您的BMI是:" + str(BMI) +" (中度肥胖)")
elif BMI>=27:
    print("您的BMI是:" + str(BMI) +" (輕度肥胖)")
elif BMI>=24:
    print("您的BMI是:" + str(BMI) +" (體重過重)")
elif BMI>=18.5:
    print("您的BMI是:" + str(BMI) +" (正常體位)")
else:
    print("您的BMI是:" + str(BMI) +" (體重過輕)") 


