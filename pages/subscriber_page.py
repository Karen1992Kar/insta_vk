
from pages.base_page import BasePage
from .locators import Subscriber, Fb, Save, User
import time
tryTime = 2


class SubscriberPage(BasePage, User):

    def go_tu_subscriber(self, browser):
        arr = []
        self.browser.find_element(*Subscriber.SUBSCRIBER).click()
        time.sleep(1)
        self.browser.find_element(*Fb.LOGIN).send_keys('+995579909741')
        self.browser.find_element(*Fb.PASSWORD).send_keys('+995579909741gago')
        self.browser.find_element(*Fb.BUTTON).click()
        time.sleep(4)
        self.browser.find_element(*Save.SAVE).click()
        time.sleep(tryTime)
        self.browser.find_element(*Subscriber.SUBSCRIBER).click()
        time.sleep(tryTime)
        fBody = browser.find_element(*User.FBODY)
        scroll = 0
        try:
            while scroll < 9:  # scroll 5 times
                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                time.sleep(1)
                scroll += 1
        except:
            print("vay qu ara")
        fList = browser.find_elements(*User.FLIST)
        for i in fList:
            arr.append(i.text)
        return arr
