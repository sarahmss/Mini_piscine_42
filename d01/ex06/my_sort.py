def key_exist(len, d_dict_keys, key):
    if len == 0:
        return False
    for element in d_dict_keys:
        if key == element:
            return True

def make_dict(d):
    sorted_dict =  dict()
    for key, value in d.items():
        if key_exist(len(sorted_dict), sorted_dict.keys(), value) == True:
            sorted_dict[value] += (" " + key) 
        else:
            sorted_dict[value] = key
    for key, value in sorted_dict.items():
        sorted_dict[key] = value.split()
    return(sorted_dict)

def make_sorted_dic(d):
    dic = make_dict(d)
    year_sorted = sorted(dic)

    for element in year_sorted:
        if len(dic[element]) > 1:
            name_sorted = sorted(dic[element])
        else:
            name_sorted = dic[element]
        for item in name_sorted:
                print(item)


def my_sort():
    d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }
    make_sorted_dic(d)

if __name__ == '__main__':
    my_sort()
