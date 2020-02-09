
def auth(package):
    print(package);
    file = open("auth.txt", "r+");
    data = file.read().replace("\n", " ").split(" ");
    print(data);
    inputUserID = package.split(":")[0];
    inputPassword = package.split(":")[1];
    inputPassword = inputPassword[0:len(inputPassword)-1];
    print(inputUserID);
    print(inputPassword);
    allIds = [];
    allPwds = [];
    for users in data:
        allIds.append(users.split(",")[0]);
        allPwds.append(users.split(",")[1]);
    print(allIds);
    print(allPwds);
    for x in range(0, len(allIds)+1):
        print(x);
        if(inputUserID == allIds[x] and inputPassword == allPwds[x]):
            print("Authentification Complete");
            return True;

    return False;

def get(package):
    print("Still needs to be written");

def _set(package):
    print("Still needs to be written");


def parse(package):
    package = package[1:len(package)]
#   print(package);
    keyWord = package.split(":")[0];
    if(keyWord == "auth"):
        package = package[len(keyWord) + 1 : len(package)];
        print(len(keyWord));
        print(len(package));
        auth(package);
    elif(keyWord == "get"):
        get(package);
    elif(keyWord == "set"):
        _set(package);
    else:
        print("Invalid Keyword");


inputPackage = input("Simulate an incoming package ");


if(inputPackage[0] == "{"):
#   print("Valid input");
    parse(inputPackage);
else:
    print("Invalid input");
