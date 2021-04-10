# Luta

Luta is a [Selenium](https://selenium-python.readthedocs.io) based web spider / scraper.

Luta assumes that you are a Mac user and your application is executed on the foreground. That enables Luta to access HTML pages over Safari, and bypass any scraper protection on the server side.

## Installation

```
pip install selenium
pip install git+https://github.com/keremkoseoglu/luta.git
```

## Configuration

On Safari, Develop - Allow Remote Automation should be enabled.

## Usage

Here is a simple usage example:
```
from luta.crawler import Crawler

crw = Crawler("www.mysite.com")

prices = crw.get_values_between('<td class="searchResultsPriceValue">', '</div>')
for price in prices:
    print(price)

next_url = crw.get_last_value_between('<a href="', '" class="prevNextBut" title="Next"')
print(next_url)
```

## Trivia
Luta means "Spider" in Sanskrit.