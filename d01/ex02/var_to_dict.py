
def print_result(d_dict):
    for key, value in d_dict.items():
        print(key, ":", value)

def make_dict(d):
    d_dict =  dict()
    for value, key in d:
        if key_exist(len(d_dict), d_dict.keys(), key) == True:
            d_dict[key] += (" " + value) 
        else:
            d_dict[key] = value
    print_result(d_dict)

def key_exist(len, keys_list, key):
    if len == 0:
        return False
    for element in keys_list:
        if key == element:
            return True
    return False
    
def var_to_dict():
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]
    make_dict(d)

        
if __name__ == '__main__':
  var_to_dict()