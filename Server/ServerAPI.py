import ServerSockets

def didPass():
    return True

def auth(packet):
    #print(packet)
    outPutPacket = packet
    packetLength = len(outPutPacket)
    file = open("auth.txt", "r+")
    data = file.read().replace("\n", " ").split(" ")
    file.close()
    #print(data)
    splitPacket = packet.split(":")
    #print(splitpacket)
    inputUserID = splitPacket[0]
    inputPassword = splitPacket[1]
    #print(inputUserID)
    #print(inputPassword)
    outPutPacket = splitPacket[2] + ":" + splitPacket[3]
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
            postAuthParse(outPutPacket, inputUserID)
            break
        else:
            print("Invalid userID and/or userPWD")


def postAuthParse(packet, UserID):
    #print(packet)
    splitPacket = packet.split(":")
    function = splitPacket[0]
    argumentLength = len(splitPacket[1])
    argument = splitPacket[1][0:argumentLength-1]
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


def createID(packet):
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
    splitPacket = packet.split(":")
    firstName = splitPacket[1]
    lastName = splitPacket[2]
    pswdLength = len(splitPacket[3])
    pswd = splitPacket[3][0:pswdLength-1]
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

def parse(TXTdata):
    TXTdata = TXTdata[1:len(packet)]
#   print(packet)
    keyWord = TXTdata.split(":")[0]
    if(keyWord == "auth"):
        TXTdata = TXTdata[len(keyWord) + 1 : len(TXTdata)]
        #print(len(keyWord))
        #print(len(packet))
        auth(TXTdata)
    elif(keyWord == "createID"):
        createID(TXTdata)
    else:
        print("Invalid Keyword")


def recieveTXTPacket(data):
    parse(data)

def recieveIMGPacket(data, img):
    parse(data,img)

#Code Starts Here
net = ServerSockets.SocketHandler(recieveTXTPacket,recieveIMGPacket)
net.start_listeners()

while(True):
    pass


#inputpacket = input("Simulate an incoming packet ")
#if(inputpacket[0] == "{"):
#   print("Valid input")
#    parse(inputpacket)
#else:
#    print("Invalid input")