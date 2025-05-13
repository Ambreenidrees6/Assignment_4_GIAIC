"""A program to calculate weight on Mars or any other planet in the solar system."""


MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
  
    earth_weight = float(input("Enter a weight on Earth: "))
    
    choice = input("Do you want to calculate weight for Mars only? (yes/no): ").strip().lower()

    if choice == 'yes':
        mars_weight = earth_weight * MARS_GRAVITY
        rounded_weight = round(mars_weight, 2)
        print("The equivalent weight on Mars:", rounded_weight)

    else:
       planet = input("Enter a planet: ").strip().title()

    if planet == "Mercury":
            gravity = MERCURY_GRAVITY
    elif planet == "Venus":
            gravity = VENUS_GRAVITY
    elif planet == "Mars":
            gravity = MARS_GRAVITY
    elif planet == "Jupiter":
            gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
            gravity = SATURN_GRAVITY
    elif planet == "Uranus":
            gravity = URANUS_GRAVITY
    elif planet == "Neptune":
            gravity = NEPTUNE_GRAVITY
    else:
            print("Invalid planet name!")
            return

    planetary_weight = earth_weight * gravity
    rounded_weight = round(planetary_weight, 2)
    print("The equivalent weight on", planet + ":", rounded_weight)

if __name__ == '__main__':
    main()
