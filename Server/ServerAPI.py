
def auth(package):
    print(package);
    outPutPackage = package;
    packageLength = len(outPutPackage);
    file = open("auth.txt", "r+");
    data = file.read().replace("\n", " ").split(" ");
    file.close();
    #print(data);
    splitPackage = package.split(":");
    print(splitPackage);
    inputUserID = splitPackage[0];
    inputPassword = splitPackage[1];
    #print(inputUserID);
    #print(inputPassword);
    outPutPackage = splitPackage[2] + splitPackage[3];
    allIds = [];
    allPwds = [];
    for users in data:
        allIds.append(users.split(",")[0]);
        allPwds.append(users.split(",")[1]);
    #print(allIds);
    #print(allPwds);
    for x in range(0, len(allIds)):
        #print(x);
        if(inputUserID == allIds[x] and inputPassword == allPwds[x]):
            print("Authentification Complete");
            postAuthParse(outPutPackage);
            return True;

    print("Invalid userID and/or userPWD");


def postAuthParse(package):
    #print(package);
    packageFunction = package.split(":")[0];
    #print(packageFunction);

def createID(package):
    auth = open("auth.txt", "r+");
    data = auth.read().replace("\n", " ").split(" ");
    numberUsers = len(data) + 1;
    userID = "00000" + str(numberUsers);
    while(len(userID) > 6):
        userID = userID[1:len(UserID)];
    print(userID);
    print(data);
    print(package);
    splitPackage = package.split(":");
    print(splitPackage);
    firstName = splitPackage[1];
    lastName = splitPackage[2];
    pswdLength = len(splitPackage[3]);
    pswd = splitPackage[3][0:pswdLength-1];
    auth.write("\n" + userID + "," + pswd);




def parse(package):
    package = package[1:len(package)]
#   print(package);
    keyWord = package.split(":")[0];
    if(keyWord == "auth"):
        package = package[len(keyWord) + 1 : len(package)];
        print(len(keyWord));
        print(len(package));
        auth(package);
    elif(keyWord == "createID"):
        createID(package);
    else:
        print("Invalid Keyword");

#Code Starts Here

inputPackage = input("Simulate an incoming package ");
if(inputPackage[0] == "{"):
#   print("Valid input");
    parse(inputPackage);
else:
    print("Invalid input");
