""" Luta test entry module """
from luta.crawler import Crawler

URL1 = "http://www.sahibinden.com/telli-calgilar-muzik-aletleri?query_text_mf=fender+telecaster&query_text=fender+telecaster"

def test_single():
    crw = Crawler(URL1)

    prices = crw.get_values_between('<td class="searchResultsPriceValue">', '</div>')
    for price in prices:
        print(price)

    next_url = crw.get_last_value_between('<a href="', '" class="prevNextBut" title="Sonraki"')
    print(next_url)

def test_multi():
    loop_pos = 1
    url = URL1
    while True:
        print(f"Loop {str(loop_pos)}")
        crw = Crawler(url)

        prices = crw.get_values_between('<td class="searchResultsPriceValue">', '</div>')
        for price in prices:
            print(price)

        next_url = crw.get_last_value_between('<a href="', '" class="prevNextBut" title="Sonraki"')
        if next_url == "":
            return
        print(next_url)
        url = f"http://sahibinden.com{next_url}"
        loop_pos += 1

test_multi()