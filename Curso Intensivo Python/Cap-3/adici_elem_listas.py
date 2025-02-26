#O programa abaixo mostra como adicionar novos elementos a listas e como removelos dinamicamente
motos =['honda','ducati','yamaha']
print(motos)
motos.append('harley')# O novo item sempre será adicionado ao final da lista
print(motos)
motos.insert(0,'kawasaki')# Também podemos inserir um novo elemento a lista em qualquer posição utilizando o "insert"
print(motos)
del motos[1]
print(motos)# Também podemos remover qualquer elemento de uma lista com o "del" desde que saibamos a posição deste elemento
# Com o método "pop()" abaixo podemos remover um elemento da lista e ainda sim utilizar seu valor após removido da lista
motos_removida = motos.pop()# Podemos remover qualquer elemento da lista desde que saibamos a sua posição
print(motos)
print(motos_removida)
#Caso não saibamos a posição do eleemnto que desejamos remover, mas apenas o seu valor podemos utilizar o método "remove()" conforme abaixo
print(motos)
motos.remove('ducati')
print(motos)