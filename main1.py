# SNKRS Bot created by: Wenyu She

# Use Task Scheduler app to auto run this command through a batch file at 10am est:
# C:\Users\mail4\AppData\Local\Programs\Python\Python39\python.exe "C:\Users\mail4\PycharmProjects\SNKRS_bot\main1.py" pause

import time
from datetime import datetime
import webbrowser
from Nike_Bot.general_methods import login_SNKRS, SNKRS_notify
from Nike_Bot.general_methods import new_tab, find_tab, reload_page, next_tab, new_window, switch_window, close_tab, place_holder
from Nike_Bot.general_methods import find_and_click, find_image, wifi_on, captcha
import pyautogui
import screen_brightness_control as sbc


# replace settings:
buy = r"SNKRS_imgs\size_imgs\SNKRS_buy.png"
draw = r"SNKRS_imgs\SNKRS_draw.png"


profiles = 2
SNKRS_size = ["M 9", "M 8.5"]
SNKRS_size_image = [r"SNKRS_imgs\SNKRS_M9.png", r"SNKRS_imgs\SNKRS_M8.5.png"]
back_to = "SNKRS2"


# replace links
# Order: name of site, run method, link, other specific methods (find shoe, login, etc.)
site_resources = [
    ["SNKRS1", "https://www.nike.com/launch/t/sb-dunk-low-what-the-paul?cp=65052578087_search_%7Csnkrs%7Cg%7C11856077755%7C115377939556%7Ce%7Cc", SNKRS_notify],
    ["SNKRS2", "https://www.nike.com/launch/t/womens-air-jordan-og-coconut-milk?cp=65052578087_search_%7Csnkrs%7Cg%7C11856077755%7C115377939556%7Ce%7Cc", SNKRS_notify]
]


def open_links():
    for sites in site_resources:
        new_tab()
        pyautogui.write(sites[1])
        pyautogui.press("enter")
        for method in sites[2:]:
                method()
                time.sleep(1)
        if sites[0] == back_to:
            next_tab()
            close_tab()


def run_SNKRS():
    time.sleep(1)
    while True:
        if datetime.now().hour == 7:
            time.sleep(20)
            # iterating through the chrome profiles
            for run_num in range(profiles):
                if datetime.now().minute >= 9:
                    break
                # choosing the profile to run:
                pyautogui.click(find_image(r"chrome.png", .95))
                time.sleep(2)
                pyautogui.click(550 + (run_num % 4)*300, 450 + (int(run_num / 4))*300)
                time.sleep(2)
                # clicking shoe size:
                for shoe in range(len(SNKRS_size)):
                    pyautogui.moveTo(800, 500)
                    run = True
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    pyautogui.write(SNKRS_size[shoe])
                    time.sleep(1)
                    pyautogui.click(find_image(SNKRS_size_image[shoe], .8))
                    time.sleep(1)
                    pyautogui.press('esc')
                    if run:
                        run1 = True
                        while True:
                            if find_image(draw, .9) != None:
                                pyautogui.click(find_image(draw, .9))
                                time.sleep(4)
                                if find_image(r"SNKRS_imgs\SNKRS_draw_info.png", .9) != None:
                                    pyautogui.click(find_image(r"SNKRS_imgs\SNKRS_draw_info.png", .9))
                                    scrolls = 0
                                    while find_image(r"SNKRS_imgs\SNKRS_draw_ok.png", .95) == None:
                                        pyautogui.scroll(-500)
                                        scrolls += 1
                                        if scrolls == 4:
                                            run1 = False
                                            break
                                    pyautogui.click(find_image(r"SNKRS_imgs\SNKRS_draw_ok.png", .95))
                                    time.sleep(1)
                                    pyautogui.click(find_image(draw, .9))
                                break
                            elif find_image(buy, .9) != None:
                                pyautogui.click(find_image(buy, .9))
                                break
                            else:
                                pyautogui.scroll(-400)
                                time.sleep(0.2)
                        if run1:
                            click = find_and_click(r"SNKRS_imgs\SNKRS_security_code.png", .9, 6)
                            if click:
                                # Enter CVV:
                                pyautogui.write("   ")
                                pyautogui.click(find_image(r"SNKRS_imgs\SNKRS_save_payment.png", .9))
                            while find_image(r"SNKRS_imgs\SNKRS_submit_order.png", .9) == None:
                                pyautogui.scroll(-300)
                            pyautogui.click(find_image(r"SNKRS_imgs\SNKRS_submit_order.png", .9))
                            if find_image(r"SNKRS_imgs\SNKRS_draw_confirm.png", .95) != None:
                                pyautogui.click(find_image(r"SNKRS_imgs\SNKRS_draw_confirm.png", .95))
                    time.sleep(5)
                    next_tab()
            break


def main():
    sbc.set_brightness(0)
    wifi = wifi_on(0)
    if wifi:
        for i in range(profiles):
            pyautogui.click(find_image(r"chrome.png", .9))
            time.sleep(2)
            pyautogui.click(550 + (i % 4)*300, 450 + (int(i / 4))*300)
            open_links()


if __name__ == '__main__':
    main()
    run_SNKRS()

