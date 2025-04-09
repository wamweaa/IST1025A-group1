def kilograms_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg * 2.20462

def pounds_to_kilograms(lbs):
    """Convert pounds to kilograms."""
    return lbs / 2.20462

def grams_to_ounces(grams):
    """Convert grams to ounces."""
    return grams * 0.035274

def ounces_to_grams(ounces):
    """Convert ounces to grams."""
    return ounces / 0.035274

# Example usage:
if __name__ == "__main__":
    print(f"10 kg to pounds: {kilograms_to_pounds(10)} lbs")
    print(f"22 lbs to kilograms: {pounds_to_kilograms(22)} kg")
    print(f"100 grams to ounces: {grams_to_ounces(100)} oz")
    print(f"5 ounces to grams: {ounces_to_grams(5)} g")
