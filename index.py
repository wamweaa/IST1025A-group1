# Length & Distance Conversions
def meters_to_feet(meters):
    return meters * 3.2808

def feet_to_meters(feet):
    return feet / 3.28084

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

# Weight & Mass Conversions
def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lbs):
    return lbs / 2.20462

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

# Temperature Conversions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Time Conversions
def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def days_to_weeks(days):
    return days / 7

def weeks_to_days(weeks):
    return weeks * 7

def days_to_months(days):
    return days / 30.44  # Approximate average number of days in a month

def months_to_days(months):
    return months * 30.44

# Speed Conversions
def kmph_to_mph(kmph):
    return kmph * 0.621371

def mph_to_kmph(mph):
    return mph / 0.621371

def meters_per_sec_to_feet_per_sec(mps):
    return mps * 3.28084

def feet_per_sec_to_meters_per_sec(fps):
    return fps / 3.28084

# Volume & Capacity Conversions
def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def milliliters_to_fluid_ounces(ml):
    return ml * 0.033814

def fluid_ounces_to_milliliters(fl_oz):
    return fl_oz / 0.033814

# Main program interface
def main():
    print("Unit Conversion Program")
    while True:
        # Display main menu
        print("\nChoose a category:")
        print("1. Length & Distance")
        print("2. Weight & Mass")
        print("3. Temperature")
        print("4. Time & Seconds")
        print("5. Speed")
        print("6. Volume & Capacity")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        # Length & Distance
        if choice == "1":
            value = float(input("Enter value: "))
            print("1. Meters to Feet\n2. Feet to Meters\n3. Kilometers to Miles\n4. Miles to Kilometers")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value} meters = {meters_to_feet(value):.2f} feet")
            elif sub_choice == "2":
                print(f"{value} feet = {feet_to_meters(value):.2f} meters")
            elif sub_choice == "3":
                print(f"{value} km = {kilometers_to_miles(value):.2f} miles")
            elif sub_choice == "4":
                print(f"{value} miles = {miles_to_kilometers(value):.2f} km")

        # Weight & Mass
        elif choice == "2":
            value = float(input("Enter value: "))
            print("1. Kilograms to Pounds\n2. Pounds to Kilograms\n3. Grams to Ounces\n4. Ounces to Grams")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value} kg = {kilograms_to_pounds(value):.2f} lbs")
            elif sub_choice == "2":
                print(f"{value} lbs = {pounds_to_kilograms(value):.2f} kg")
            elif sub_choice == "3":
                print(f"{value} grams = {grams_to_ounces(value):.2f} ounces")
            elif sub_choice == "4":
                print(f"{value} ounces = {ounces_to_grams(value):.2f} grams")

        # Temperature
        elif choice == "3":
            value = float(input("Enter value: "))
            print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\n4. Kelvin to Celsius")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
            elif sub_choice == "2":
                print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
            elif sub_choice == "3":
                print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
            elif sub_choice == "4":
                print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")

        # Time
        elif choice == "4":
            value = float(input("Enter value: "))
            print("1. Hours to Minutes\n2. Minutes to Hours\n3. Days to Weeks\n4. Weeks to Days\n5. Days to Months\n6. Months to Days")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value} hours = {hours_to_minutes(value):.2f} minutes")
            elif sub_choice == "2":
                print(f"{value} minutes = {minutes_to_hours(value):.2f} hours")
            elif sub_choice == "3":
                print(f"{value} days = {days_to_weeks(value):.2f} weeks")
            elif sub_choice == "4":
                print(f"{value} weeks = {weeks_to_days(value):.2f} days")
            elif sub_choice == "5":
                print(f"{value} days = {days_to_months(value):.2f} months")
            elif sub_choice == "6":
                print(f"{value} months = {months_to_days(value):.2f} days")

        # Speed
        elif choice == "5":
            value = float(input("Enter value: "))
            print("1. km/h to mph\n2. mph to km/h\n3. m/s to ft/s\n4. ft/s to m/s")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value} km/h = {kmph_to_mph(value):.2f} mph")
            elif sub_choice == "2":
                print(f"{value} mph = {mph_to_kmph(value):.2f} km/h")
            elif sub_choice == "3":
                print(f"{value} m/s = {meters_per_sec_to_feet_per_sec(value):.2f} ft/s")
            elif sub_choice == "4":
                print(f"{value} ft/s = {feet_per_sec_to_meters_per_sec(value):.2f} m/s")

        # Volume & Capacity
        elif choice == "6":
            value = float(input("Enter value: "))
            print("1. Liters to Gallons\n2. Gallons to Liters\n3. Milliliters to Fluid Ounces\n4. Fluid Ounces to Milliliters")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                print(f"{value} liters = {liters_to_gallons(value):.2f} gallons")
            elif sub_choice == "2":
                print(f"{value} gallons = {gallons_to_liters(value):.2f} liters")
            elif sub_choice == "3":
                print(f"{value} ml = {milliliters_to_fluid_ounces(value):.2f} fl oz")
            elif sub_choice == "4":
                print(f"{value} fl oz = {fluid_ounces_to_milliliters(value):.2f} ml")

        # Exit program
        elif choice == "7":
            break

        # Handle invalid choices
        else:
            print("Invalid choice. Try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
