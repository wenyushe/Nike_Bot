import pyautogui
import time
import webbrowser
from datetime import datetime


def find_image(target, conf):
    coordinates = None
    count = 0
    while coordinates == None and count < 8:
        coordinates = pyautogui.locateCenterOnScreen(target, grayscale=True, confidence=conf)
        count += 1
    return coordinates


def wifi_on(tries):
    tries += 1
    if find_image(r"C:\Users\mail4\PycharmProjects\wifi\no_wifi.png", .9) != None:
        pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\wifi\no_wifi.png", .9))
        time.sleep(2)
        if find_image(r"C:\Users\mail4\PycharmProjects\wifi\disconnect_wifi.png", .8) != None:
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\wifi\diconnect_wifi.png", .8))
            time.sleep(2)
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\wifi\connect_wifi.png", .7))
        elif find_image(r"C:\Users\mail4\PycharmProjects\wifi\deco.png", .8) != None:
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\wifi\deco.png", .8))
            time.sleep(2)
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\wifi\connect_wifi.png", .8))
        pyautogui.click(1100, 200)
        time.sleep(10)
        if find_image(r"C:\Users\mail4\PycharmProjects\wifi\no_wifi.png", .9) != None:
            if tries != 3:
                wifi_on(tries)
            else:
                return False
        else:
            return True
    else:
        return True


def captcha():
    if find_image(r"C:\Users\mail4\PycharmProjects\Bodega_Bot\captcha_solver.png", 0.7) != None:
        time.sleep(1)
        pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\Bodega_Bot\captcha_solver.png", 0.7))
        pyautogui.scroll(150)
        time.sleep(2)
        redo = 0
        while find_image(r"C:\Users\mail4\PycharmProjects\Bodega_Bot\captcha_solver.png", 0.7) != None:
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\Bodega_Bot\redo_captcha.png", 0.7))
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\Bodega_Bot\captcha_solver.png", 0.7))
            time.sleep(3)
            redo += 1
            if redo == 5:
                break


def login_SNKRS():
    time.sleep(10)
    if find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_login.png", .95) != None:
        pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_login.png", .9))
        time.sleep(1)
        if find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_email.png", .95) != None:
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_email.png", .9))
            # Enter email:
            pyautogui.write("")
            pyautogui.press("tab")
            time.sleep(0.5)
            # Enter password:
            pyautogui.write("")
            pyautogui.click(find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_signin.png", .9))


def SNKRS_notify():
    pyautogui.moveTo(500, 500)
    time.sleep(2)
    scrolls = 0
    while find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_notify.png", .9) == None:
        if find_image(r"C:\Users\mail4\PycharmProjects\SNKRS_bot\SNKRS\SNKRS_notify1.png", .9) != None:
            break
        pyautogui.scroll(-500)
        scrolls += 1
        if scrolls == 10:
            break
    time.sleep(2)
    pyautogui.scroll(600)


def find_and_click(image, conf, seconds):
    x = 0
    click = True
    while find_image(image, conf) == None:
        x += 1
        if x >= seconds:
            click = False
            break
    if click:
        pyautogui.click(find_image(image, conf))
    return click


def new_tab():
    pyautogui.keyDown("ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("ctrl")


def find_tab(img):
    pyautogui.keyDown("ctrl")
    while find_image(img, .9) == None:
        pyautogui.press("tab")
    pyautogui.keyUp("ctrl")


def next_tab():
    pyautogui.keyDown("ctrl")
    pyautogui.press("tab")
    pyautogui.keyUp("ctrl")


def reload_page():
    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")


def new_window():
    pyautogui.keyDown("ctrl")
    pyautogui.press("n")
    pyautogui.keyUp("ctrl")


def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")


def close_tab():
    pyautogui.keyDown("ctrl")
    pyautogui.press("w")
    pyautogui.keyUp("ctrl")


def place_holder():
    print()
