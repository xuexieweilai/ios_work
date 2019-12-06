from appium import webdriver


def start_tapp():
    caps = {
        'platformName': 'ios',
        'platformVersion': '10',
        'deviceName': '“纪淼”的 iPhone',
        'app': 'com.jiangjia.gif',
        'udid': 'xxxxxxxx',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)


if __name__ == '__main__':
    start_tapp()