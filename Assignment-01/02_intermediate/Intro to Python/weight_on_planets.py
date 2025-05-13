earth_weight = float(input("Enter a weight on Earth: "))

choice = input("Do you want to calculate weight for Mars only? (yes/no): ")


if choice.lower() == "yes":
    mars_weight = earth_weight * 0.378
    rounded_weight = round(mars_weight, 2)
    print("The equivalent on Mars:", rounded_weight)


else:
    planet = input("Enter a planet: ")

    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    if planet in gravity_factors:
        planet_weight = earth_weight * gravity_factors[planet]
        rounded_weight = round(planet_weight, 2)
        print("The equivalent weight on", planet + ":", rounded_weight)
    else:
        print("Invalid planet name!")
