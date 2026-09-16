import time
import os

with open("musica.txt", "r", encoding="utf-8") as file:
    for line in file:
        print([line.strip()])
        time.sleep(1)  # Adiciona um pequeno atraso entre as impressões
