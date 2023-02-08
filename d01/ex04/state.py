import sys

def check_input(capital_cities_values):
    valid = False
    if len(sys.argv) != 2:
        return True
    for element in capital_cities_values:
        if element == sys.argv[1]:
            valid = True
    if valid == False:
        print("Unknown capital city")
        return True       

def print_result(states, capital_cities):
    for key_c, value_c in capital_cities.items():
        if value_c == sys.argv[1]:
            for key_s, value_s in states.items():
                if (key_c == value_s):
                    print(key_s)

def capital_city():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if check_input(capital_cities.values()) == True:
        return
    print_result(states, capital_cities)

if __name__ == '__main__':
    capital_city()
