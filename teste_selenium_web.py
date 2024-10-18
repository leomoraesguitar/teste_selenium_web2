from selenuim_leo import SeleniumLeo, By
from time import sleep

s = SeleniumLeo(print)
# s.Abrir_site('https://www.tjse.jus.br/oficialjustica/paginas/movimentacaoMandado/movimentacaoMandado.tjse')
link = "https://www.tjse.jus.br/oficialjustica/paginas/movimentacaoMandado/movimentacaoMandado.tjse"
# self.pprint('Abrindo Portal do Oficial...')

s.Abrir_site(link)
# s.Aguardar = s.Aguardar2
while True:
    sleep(120)