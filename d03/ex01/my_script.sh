
Color_Off='\033[0m'
Red='\033[0;31m'      
Green='\033[0;32m'

echo -n "${Green}* Current pip version:${Color_Off} "
python3 -m pip --version | cut -d " " -f 1,2

echo -n "${Green}* pip install: ${Color_Off} "
pip install --log install.log --target=./local_lib --force-reinstall git+https://github.com/jaraco/path.py.git

echo -n ${Green}* Execute Output:${Color_Off}
python3 my_program.py