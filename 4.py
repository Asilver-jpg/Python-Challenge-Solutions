import urllib2 as url
import re
thing= url.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read()
print(thing)
