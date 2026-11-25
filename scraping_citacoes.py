import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

registos = []

try:
	resposta = requests.get(url, timeout=10)
	resposta.raise_for_status()
	soup = BeautifulSoup(resposta.text, "html.parser")
	for bloco in soup.find_all("div", class_="quote"):
		texto = bloco.select_one("span.text").get_text(strip=True)
		autor = bloco.select_one("small.author").get_text(strip=True)
		registos.append({"texto": texto, "autor": autor})
	print("Citações recolhidas:", len(registos))
	for registo in registos:
		print(registo["autor"], "-", registo["texto"])

except requests.exceptions.RequestException as erro:
 	print("Falha na consulta da página:", erro)


import csv

with open("citacoes.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
	escritor = csv.DictWriter(ficheiro, fieldnames=["texto", "autor"], delimiter=";")
	escritor.writeheader()
	escritor.writerows(registos)
print("CSV de citações criado")

# Opção B — Estatísticas de citações: apresentar o número de citações por autor, de forma organizada.

contagem_autores = {}

try:
    with open("citacoes.csv", mode="r", newline="", encoding="utf-8-sig") as ficheiro:
        leitor = csv.DictReader(ficheiro, delimiter=";")
        for linha in leitor:
            autor = (linha.get("autor") or "").strip()
            if autor:
                contagem_autores[autor] = contagem_autores.get(autor, 0) + 1

    print("\n--- Estatísticas de citações por autor ---")
    if not contagem_autores:
        print("Não foram encontradas citações no ficheiro.")
    else:
        for autor, total in sorted(contagem_autores.items(), key=lambda item: item[0].casefold()):
            print(f"{total} -> {autor}")

except FileNotFoundError:
    print(f"O ficheiro citacoes.csv não foi encontrado. Execute primeiro a recolha e exportação.")
