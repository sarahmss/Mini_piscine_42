import sys

def check_input(states_keys):
    valid = False
    if len(sys.argv) != 2:
        return True
    for element in states_keys:
        if element == sys.argv[1]:
            valid = True
    if valid == False:
        print("Unknown state")
        return True       

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
    if check_input(states.keys()) == True:
        return
    print(capital_cities[states[sys.argv[1]]])

if __name__ == '__main__':
    capital_city()
