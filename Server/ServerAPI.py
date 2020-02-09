import ServerSockets
import cv2
import os.path
import add_image
from os import path


#def didPass():
#    return "Allow"

def auth(packet, img = None):
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
            return postAuthParse(outPutPacket, inputUserID, img)
            break
        else:
            print("Invalid userID and/or userPWD")
            return "Deny", False


def postAuthParse(packet, UserID, img = None):
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
    if(function == "set" and argument == "Single" or argument == "Taken" or argument == "Not Looking"):
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
                    profileInfo.seek(0)
                    profileInfo.write(profInfo[x])
                    profileInfo.close()
                    return argument, False
                elif(x == 0):
                    profileInfo.seek(0)
                    profileInfo.write(profInfo[x] + "\n")
                    profileInfo.close()
                    return argument, False
                else:
                    profileInfo.seek(0)
                    profileInfo.write(profInfo[x] + "\n")
                    profileInfo.close()
                    return argument, False
                    #print("We done")
    elif(function == "get"):
        #print("Start Here")
        #print(profInfo)
        for x in range(0,len(profInfo)):
            #print(profInfo[x])
            #print(UserID)
            splitProfInfo = profInfo[x].split(",")
            if(splitProfInfo[0] == UserID):
                if(argument == "First Name"):
                    return splitProfInfo[1], False
                elif(argument == "Last Name"):
                    return splitProfInfo[2], False
                elif(argument == "Status"):
                    return splitProfInfo[3], False
                else:
                    return "Invalid Argument", False
    elif(function == "login"):
        return "Allow", False
    elif(function == "getFirstName"):
        for x in range(0,len(profInfo)):
            splitInfo = profInfo[x].split(",")
            if(splitInfo[0] == argument):
                return splitInfo[1], False
    elif(function == "getStatus"):
        for x in range(0,len(profInfo)):
            splitInfo = profInfo[x].split(",")
            if(splitInfo[0] == argument):
                return splitInfo[3], False
    elif(function[0] == "i"):
        #photo mode activated
        functionLength = len(function);
        index = function[1:len(function)];
        targetId = UserID;
        directory = "Imgs/" + targetId + "/" + index + "vP.jpg"
        if(path.exists(directory)):
            img = cv2.imread(directory)
            print("basic")
            return ServerSockets.picture_to_data(img), True

        directory = "Imgs/" + targetId + "/" + index + "vH.jpg"
        if(path.exists(directory) and targetId == UserID):
            print("Private")
            img = cv2.imread(directory)
            return ServerSockets.picture_to_data(img), True

        print("No photo")
        return "None", False
    elif(function == "P" or function == "H"):
        for x in range(1,100):
            location = "Imgs/" + UserID + "/" + x + "vP.jpg"
            if(path.exists(location)):
                continue
            location = "Imgs/" + UserID + "/" + x + "vH.jpg"
            if(path.exists(location)):
                continue
            location = "Imgs/" + UserID + "/" + x + "v" + function + ".jpg"
            img.imwrite(location)
            add_image.add_img(location)
            return str(x);
    else:
        print("Invalid function")
        return "Invalid", False


def createID(packet):
    print("Creating ID")
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
    path = "Imgs/" + userID;
    os.mkdir(path);
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
        return userID, False
    else:
        profileInfo.write("\n" + userID + "," + firstName + "," + lastName + "," + "relation")
        return userID, False

    auth.close()
    profileInfo.close()

def parse(TXTdata, img = None):
    TXTdata = TXTdata[1:len(TXTdata)]
#   print(packet)
    keyWord = TXTdata.split(":")[0]
    if(keyWord == "auth"):
        TXTdata = TXTdata[len(keyWord) + 1 : len(TXTdata)]
        #print(len(keyWord))
        #print(len(packet))
        return auth(TXTdata, img)
    elif(keyWord == "createID"):
        return createID(TXTdata)
    else:
        print("Invalid Keyword")


def recieveTXTPacket(data):
    print(data);
    return parse(data)

def recieveIMGPacket(data, img):
    parse(data,img = img)

#Code Starts Here
net = ServerSockets.SocketHandler(recieveTXTPacket,recieveIMGPacket)
net.start_listeners()

while(True):
    pass


#inputpacket = input("Simulate an incoming packet ")
#if(inputpacket[0] == "{"):
#   print("Valid input")
#   parse(inputpacket)
#else:
#    print("Invalid input")