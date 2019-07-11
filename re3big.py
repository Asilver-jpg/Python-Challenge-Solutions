import urllib2 as url
import re
thing= url.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
print(thing)
comments= re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+',thing)

result=''

for i in comments:
    for x in i:
        value = ord(x)
        if value >=97 and value<=122:
            result= result+x


print(result)
