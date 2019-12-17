from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def start_app():
    caps = {
        'platformName': 'android',
        'platformVersion': '7',
        'deviceName': 'caf146b4',
        'appPackage': 'com.smile.gifmaker',
        'appActivity': 'com.yxcorp.gifshow.HomeActivity',
        'automationName': 'uiautomator2',
        'noReset': 'True',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)


    try:
        # 用户隐私政策
        if WebDriverWait(driver, 3).until(lambda x:x.find_element_by_id("com.smile.gifmaker:id/positive")):
            driver.find_element_by_id("com.smile.gifmaker:id/positive").click()
        # 青少年模式，我知道了
        if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("com.smile.gifmaker:id/positive")):
            driver.find_element_by_id("com.smile.gifmaker:id/positive").click()
        # 大屏模式
        if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_id("com.smile.gifmaker:id/close")):
            driver.find_element_by_id("com.smile.gifmaker:id/close").click()
    except Exception as e:
        pass
    return driver

def publish():
    driver = start_app()
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.smile.gifmaker:id/right_btn']").click()
    sleep(2)
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.smile.gifmaker:id/button_album_frame']").click()
    sleep(1)
    driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@resource-id='com.smile.gifmaker:id/album_view_list']/android.widget.FrameLayout[4]/android.widget.ImageView[1]").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/next_step']").click()
    sleep(2)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/next_button']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/next_step_button']").click()
    sleep(3)
    driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.smile.gifmaker:id/right_radio_btn']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/publish_button']").click()
    sleep(1)
    try:
        while driver.find_element_by_xpath("//android.view.View[@resource-id='com.smile.gifmaker:id/player_sector_progress']"):
            sleep(10)
    except Exception as e:
        pass
    driver.close()


def shoot():
    driver = start_app()
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.smile.gifmaker:id/right_btn']").click()
    sleep(2)
    driver.tap([(445, 1542), (634, 1731)], 1000*15)
    if WebDriverWait(driver, 15).until(lambda x:x.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/next_step_button']")):
        driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/next_step_button']").click()
    sleep(2)
    driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id='com.smile.gifmaker:id/right_radio_btn']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.smile.gifmaker:id/publish_button']").click()
    sleep(1)
    try:
        while driver.find_element_by_xpath("//android.view.View[@resource-id='com.smile.gifmaker:id/player_sector_progress']"):
            sleep(10)
    except Exception as e:
        pass
    driver.close_app()


if __name__ == '__main__':
    shoot()