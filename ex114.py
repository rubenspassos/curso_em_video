import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim não estão acessível no momento')
else:
    print('Tudo Ok')