import json
import numpy as np
import sys
import rich

if len(sys.argv) < 4:
    raise ValueError("Número de argumentos menor que 4")
    exit()

try:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        file = json.load(file)
except FileNotFoundError:
    raise FileNotFoundError(f"Arquivo JSON --> {sys.argv[1]} base inválido!")
    exit()

nomes = sys.argv[2:]
num_parts = len(nomes)

split_list = np.array_split(file, num_parts)

for index in range(num_parts):
    with open(f"{nomes[index]}.json", "w", encoding="utf-8") as file_out:
        json.dump(
            split_list[index].tolist(), file_out, indent=2, ensure_ascii=False
        )

rich.print(
    f"\n:tada: Arquivo '{sys.argv[1]}' dividido em {num_parts} partes:\n"
)
for nome in nomes:
    rich.print(f">>> [bold]./{nome}.json[/bold]")
