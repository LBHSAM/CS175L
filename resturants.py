#Anthony Mendes
#restaurants

restaurants = {
    "Joe’s Gourmet Burgers": {"Vegetarian": False, "Vegan": False, "Gluten-Free": False},
    "Main Street Pizza Company": {"Vegetarian": True, "Vegan": False, "Gluten-Free": True},
    "Corner Café": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True},
    "Mama’s Fine Italian": {"Vegetarian": True, "Vegan": False, "Gluten-Free": False},
    "The Chef’s Kitchen": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True}
}

def filter_restaurants(vegetarian, vegan, gluten_free):
    choices = []
    for restaurant, options in restaurants.items():
        if (not vegetarian or options["Vegetarian"]) and \
           (not vegan or options["Vegan"]) and \
           (not gluten_free or options["Gluten-Free"]):
            choices.append(restaurant)
    return choices

def main():
    repeat = 'yes'
    while repeat == 'yes':
        vegetarian = input("Is anyone in your party vegetarian? ").lower() == 'yes'
        vegan = input("Is anyone in your party vegan? ").lower() == 'yes'
        gluten_free = input("Is anyone in your party gluten-free? ").lower() == 'yes'

        print("Here are your restaurant choices:")
        for choice in filter_restaurants(vegetarian, vegan, gluten_free):
            print(choice)

        repeat = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ").lower()

if __name__ == "__main__":
    main()
