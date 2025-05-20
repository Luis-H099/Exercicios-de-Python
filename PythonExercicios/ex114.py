import urllib
import urllib.request

try:
    esc = str(input('Qual site você deseja acessar?: '))
    site = urllib.request.urlopen(f'http://www.{esc}.com.br')
except urllib.error.URLError:
    print(f'O site {esc} não está acessível no momento.')
else:
    print(f'Consegui acessar o site {esc} com sucesso!')
