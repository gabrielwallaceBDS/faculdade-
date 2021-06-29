# escopo é a propriedade que determina onde uma variavel pode ser utilizada dentro de um programa
#\\\\ESCOPO LOCAL \\\\\
# criado sempre que uma funcao é chamada 
# variaveis criadas, seja no campo de um parametro ou dentro do corpo da funcao, fazem parte do escopo local daquela funcao e sao chamadas de variaveis locais. essas variaveis so existem dentro daquela propria funcao
#\\\\\ ESCOPO GLOBAL\\\\\
#criado no programa principal
# variaveis globais pertencem a um escopo global e sao variaveis criadas dentro do programa principal. uma variavel global existe tambem em todas as funcoes invocadas ao longo do programa  


3 #\\\ESCOPO DE VARIAVEIS///
def comida():
  print(ovos)
# programa principal
ovos = 12
comida()

# outro exemplo 

def comida():
  ovos = 12
  bacon()
  print(ovos)

def bacon():
  ovos = 6

# programa principal
comida()

# exemplo 3

def comida():
  ovos = 'variavel local de comida'
  print(ovos)

def bacon():
  ovos = 'variavel local bacon'
  print(ovos)
  comida()
  print(ovos)

#programa principal
ovos = 'variavel global'
bacon()
print(ovos)


#\\\GLOBAL///
# forca nosso programa a nao criar uma variavel local de mesmo nome e manipular somente a global dentro de uma funcao 
 
def comida():
  global ovos
  ovos = 'comida'
#programa principal 
ovos = 'global'
comida()
print(ovos)

