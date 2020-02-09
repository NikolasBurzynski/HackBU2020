
def auth(package):
    print(package);
    outPutPackage = package;
    packageLength = len(outPutPackage);
    file = open("auth.txt", "r+");
    data = file.read().replace("\n", " ").split(" ");
    print(data);
    inputUserID = package.split(":")[0];
    package = package.split(":")[1][0:len(package)];
    print(package);
    inputPassword = package.split(":")[0];
    inputPassword = inputPassword[0:len(inputPassword)];
    print(inputUserID);
    print(inputPassword);
    outPutPackage = outPutPackage[len(inputPassword) + len(inputUserID) + 2:packageLength]
    allIds = [];
    allPwds = [];
    for users in data:
        allIds.append(users.split(",")[0]);
        allPwds.append(users.split(",")[1]);
    print(allIds);
    print(allPwds);
    for x in range(0, len(allIds)+1):
        #print(x);
        if(inputUserID == allIds[x] and inputPassword == allPwds[x]):
            print("Authentification Complete");
            postAuthParse(outPutPackage);
            return True;

    print("Invalid userID and/or userPWD");


def postAuthParse(package):
    print(package);



def parse(package):
    package = package[1:len(package)]
#   print(package);
    keyWord = package.split(":")[0];
    if(keyWord == "auth"):
        package = package[len(keyWord) + 1 : len(package)];
        print(len(keyWord));
        print(len(package));
        auth(package);
    elif(keyWord == "create"):
        get(package);
    else:
        print("Invalid Keyword");


inputPackage = input("Simulate an incoming package ");


if(inputPackage[0] == "{"):
#   print("Valid input");
    parse(inputPackage);
else:
    print("Invalid input");
