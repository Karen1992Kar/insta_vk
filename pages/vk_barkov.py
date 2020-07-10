
from .base_page import BasePage
from .locators import Conversion
import time, os
from selenium.webdriver.common.keys import Keys


class VkBarkov(BasePage):

    def conversion(self, users, browser):
        if not self.is_element_present(*Conversion.LI_USER):
            self.browser.find_element(*Conversion.SUBMIT_VK).click()
            self.browser.find_element(*Conversion.VK_LOGIN).send_keys("+995579909741")
            self.browser.find_element(*Conversion.VK_PASSWORD).send_keys("kar1992marg")
            self.browser.find_element(*Conversion.VK_SUBMIT).click()
            browser.execute_script("window.history.go(-2)")
        time.sleep(3)

        for i in range(len(users)):
            self.browser.find_element(*Conversion.TEXT_AREA).send_keys(users[i])
            self.browser.find_element(*Conversion.TEXT_AREA).send_keys(Keys.RETURN)
        self.browser.find_element(*Conversion.SUBMIT_INSTA).click()
        time.sleep(15)
        self.browser.find_element(*Conversion.DOWN_RES).click()
        time.sleep(5)

    def file_handling(self):
        path = 'C:\\Users\\Karen\\Desktop\\insta_vk\\pages'
        os.remove(path+'\\insta.txt')
        files = os.listdir(path)
        files = [os.path.join(path, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]
        directory = max(files, key=os.path.getctime)

        os.rename(directory, 'pages\\insta.txt')
        self.directory = path + "\\insta.txt"

        with open(self.directory, "r", encoding='utf-8') as fp:
            lines = [line.rstrip() for line in fp.readlines()]
        fp.close()
        print(lines)
        if not lines[0].isdigit():
            if lines[0][:17] != "https://vk.com/id":
                lines = lines[7:]
        if lines[0][:17] != "https://vk.com/id":
            file1 = open(self.directory, "w", encoding='utf-8')
            for line in lines:
                file1.write("https://vk.com/id" + line + "\n")
            file1.close()

    def get_file(self, con):
        time.sleep(1)
        self.browser.find_element(*Conversion.SHOW_PHONES).click()
        time.sleep(2)
        self.browser.find_element(*Conversion.MOBILE_PONES).click()
        time.sleep(2)
        self.browser.find_element(*Conversion.RADIO_CLICK_IN_ID).click()
        time.sleep(2)
        self.browser.find_element(*Conversion.DOWNLOAD_FILE).send_keys(self.directory)
        time.sleep(2)
        self.browser.find_element(*Conversion.SUBMIT_MODULE_PHONES).click()
        time.sleep(3)
        print(self.is_element_present(*Conversion.MODAL_DIALOG))
        if con < 1:
            self.browser.find_element(*Conversion.MODAL_DIALOG).click()
            time.sleep(2)
            self.browser.find_element(*Conversion.RADIO_CLICK_IN_ID).click()
            time.sleep(2)
            self.browser.find_element(*Conversion.DOWNLOAD_FILE).send_keys(self.directory)
            time.sleep(2)
            self.browser.find_element(*Conversion.SUBMIT_MODULE_PHONES).click()
        time.sleep(3)
        result = self.is_element_present(*Conversion.VISUAL_MODAL)
        if result:
            self.browser.find_element(*Conversion.VISUAL_MODAL).click()

    def main_method(self, users, browser, url, con):
        if len(users) < 8:
            return
        user = users[-8:]
        self.conversion(user, browser)
        self.file_handling()
        self.get_file(con)
        pag = BasePage(browser, url)
        pag.open()
        con += 1
        time.sleep(1)
        self.main_method(users[:-8], browser, url, con)







# with open('C:\\Users\\Karen\\Desktop\\insta_vk\\pages\\insta.txt', "r", encoding='utf-8') as fp:
#     lines = [line.rstrip() for line in fp.readlines()]
#     fp.close()
# print(lines)
#
# file1 = open('C:\\Users\\Karen\\Desktop\\insta_vk\\pages\\insta.txt', "w", encoding='utf-8')
# for line in lines:
#     file1.write("https://vk.com/id" + line + "\n")
# file1.close()
# with open('C:\\Users\\Karen\\Desktop\\insta_vk\\pages\\insta.txt', "r", encoding='utf-8') as fp:
#     lines = [line.rstrip() for line in fp.readlines()]
#     print(lines)
