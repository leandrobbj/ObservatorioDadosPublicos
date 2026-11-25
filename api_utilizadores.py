import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
	resposta = requests.get(url, timeout=10)
	resposta.raise_for_status()
	utilizadores = resposta.json()
	print("Total de utilizadores:", len(utilizadores))
	for pessoa in utilizadores:
		print(pessoa["name"], "-", pessoa["email"])

except requests.exceptions.RequestException as erro:
 	print("Não foi possível consultar a API:", erro)

import csv

with open("utilizadores.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
	escritor = csv.DictWriter(ficheiro, fieldnames=["nome", "email"], delimiter=";")
	escritor.writeheader()
	for pessoa in utilizadores:
		escritor.writerow({"nome": pessoa["name"], "email": pessoa["email"]})
print("CSV de utilizadores criado")