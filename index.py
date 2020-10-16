#import bibliotecas necessárias
import oauth2
import json
import time

#chaves e tokens fornecidos pelo twitter necessários para usar sua API
chave_key= 'INSIRA SUA KEY'
chave_key_secret='INSIRA SUA KEY SECRET'
token= 'INSIRA SEU TOKEN'
token_secret= 'INSIRA SEU TOKEN SECRET'
#autenticando tokens e chaves
consumer= oauth2.Consumer(chave_key, chave_key_secret)
token_key = oauth2.Token(token, token_secret)
cliente= oauth2.Client(consumer,token_key)

#function que conversa com API e rettwita o que desejar
def retwitar(nome,cliente):
    while True:
        requisicao= cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+nome+'&count=4')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        idd=(objeto['statuses'][0]['id'])
        time.sleep(4)
        idd= str(idd)
        requisicao= cliente.request('https://api.twitter.com/1.1/statuses/retweet/'+idd+'.json', method='POST')

#Ao digitar o nome, a conta do usuários fará retweet em todos os tweets que conter a palavra escolhida
nome= input()
retwitar(nome,cliente)



