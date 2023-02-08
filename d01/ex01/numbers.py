def read_file():
    file1 = open("numbers.txt")
    file_content = file1.read()
    file1.close()
    return(file_content)

def make_str(file_content):
    clean =  file_content.replace(",", "\n")
    print(clean.strip('\n'))

if __name__ == '__main__':
   make_str(read_file())
        