number = []
while True:
    num = int(input("Enter a number to average or type '0' to quit: "))
    if num == 0:
        print("Ok, exiting...")
        break

    try:
        number.append(num)
        if len(number)>3:
            number.pop(0)

        aveg = sum(number)/len(number)
        print(f"The average of the last {len(number)} numbers is {aveg}")
    except ValueError:
        print("Invalid entry! Try again...")
