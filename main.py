from parking_calc import FeesCalculator


def main():
    fees_calc = FeesCalculator()
    print("!!! Quyidagi vaqtlarni HH:MM formatda kiriting.")
    entered_time = input('Avtomashina kirgan vaqt: >> ')
    try:
        fees_calc.str_to_datetime_object(entered_time)
    except ValueError:
        print(''.join(['<', '-'*30, '>']))
        print('!!!Iltimos vaqtni HH:MM formatda kiriting!')
        print(''.join(['<', '-'*30, '>']))
        entered_time = input('Avtomashina kirgan vaqt: >> ')

    left_time = input('Avtomashina ketgan vaqt: >> ')
    try:
        fees_calc.str_to_datetime_object(left_time)
    except ValueError:
        print(''.join(['<', '-'*30, '>']))
        print('!!!Iltimos vaqtni HH:MM formatda kiriting!')
        print(''.join(['<', '-'*30, '>']))
        left_time = input('Avtomashina ketgan vaqt: >> ')

    result = fees_calc.calc(entered_time, left_time)
    print(''.join(['<', '-'*35, '>']))
    print(f"To'lanishi kerak bo'lgan pul miqdori: {result}$")
    print(''.join(['<', '-'*35, '>']))


if __name__ == "__main__":
    main()
