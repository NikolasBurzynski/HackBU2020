import socket
import cv2
import numpy as np


def get_response(to_send):
    s = socket.socket()
    s.connect(("149.125.138.215", 16505))
    #s.connect(("127.0.0.1", 16505))
    s.send(to_send.encode("utf-8"))
    data = s.recv(1024)
    s.close()
    return data.decode("utf-8")


def get_response_image(to_send):
    s = socket.socket()
    s.connect(("149.125.138.215", 16505))
    #s.connect(("127.0.0.1", 16505))
    s.send(to_send.encode("utf-8"))
    data = s.recv(5000000)
    image = "none"
    if len(data) >= 4 and data[0:4] == b"IMG:":
        data = data[4:len(data)]
        data = np.fromstring(data, np.uint8)
        image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    s.close()
    return image


def submit_picture(uid, pwd, vis, image):
    s = socket.socket()
    s.connect(("149.125.138.215", 16505))
    if vis:
        vis = "P"
    else:
        vis = "H"
    header = ("{auth:" + uid + ":" + pwd + ":" + vis + ":IMG}").encode("utf-8")
    s.send(header + cv2.imencode('.jpg', image)[1].tostring())
    data = s.recv(1024).decode("utf-8")
    s.close()
    return data


def authenticate(uid, pwd):
    r = get_response("{auth:" + uid + ":" + pwd + ":login:none}")
    return r == "Allow"


def create_account(pwd, first_name, last_name):
    r = get_response("{createID:" + first_name + ":" + last_name + ":" + pwd + "}")
    return True, r


def get_info(uid, pwd, target_uid, var_name):
    return get_response("{auth:" + uid + ":" + pwd + ":get:" + var_name + "}")


def get_image(uid, pwd, target_uid, index):
    r = get_response_image("{auth:" + uid + ":" + pwd + ":i" + str(index) + ":" + target_uid + "}")
    if r != "none":
        print("got img")
        return True, r
    else:
        return False, r


def get_complete_info(uid, pwd):
    first = get_info(uid, pwd, uid, "First Name")
    last = get_info(uid, pwd, uid, "Last Name")
    status = get_info(uid, pwd, uid, "Status")

    return last, first, status


def set_status(uid, pwd, new):
    r = get_response("{auth:" + uid + ":" + pwd + ":set:" + new + "}")
    return r == new


def status_text_to_index(status):
    status = status.lower()
    if status == "single":
        return 0
    elif status == "taken":
        return 1
    elif status == "not looking":
        return 2