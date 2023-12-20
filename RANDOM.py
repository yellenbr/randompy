import random

def gerar_num_aleatorio():
    num_aleatorio = random.randint(1, 100)
    return num_aleatorio

num_aleatorio = gerar_num_aleatorio()

print("Número aleatório gerado:", num_aleatorio)
