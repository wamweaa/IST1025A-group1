"""Conversion functions used by the CON-VERT Flask backend."""

# Length & Distance
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

# Weight & Mass
def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lbs):
    return lbs / 2.20462

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

# Temperature
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Time
def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

def days_to_weeks(days):
    return days / 7

def weeks_to_days(weeks):
    return weeks * 7

def days_to_months(days):
    return days / 30.44

def months_to_days(months):
    return months * 30.44

# Speed
def kmph_to_mph(kmph):
    return kmph * 0.621371

def mph_to_kmph(mph):
    return mph / 0.621371

def meters_per_sec_to_feet_per_sec(mps):
    return mps * 3.28084

def feet_per_sec_to_meters_per_sec(fps):
    return fps / 3.28084

# Volume & Capacity
def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def milliliters_to_fluid_ounces(ml):
    return ml * 0.033814

def fluid_ounces_to_milliliters(fl_oz):
    return fl_oz / 0.033814


# Conversion menu: category -> displayed option -> Python function
CONVERSIONS = {
    "length": {
        "Meters to Feet": meters_to_feet,
        "Feet to Meters": feet_to_meters,
        "Kilometers to Miles": kilometers_to_miles,
        "Miles to Kilometers": miles_to_kilometers,
    },
    "weight": {
        "Kilograms to Pounds": kilograms_to_pounds,
        "Pounds to Kilograms": pounds_to_kilograms,
        "Grams to Ounces": grams_to_ounces,
        "Ounces to Grams": ounces_to_grams,
    },
    "temperature": {
        "Celsius to Fahrenheit": celsius_to_fahrenheit,
        "Fahrenheit to Celsius": fahrenheit_to_celsius,
        "Celsius to Kelvin": celsius_to_kelvin,
        "Kelvin to Celsius": kelvin_to_celsius,
    },
    "time": {
        "Hours to Minutes": hours_to_minutes,
        "Minutes to Hours": minutes_to_hours,
        "Days to Weeks": days_to_weeks,
        "Weeks to Days": weeks_to_days,
        "Days to Months": days_to_months,
        "Months to Days": months_to_days,
    },
    "speed": {
        "Km/h to Mph": kmph_to_mph,
        "Mph to Km/h": mph_to_kmph,
        "M/s to Ft/s": meters_per_sec_to_feet_per_sec,
        "Ft/s to M/s": feet_per_sec_to_meters_per_sec,
    },
    "volume": {
        "Liters to Gallons": liters_to_gallons,
        "Gallons to Liters": gallons_to_liters,
        "Milliliters to Fluid Ounces": milliliters_to_fluid_ounces,
        "Fluid Ounces to Milliliters": fluid_ounces_to_milliliters,
    },
}
