import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_178812.json'
fh = urllib.request.urlopen(url)

data = json.loads(fh.read())




count = 0
comments_list = data['comments']
for i in comments_list:
    count += int(i['count'])


print('count:', count)

#
#
