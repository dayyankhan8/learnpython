def convert(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60

def main():
    print("What time is it?")
    time_str = input("Please enter the time in 24-hour format (e.g., 12:30): ")

    time_in_hours = convert(time_str)

    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    if breakfast_start <= time_in_hours <= breakfast_end:
        print("It's breakfast time!")
    elif lunch_start <= time_in_hours <= lunch_end:
        print("It's lunch time!")
    elif dinner_start <= time_in_hours <= dinner_end:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
