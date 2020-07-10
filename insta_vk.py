
from pages import subscriber_page
from pages.vk_barkov import VkBarkov
import time
link = "https://www.instagram.com/kudesnitsa_art/"
link1 = "https://vk.barkov.net/instagramid.aspx"


def test_open_vk(browser):
    pag = subscriber_page.SubscriberPage(browser, link)
    pag.open()
    res = pag.go_tu_subscriber(browser)
    pag1 = VkBarkov(browser, link1)
    pag1.open()
    pag1.main_method(res, browser, link1, 0)
    time.sleep(10)



