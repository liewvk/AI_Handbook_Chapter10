def read_nonnegative(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Enter a nonnegative number.")
                continue
            return value
        except ValueError:
            print("Please enter a number, such as 12.5.")

hours = read_nonnegative("Study hours: ")
print(f"Recorded hours: {hours:.1f}")

