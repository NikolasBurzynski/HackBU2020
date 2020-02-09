
def auth(package):
    print(package);
    file = open("auth.txt", "r+");
    data = file.read().replace("\n", " ").split(" ");
    print(data);

def get(package):
    print("Still needs to be written");
    
def _set(package):
    print("Still needs to be written");
    

def parse(package):
    package = package[1:len(package)]
#   print(package);
    keyWord = package.split(":")[0];
    if(keyWord == "auth"):
        #package = package[len(keyWord), len(package)];
        auth(package);
    elif(keyWord == "get"):
        get(package);
    elif(keyWord == "set"):
        _set(package);
    else:
        print("Invalid Keyword");


while(True):
    inputPackage = input("Simulate an incoming package ");


    if(inputPackage[0] == "{"):
#       print("Valid input");
        parse(inputPackage);
    else:
        print("Invalid input");






