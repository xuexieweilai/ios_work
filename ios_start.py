from appium import webdriver


def start_tapp():
    caps = {
        'platformName': 'ios',
        'platformVersion': '10',
        'deviceName': 'xxx',
        'app': 'com.jiangjia.gif',
        'udid': '9380f2f029afff8b022165223d2b40dc7966acc6',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)


if __name__ == '__main__':
    start_tapp()