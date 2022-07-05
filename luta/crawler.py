""" Crawler module """
from typing import List
from selenium import webdriver
from luta import text_finder

class Crawler():
    """ Crawler class """
    def __init__(self, url: str, wait_element: str = ""):
        self._url = url
        self._wait_element = wait_element
        self._html = ""
        self._call_url()

    @property
    def url(self) -> str:
        """ Passed URL """
        return self._url

    @property
    def html(self) -> str:
        """ HTML of URL """
        return self._html

    def get_values_between(self, first: str, last: str) -> List[str]:
        """ Returns values between given tags """
        result = []
        remain_html = self._html
        while True:
            find_result = text_finder.find_between(remain_html, first, last)
            if not find_result.found:
                return result
            result.append(find_result.clean_value)
            remain_html = remain_html[find_result.end:]

    def get_value_between(self, first: str, last: str) -> str:
        """ Returns value between given tags """
        result = text_finder.find_between(self._html, first, last)
        return result.clean_value    

    def get_last_value_between(self, first: str, last: str) -> str:
        """ Returns last value between given tags """
        results = []
        remain_html = self._html
        loop = True
        while loop:
            find_result = text_finder.find_between(remain_html, first, last)
            if find_result.found:
                results.append(find_result.clean_value)
                remain_html = remain_html[find_result.start+1:]
            else:
                loop = False
        result_count = len(results)
        if result_count <= 0:
            return ""
        return results[result_count-1]


    def _call_url(self):
        browser = webdriver.Safari(executable_path="/usr/bin/safaridriver")
        browser.get(self._url)
        self._html = browser.page_source
        browser.quit()
