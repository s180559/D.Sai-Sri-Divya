a='<html><head>......</head><body>hello......<a href="www.rgukt.ac.com"></body></html>'
s=a.find('<a href')
e=a.find('"')
link=a[s:e]
print(link)
         
