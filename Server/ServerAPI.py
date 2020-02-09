def didPass():
    return True



def auth(package):
    #print(package)
    outPutPackage = package
    packageLength = len(outPutPackage)
    file = open("auth.txt", "r+")
    data = file.read().replace("\n", " ").split(" ")
    file.close()
    #print(data)
    splitPackage = package.split(":")
    #print(splitPackage)
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
        else:
            print("Invalid userID and/or userPWD")


def postAuthParse(package, UserID):
    #print(package)
    splitPackage = package.split(":")
    function = splitPackage[0]
    argumentLength = len(splitPackage[1])
    argument = splitPackage[1][0:argumentLength-1]
    #print("USER ID")
    #print(UserID)
    profileInfo = open("profileInfo.txt", "r+")
    profInfo = profileInfo.read().split("\n")
    #print(profInfo)
    if(function == "set"):
        for x in range(0,len(profInfo)):
            splitInfo = profInfo[x].split(",")
            if(splitInfo[0] == UserID):
            #print("Changing status")
            #print(splitInfo[3])
                tempStringArray = profInfo[x].split(",")
                splitInfo[3] = argument
                profInfo[x] = tempStringArray[0] + "," + tempStringArray[1] + "," + tempStringArray[2] + "," + splitInfo[3]
            #print(profInfo[x])
            #print(splitInfo[3])
            #print("Done changing the array")
            #print(profInfo)
            profileInfo.truncate(0)
            for x in range(0,len(profInfo)):
                if(x == len(profInfo)-1):
                    profileInfo.write(profInfo[x])
                elif(x == 0):
                    profileInfo.seek(0)
                    profileInfo.write(profInfo[x] + "\n")
                else:
                    profileInfo.write(profInfo[x] + "\n")
                    profileInfo.close();
                    #print("We done")
    elif(function == "get"):
        #print("Start Here")
        #print(profInfo)
        for x in range(0,len(profInfo)):
            #print(profInfo[x])
            #print(UserID)
            splitProfInfo = profInfo[x].split(",")
            if(splitProfInfo[0] == UserID):
                print("Recieved Information")
                print(splitProfInfo[3])

    else:
        print("Invalid function")


def createID(package):
    auth = open("auth.txt", "r+")
    profileInfo = open("profileInfo.txt", "r+")
    currentAuths = auth.read();
    currentProfiles = profileInfo.read();
    data = currentAuths.replace("\n", " ").split(" ")
    if(data[0] ==''):
        numberUsers = 1;
    else:
        numberUsers = len(data)+1
    userID = "00000" + str(numberUsers)
    while(len(userID) > 6):
        userID = userID[1:len(UserID)]
    splitPackage = package.split(":")
    firstName = splitPackage[1]
    lastName = splitPackage[2]
    pswdLength = len(splitPackage[3])
    pswd = splitPackage[3][0:pswdLength-1]
    if(currentAuths == ""):
        auth.write(userID + "," + pswd)
    else:
        auth.write("\n" + userID + "," + pswd)
    if(currentProfiles == ""):
        profileInfo.write(userID + "," + firstName + "," + lastName + "," + "relation")
    else:
        profileInfo.write("\n" + userID + "," + firstName + "," + lastName + "," + "relation")

    auth.close()
    profileInfo.close()





def parse(package):
    package = package[1:len(package)]
#   print(package)
    keyWord = package.split(":")[0]
    if(keyWord == "auth"):
        package = package[len(keyWord) + 1 : len(package)]
        #print(len(keyWord))
        #print(len(package))
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
