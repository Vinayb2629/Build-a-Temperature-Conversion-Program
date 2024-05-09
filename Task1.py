class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

def main():
    converter = TemperatureConverter()
    continue_conversion = True

    while continue_conversion:
        try:
            temperature = float(input("Enter temperature value: "))
            original_unit = input("Enter the original unit of measurement (C, F, or K): ").upper()

            if original_unit == "C":
                print(f"\n{temperature} degrees Celsius is equal to:")
                print(f"{converter.celsius_to_fahrenheit(temperature):.2f} degrees Fahrenheit")
                print(f"{converter.celsius_to_kelvin(temperature):.2f} Kelvin")

            elif original_unit == "F":
                print(f"\n{temperature} degrees Fahrenheit is equal to:")
                print(f"{converter.fahrenheit_to_celsius(temperature):.2f} degrees Celsius")
                print(f"{converter.fahrenheit_to_kelvin(temperature):.2f} Kelvin")

            elif original_unit == "K":
                print(f"\n{temperature} Kelvin is equal to:")
                print(f"{converter.kelvin_to_celsius(temperature):.2f} degrees Celsius")
                print(f"{converter.kelvin_to_fahrenheit(temperature):.2f} degrees Fahrenheit")

            else:
                print("Invalid unit of measurement. Please enter C, F, or K.")

        except ValueError:
            print("Please enter a valid number for temperature.")

        if input("\nDo you want to perform another conversion? (yes/no): ").lower() != 'yes':
            continue_conversion = False

if __name__ == "__main__":
    main()
