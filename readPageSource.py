import urllib2 as url
from collections import Counter
thing= url.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

rareCount= Counter(thing).most_common()
print(rareCount)
