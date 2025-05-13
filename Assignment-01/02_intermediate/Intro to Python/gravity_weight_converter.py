"""
Prompts the user for a weight on Earth and a planet (in separate inputs). 
Then prints the equivalent weight on that planet.

Note: The user should type the planet with the first letter capitalized.
"""

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
        print("The equivalent weight on Mars:", round(mars_weight, 2))
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
        planet_weight = earth_weight * gravity
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")

if __name__ == "__main__":
    main()
