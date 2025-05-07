import requests
from pprint import pprint

nome = input("Digite um nome para pesquisa:\n")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

params = {
  "localidade": 33 #RJ
}

response = requests.get(url, params=params)Brun
try:
  response.raise_for_status()
except requests.HTTPError as e:
  print(f"Erro no request: {e}")
  resultado = None
else:
  resultado = response.json()
  pprint(resultado[0]["res"])
