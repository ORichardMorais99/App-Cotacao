import requests

# importar o App, Builder (GUI)
#criar o nosso aplicativo
#criar a função build

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):

    def build(self):
        return GUI
    
    def on_start(self):
        cotacao_dolar = float(self.pegar_cotacao('USD'))
        cotacao_euro = float(self.pegar_cotacao('EUR'))
        cotacao_bitcoin = float(self.pegar_cotacao('BTC'))
        cotacao_etherum = float(self.pegar_cotacao('ETH'))
        self.root.ids["moeda1"].text = f"Dolár: R${round(cotacao_dolar, 2)}"
        self.root.ids["moeda2"].text = f"Euro: R${round(cotacao_euro, 2)}"
        self.root.ids["moeda3"].text = f"Bitcoin: R${round(cotacao_bitcoin, 2)}"
        self.root.ids["moeda4"].text = f"Etherum: R${round(cotacao_etherum, 2)}"

    def pegar_cotacao(self, moeda):
            link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
            return cotacao

MeuAplicativo().run()