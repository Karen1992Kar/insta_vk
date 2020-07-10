
from selenium.webdriver.common.by import By


class Subscriber:
    SUBSCRIBER = (By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')


class Save:
    SAVE = (By.CSS_SELECTOR, "#react-root > section > main > div > div > div > section > div > button")


class Fb:
    FB = (By.CSS_SELECTOR, "body>div.RnEpo._Yhr4>div.pbNvD.fPMEg._8PWHW>div>div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > "
                           "div > div > div.gr27e.o7laV > div > form > div:nth-child(6) > button")

    LOGIN = (By.CSS_SELECTOR, "body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > "
                              "div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > "
                              "div:nth-child(2) > div > label > input")

    PASSWORD = (By.CSS_SELECTOR, 'body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > '
                                 'div > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > '
                                 'form > div:nth-child(3) > div > label > input')

    BUTTON = (By.CSS_SELECTOR, "body > div.RnEpo._Yhr4 > div.pbNvD.fPMEg._8PWHW > div > "
                               "div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.lDRO1 > div > div > div.gr27e.o7laV > div > form > "
                               "div:nth-child(4) > button")


class User:
    FBODY = (By.XPATH, "//div[@class='isgrP']")
    FLIST = (By.XPATH, "//div[@class='isgrP']//li//a[@class='FPmhX notranslate  _0imsa ']")


class Conversion:

    LI_USER = (By.CSS_SELECTOR, "#ctl00_liUser")
    TEXT_AREA = (By.CSS_SELECTOR, "#instaLoginsList")
    SUBMIT_INSTA = (By.CSS_SELECTOR, "#submitInsta")
    SUBMIT_VK = (By.CSS_SELECTOR, "#ctl00_liWelcome > a")
    VK_LOGIN = (By.CSS_SELECTOR, "#login_submit > div > div > input:nth-child(7)")
    VK_PASSWORD = (By.CSS_SELECTOR, "#login_submit > div > div > input:nth-child(9)")
    VK_SUBMIT = (By.CSS_SELECTOR, "#install_allow")
    DOWN_RES = (By.CSS_SELECTOR, "#downloadArea > div.content > button")
    SHOW_PHONES = (By.CSS_SELECTOR, "#sidebar-menu > div > div.vk.active > ul > li:nth-child(21)")
    MOBILE_PONES = (By.CSS_SELECTOR, "#sidebar-menu > div > div.vk.active > ul > li.active > ul > li:nth-child(1) a")
    RADIO_CLICK_IN_ID = (By.CSS_SELECTOR, "#usersTab2")
    SELECTED_USER_LIST = (By.CSS_SELECTOR, "#selectedUsersList")
    VISUAL_MODAL = (By.CSS_SELECTOR, "#visualBody > div:nth-child(4) > span > a")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "#massUploadFile")
    SUBMIT_MODULE_PHONES = (By.CSS_SELECTOR, "#submitMobilePhones")
    VISUAL_HEADR = (By.CSS_SELECTOR, "#visualBody > div.visualHeader > div.download > a:nth-child(9)")
    MODAL_DIALOG = (By.CSS_SELECTOR, '#cloudAccessWindow > div > div > div.modal-body > p:nth-child(5) > a')


