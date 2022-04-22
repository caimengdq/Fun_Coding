from selenium import webdriver
import time

s = ShoesBot(url)


class ShoesBot:

    def __init__(self, shoes_url):
        self.shoes_url = shoes_url
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def get_price(self):
        self.driver.get(self.shoes_url)
        price = self.driver.find_element_by_xpath('//div[@data-test="product-price"]')
        return int(price.get_attribute('innerHTML').strip('€'))

def main():
    url = "https://www.nike.com/fr/t/chaussures-de-running-sur-route-air-zoom-alphafly-next-flyknit-pour-N91wzC/DJ5456-100"
    bot = ShoesBot(url)

    last_price = None
    while 1:
        price = bot.get_price()
        if last_price:
            if price < last_price:
                print(f"Price dropped: {last_price - price}")
            elif price > last_price:
                print(f"Price increased by: {price - last_price}")
            else:
                print(f"Price stayed: {price}")
        last_price = price
        time.sleep(3) #every 3 seconds

if __name__ == "__main__":
    main()