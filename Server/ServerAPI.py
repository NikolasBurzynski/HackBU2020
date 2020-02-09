def didPass():
    return True



def auth(package):
    print(package)
    outPutPackage = package
    packageLength = len(outPutPackage)
    file = open("auth.txt", "r+")
    data = file.read().replace("\n", " ").split(" ")
    file.close()
    #print(data)
    splitPackage = package.split(":")
    print(splitPackage)
    inputUserID = splitPackage[0]
    inputPassword = splitPackage[1]
    #print(inputUserID)
    #print(inputPassword)
    outPutPackage = splitPackage[2] + ":" + splitPackage[3]
    allIds = []
    allPwds = []
    for users in data:
        allIds.append(users.split(",")[0])
        allPwds.append(users.split(",")[1])
    #print(allIds)
    #print(allPwds)
    for x in range(0, len(allIds)):
        #print(x)
        if(inputUserID == allIds[x] and inputPassword == allPwds[x]):
            print("Authentification Complete")
            didPass()
            postAuthParse(outPutPackage, inputUserID)
            break

    print("Invalid userID and/or userPWD")


def postAuthParse(package, UserID):
    print(package)
    profileInfo = open("profileInfo.txt", "r+")
    profInfo = profileInfo.read().split("\n")
    print(profInfo)
    splitPackage = package.split(":")
    packageFunction = splitPackage[0]
    argLength = len(splitPackage[1])
    arg = splitPackage[1][0:argLength-1]
    if(packageFunction == "set"):
        for x in range(0, len(profInfo)):
            profileId = profInfo[x][0:6]
            #print("CHECK HERE")
            #print(profileId)
            #print(UserID)
            if(UserID == profileId):
                print("CHECK UNDER ME")
                print(arg)
                profInfo[x].split(",")[3] = arg
                print(profInfo[x].split(",")[3])
        return
    elif(packageFunction == "get"):
        return
    elif(packageFunction == "analyze"):
        return
    #print(packageFunction)

def createID(package):
    auth = open("auth.txt", "r+")
    profileInfo = open("profileInfo.txt", "r+")
    data = auth.read().replace("\n", " ").split(" ")
    numberUsers = len(data)
    userID = "00000" + str(numberUsers)
    while(len(userID) > 6):
        userID = userID[1:len(UserID)]
#    print(userID)
#    print(data)
#    print(package)
    splitPackage = package.split(":")
#    print(splitPackage)
    firstName = splitPackage[1]
    lastName = splitPackage[2]
    pswdLength = len(splitPackage[3])
    pswd = splitPackage[3][0:pswdLength-1]
    if(auth.read() == ""):
        auth.write(userID + "," + pswd)
    else:
        auth.write("\n" + userID + "," + pswd)
    if(profileInfo.read() == ""):
        profileInfo.write(userID + "," + firstName + "," + lastName + "," + "This is where the relation status goes")
    else:
        profileInfo.write("\n" + userID + "," + firstName + "," + lastName + "," + "This is where the relation status goes")

    auth.close()
    profileInfo.close()





def parse(package):
    package = package[1:len(package)]
#   print(package)
    keyWord = package.split(":")[0]
    if(keyWord == "auth"):
        package = package[len(keyWord) + 1 : len(package)]
        print(len(keyWord))
        print(len(package))
        auth(package)
    elif(keyWord == "createID"):
        createID(package)
    else:
        print("Invalid Keyword")

#Code Starts Here

inputPackage = input("Simulate an incoming package ")
if(inputPackage[0] == "{"):
#   print("Valid input")
    parse(inputPackage)
else:
    print("Invalid input")
