import sys
import os

def read_file(file_name):
    file1 = open(file_name, "r")
    file_content = file1.read()
    file1.close()
    return(file_content)

def check_input():
    if len(sys.argv) != 2:
        return True
    extension = (sys.argv[1])[-9:]
    if extension != ".template":
        return True
    if os.path.isfile(sys.argv[1]) == False \
        or os.path.isfile("settings.py") == False:
        return True

def read_settings():
    settings = dict()
    settings_content = (read_file("settings.py").split("\n"))
    for itens in settings_content:
        if (len(itens) != 0):
            iten = itens.split("=")
            settings[iten[0].strip("\" ")] = iten[1].strip("\" ")
    return(settings)

def make_html(file_name, result):
    final_file = open(file_name, "w")
    final_file.write(result)

def render():
    if check_input() == True:
        return
    template_content = read_file(sys.argv[1])
    settings = read_settings()
    keys = settings.keys()
    for key in keys:
        template_content = template_content.replace('{' + key + '}', settings[key])    
  
    make_html(sys.argv[1].replace(".template", ".html"), template_content)

if __name__ == '__main__':
    render()