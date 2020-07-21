from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def google(keyword):
    # google ile keyword araması yap
    profile = webdriver.FirefoxProfile()
    profile.native_events_enabled = True

    driver = webdriver.Firefox()
    searchEngineUrl = "http://google.com"

    # Firefox sayfasını aç ve google sitesine bağlan

    driver.get(searchEngineUrl)

    # Adı q alan html elemanı bul (arama kutusu)

    inputElement = driver.find_element_by_name("q")

    # keyword bilgisini arama kutusuna gir ve Return tuşuna tıkla

    inputElement.send_keys(keyword + Keys.RETURN)

    # Dikkat! incelemen bittiğinde sayfayı kapatmayı unutma!
    # Bu kod, sayfayı otomatik kapatmaz.
    # Otomatik kapanmasını isterseniz aşağıdaki iki satırın başındaki
    # işaretini kaldırn

    time.sleep(30)  # 30 saniye bekle
    driver.quit()  # sayfayı kapat


keyword = "Berk Batuhan ŞAKAR"

google(keyword)
