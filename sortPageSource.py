import urllib2 as url
import re
from collections import Counter
thing= url.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
comments= re.findall("<!--(.*?)-->",thing,re.DOTALL)
#print(comments)
data=comments[-1]
print(comments)

rareCount= Counter(thing).most_common()
#print(rareCount)
