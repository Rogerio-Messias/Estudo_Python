palavra = "garrafas"
for quantd_cerveja in range(99, 0, -1):
    print(quantd_cerveja, palavra, "de cerveja sobre o muro.")
    print(quantd_cerveja, palavra, "de cerveja.")
    print("Se derrubar uma.")
    print("Passe ao redor.")
    if quantd_cerveja == 1:
        print("Nao ha mais garrafas de cerveja no muro.")
    else:
        new_num = quantd_cerveja - 1
        if new_num == 1:
            palavra = "garrafa"
        print(new_num, palavra, "de cerveja sobre o muro.")
    print()