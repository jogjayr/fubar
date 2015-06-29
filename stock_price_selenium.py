#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import json
from urllib import quote
import time


class StockPriceSelenium(object):

    def __init__(self, ticker):
        self.driver = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile('/Users/jayraj/Desktop/selenium-ff/'))
        self.driver.implicitly_wait(30)
        self.base_url = 'https://www.kimonolabs.com/load?url='
        self.verificationErrors = []
        self.accept_next_alert = True
        self.ticker = ticker

    def _get_goog_url(self, page=1):
        if page == 1:
            return quote('https://www.google.com/finance/historical?q=%s&startdate=Jan+1,+2014&enddate=Dec+31,+2014&num=300'
                         % self.ticker)
        else:
            return quote('https://www.google.com/finance/historical?q=%s&startdate=Jan+1,+2014&enddate=Dec+31,+2014&num=300&start=200'
                         % self.ticker)

    def test_stock_price_selenium(self, ticker_name, page=1):
        SLEEP_TIME = 0.5
        driver = self.driver
        google_url = self._get_goog_url(page)
        driver.get(self.base_url + google_url)

        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("date")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("td.lm").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[1]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("a.kim-new-datatype").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("open")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("td.rgt").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[2]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("a.kim-new-datatype").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("high")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[3]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("a.kim-new-datatype").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("low")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[4]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("a.kim-new-datatype").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("close")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[5]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("a.kim-new-datatype").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-ToolbarDataName").send_keys("volume")
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[6]").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_css_selector("[kimonotier= '1'] a.kim-highlight-button.kim-accept-highlight:first-of-type").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-DoneButton").click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-APIName").clear()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_id("kim-APIName").send_keys("%s-%s" % (ticker_name, page))
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//input[@value='Create API']"
                                     ).click()
        time.sleep(SLEEP_TIME)
        driver.find_element_by_xpath("//div[@id='kim-Large-Overlay']/button"
                                     ).click()
        time.sleep(20)

if __name__ == '__main__':
    with open('bom.json') as fd:
        json_text = fd.read()
    tickers = json.loads(json_text)
    for (ticker_key, val) in tickers.iteritems():
        x = StockPriceSelenium(val)
        for i in xrange(1, 3):
            x.test_stock_price_selenium(ticker_name=ticker_key, page=i)
