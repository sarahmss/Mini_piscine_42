import sys

def check_input():
    if len(sys.argv) != 2:
        return True

def get_args():
    i = 0
    args = ((sys.argv[1]).split(","))
    for items in args:
        args[i] = items.strip(" ")
        i += 1
    return args

def search_key(_dict, key_to_find):
    for key, value in _dict.items():
        if key.lower() == key_to_find.lower():
            return(key)

def search_value(_dict, value_to_find):
    for key, value in _dict.items():
        if value.lower() == value_to_find.lower():
            return(value)

def find_capital(states, capital_cities, key):
    if key != None and capital_cities[states[key]] != None:
        print(capital_cities[states[key]], "is the capital of", key)
        return True
    return False

def find_state(states, capital_cities, value):
    if value != None:
        for key_c, value_c in capital_cities.items():
            if value_c == value:
                for key_s, value_s in states.items():
                    if (key_c == value_s):
                        print(value, "is the capital of", key_s)
                        return True
    return False

def find(states, capital_cities, element):
    s_key = search_key(states, element)
    c_key = search_key(capital_cities, element)
    s_value = search_value(states, element)
    c_value = search_value(capital_cities, element)
    v1 = find_capital(states, capital_cities, s_key)
    v2 = find_capital(states, capital_cities, c_key)
    v3 = find_state(states, capital_cities, s_value) 
    v4 = find_state(states, capital_cities, c_value)
    if v1 == False and v2 == False and v3 == False and v4 == False:
        return False
    return True
    

def print_result(states, capital_cities, args):
    for element in args:
        if len(element.strip()) != 0:
            if find(states, capital_cities, element) == False:
                print(element, "is neither a capital city nor a state")


def all_in():
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
    if check_input() == True:
        return
    print_result(states, capital_cities, get_args())

if __name__ == '__main__':
    all_in()
