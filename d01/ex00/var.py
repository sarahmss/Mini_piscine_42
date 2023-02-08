def my_var():
    var_int = 42
    var_str1 = "42"
    var_str2 = "quarante-deux"
    var_float = 42.0
    var_bool = True
    var_list = [42]     # List items are ordered, changeable, and allow duplicate values.
    var_dict = {42: 42} # A dictionary is a collection which is ordered*, changeable and do not allow duplicates
    var_tuple = (42,)   # A tuple is a collection which is ordered and unchangeable.
    var_set = set()     # Set items are unordered, unchangeable, and do not allow duplicate values.

    print(var_int, "has a type", type(var_int))
    print(var_str1, "has a type", type(var_str1))
    print(var_str2, "has a type", type(var_str2))
    print(var_float, "has a type", type(var_float))
    print(var_bool, "has a type", type(var_bool))
    print(var_list, "has a type", type(var_list))
    print(var_dict, "has a type", type(var_dict))
    print(var_tuple, "has a type", type(var_tuple))
    print(var_set, "has a type", type(var_set))

if __name__ == '__main__':
    my_var()