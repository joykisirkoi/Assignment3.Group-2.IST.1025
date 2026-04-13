# Function to convert Fahrenheit to Celsius
def convert(fahrenheit):
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

# Main program
def main():
    try:
        # Input temperature in Fahrenheit
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        # Convert using the function
        celsius = convert(fahrenheit)

        # Display Celsius value (rounded to 2 decimal places)
        print(f"Temperature in Celsius: {celsius:.2f}")

        # Check condition and print message
        if celsius > 20:
            print("ITS HOT HERE")
        else:
            print("ITS COLD HERE")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()
