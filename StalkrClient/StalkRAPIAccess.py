import socket
import cv2


def get_response(to_send):
    s = socket.socket()
    s.connect(("149.125.138.215", 16505))
    #s.connect(("127.0.0.1", 16505))
    s.send(to_send.encode("utf-8"))
    data = s.recv(1024)
    s.close()
    return data.decode("utf-8")


def submit_picture(uid, pwd, image):
    s = socket.socket()
    s.connect(("127.0.0.1", 16505))
    header = ("{auth:" + uid + ":" + pwd + ":IMG}").encode("utf-8")
    s.send(header + cv2.imencode('.jpg', image)[1].tostring())
    print(s.recv(1024))
    s.close()


def authenticate(uid, pwd):
    r = get_response("{auth:" + uid + ":" + pwd + ":login:none}")
    return r == "Allow"


def create_account(pwd, first_name, last_name):
    r = get_response("{createID:" + first_name + ":" + last_name + ":" + pwd + "}")
    return True, r


def get_info(uid, pwd, target_uid, var_name):
    return get_response("{auth:" + uid + ":" + pwd + ":get:" + var_name + "}")


def get_image(uid, pwd, target_uid, index):
    if 0 <= index <= 3:
        return True, cv2.imread(str(index) + ".jpg")
    else:
        return False, None


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