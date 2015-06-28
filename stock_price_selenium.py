#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import json
from urllib import quote


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
        driver = self.driver
        google_url = self._get_goog_url(page)
        driver.get(self.base_url + google_url)

        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]

        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('date')
        driver.find_element_by_css_selector('td.lm').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('a.kim-new-datatype'
                                            ).click()
        driver.find_element_by_id('kim-ToolbarDataName').click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('open')
        driver.find_element_by_css_selector('td.rgt').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('a.kim-new-datatype'
                                            ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('high')
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[3]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('a.kim-new-datatype'
                                            ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName').send_keys('low')
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[4]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('a.kim-new-datatype'
                                            ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('close')
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[5]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('a.kim-new-datatype'
                                            ).click()
        driver.find_element_by_id('kim-ToolbarDataName').click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('volume')
        driver.find_element_by_css_selector('td.rgt.rm').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_css_selector('div.SP_arrow_next').click()
        driver.find_element_by_id('kim-DoneButton').click()
        driver.find_element_by_id('kim-APIName').clear()
        driver.find_element_by_id('kim-APIName').send_keys('CARE-2')
        driver.find_element_by_xpath("//input[@value='Create API']"
                                     ).click()
        driver.find_element_by_xpath("//div[@id='kim-Large-Overlay']/button"
                                     ).click()

        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | _self | 30000]]

        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('date')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[2]"
                                     ).click()
        driver.find_element_by_id('kim-ToolbarDataName').click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('open')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[3]"
                                     ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('high')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[4]"
                                     ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName').send_keys('low')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[5]"
                                     ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('close')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[6]"
                                     ).click()
        driver.find_element_by_id('kim-ToolbarDataName').clear()
        driver.find_element_by_id('kim-ToolbarDataName'
                                  ).send_keys('volume')
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a/span"
                                     ).click()
        driver.find_element_by_css_selector('td.lm').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[2]/span"
                                     ).click()
        driver.find_element_by_css_selector('td.rgt').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[3]/span"
                                     ).click()
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[3]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[4]/span"
                                     ).click()
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[4]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[5]/span"
                                     ).click()
        driver.find_element_by_xpath("//table[@id='kim-normalized-table-3']/tbody/tr[2]/td[5]"
                                     ).click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_xpath("//div[@id='kim-Toolbar']/div[3]/a[6]/span"
                                     ).click()
        driver.find_element_by_css_selector('td.rgt.rm').click()
        driver.find_element_by_css_selector('a.kim-highlight-button.kim-accept-highlight'
                                            ).click()
        driver.find_element_by_id('kim-DoneButton').click()
        driver.find_element_by_id('kim-APIName').clear()
        driver.find_element_by_id('kim-APIName').send_keys('%s-%s' % (ticker_name, page))
        driver.find_element_by_xpath("//input[@value='Create API']"
                                     ).click()
        driver.find_element_by_xpath("//div[@id='kim-Large-Overlay']/button"
                                     ).click()


if __name__ == '__main__':
    with open('bom.json') as fd:
        json_text = fd.read()
    tickers = json.loads(json_text)
    for (ticker_key, val) in tickers.iteritems():
        x = StockPriceSelenium(val)
        for i in xrange(1, 3):
            x.test_stock_price_selenium(ticker_name=ticker_key, page=i)
