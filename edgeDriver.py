import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By

from fp.fp import FreeProxy
from fake_headers import Headers


def get_driver(proxy=False):

    options=webdriver.ChromeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument(f"user-agent={get_headers()}")

    if proxy:
        options.add_argument(
            '--proxy-server=%s' % FreeProxy(country_id=['BR']).get().split('//')[-1]
        )

    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    ) 
    return driver


def get_headers():
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="linux",  # Generate only Windows platform
        headers=False # generate misc headers
    )
    return header.generate()['User-Agent']


def check_proxy(driver):
    
    driver.get('http://www.whatismyproxy.com/')
    proxy_check = driver.find_element(By.XPATH, '//div[@class="information"]')
    
    print(proxy_check.text)


def main():

    driver = get_driver(proxy=True)

    try:
        check_proxy(driver)
        print("\_ That`s it _/")

    except Exception:
        print(traceback.format_exc())

    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()