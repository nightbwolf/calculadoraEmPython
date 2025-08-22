#soma(a,b):

def soma(a,b):
    resultado = a + b;
    print(f"a soma dos valores é {resultado}");
   
#div(a,b);

def div(a,b):
    resultado = a/b;
    print(f'a divisão dos valores é {resultado}');

#mult(a,b):

def mult(a,b):
    resultado = a*b;
    print(f'a multiplicação dos valores é {resultado}');

#subt(a,b):

def subt(a,b):
    resultado = a-b;
    print(f'a subtração dos valores é {resultado}');

#media
def media(a,b,c,d):
    resultado = (a+b+c+d)/4
    print(f'o Resultado da média dos valores é {resultado}');
#Escolher numeros para operação:

a = int(input("escolha um numero: "));
b = int(input("escolha outro numero: "));

#Realizar Operação:

escolha = int(input("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - média\n Escolha a formula: "));
if escolha == 1: 
    soma(a,b);
elif escolha == 2: 
    subt(a,b);
elif escolha == 3:
    mult(a,b);
elif escolha == 4:
    div(a,b);
elif escolha == 5: #implementa uma função de média colocando mais duas variáveis no código, pode ser usada para avaliar alunos - roberto
    c = int(input("escolha o terceiro numero:"));
    d = int(input("escolha o ultimo numero:"));
    media(a,b,c,d);
else: 
    print("escolha inexistente, tente novamente");
    exit();