# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")


print("1) Soma\n2) Subtração\n3) Multiplicação\n4) Divisão\n ")

p = input('Informe qual operação deseja realizar: ')
i = int(p)

v1 = int(input('Informe o primeiro número: '))
v2 = int(input('Informe o segundo número: '))


def soma(s1,s2):
    rsoma = s1 + s2
    print(f'Resultado da operação {s1} + {s2} = {rsoma}')

def subt(t1,t2):
    rsubt = t1 - t2
    print(f'Resultado da operação {t1} - {t2} = {rsubt}')

def mult(m1,m2):
    rmult = m1 * m2
    print(f'Resultado da operação {m1} x {m2} = {rmult}')

def divis(d1,d2):
    rdivis = d1 / d2
    print(f'Resultado da operação {d1} / {d2} = {rdivis}')

if i == 1:
    soma(v1,v2)
elif i == 2:
    subt(v1,v2)
elif i == 3:
    mult(v1,v2)
elif i == 4:
    divis(v1,v2)
else:
    print("Não foi ecolhido uma das possibilidades ?")
