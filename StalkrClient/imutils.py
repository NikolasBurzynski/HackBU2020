import cv2


def scale_and_pad(img, scale=480):
    original_dims = img.shape[:2]
    ratio = float(scale) / max(original_dims)
    resized_dims = tuple([int(x * ratio) for x in original_dims])
    resized = cv2.resize(img, (resized_dims[1], resized_dims[0]))

    diff_wid = scale - resized_dims[1]
    diff_hgt = scale - resized_dims[0]
    t, b = diff_hgt // 2, diff_hgt - (diff_hgt // 2)
    l, r = diff_wid // 2, diff_wid - (diff_wid // 2)

    color = [255, 255, 255]
    resized = cv2.copyMakeBorder(resized, t, b, l, r, cv2.BORDER_CONSTANT, value=color)
    return resized
