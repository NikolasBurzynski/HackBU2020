import socket
import cv2


def get_response(to_send):
    s = socket.socket()
    s.connect(("149.125.138.215", 16505))
    s.send(to_send)
    print(s.recv(1024))
    s.close()


def submit_picture(uid, pwd, image):
    pass


def authenticate(uid, pwd):
    return True


def create_account(pwd, first_name, last_name):
    return True, "000000"


def get_info(uid, pwd, target_uid, var_name):
    if var_name == "first_name":
        return "Patricia"
    elif var_name == "last_name":
        return "Madmen"
    elif var_name == "rel_stat":
        return "Taken"
    else:
        return ""


def get_image(uid, pwd, target_uid, index):
    if 0 <= index <= 3:
        return True, cv2.imread(str(index) + ".jpg")
    else:
        return False, None


def get_complete_info(uid, pwd):
    first = get_info(uid, pwd, uid, "first_name")
    last = get_info(uid, pwd, uid, "last_name")
    status = get_info(uid, pwd, uid, "rel_stat")

    return last, first, status


def status_text_to_index(status):
    status = status.lower()
    if status == "single":
        return 0
    elif status == "taken":
        return 1
    elif status == "not looking":
        return 2