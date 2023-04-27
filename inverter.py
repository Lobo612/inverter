def inverter():
    palavra = (input("Digite a palavra que deseja inverter: "))
    caracteres = list(palavra)
    tamanpala = len(palavra)

    for i in range(tamanpala // 2):
        vartemp = caracteres[i]
        caracteres[i] = caracteres[tamanpala - i - 1]
        caracteres[tamanpala - i - 1] = vartemp
    
    invertida = "".join(caracteres)
    print(invertida)

if __name__ == "__main__":
    inverter()