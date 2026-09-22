def calc_bmi(height_cm: float, weight_kg: float) -> float:
    h = height_cm / 100
    return weight_kg / (h * h)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "過輕"
    if bmi < 24:
        return "正常"
    if bmi < 27:
        return "過重"
    return "肥胖"


def main():
    try:
        h = float(input("身高(cm): "))
        w = float(input("體重(kg): "))
        if h <= 0 or w <= 0:
            print("身高體重需大於0")
            return
        bmi = calc_bmi(h, w)
        print(f"BMI: {bmi:.1f} ({bmi_category(bmi)})")
    except ValueError:
        print("請輸入數字")


if __name__ == "__main__":
    main()
