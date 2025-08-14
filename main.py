
def soma(a,b):
    resultado = a + b;
    print(f"a soma dos valores é {resultado}");
   
#soma(a,b);

def div(a,b):
    resultado = a/b;
    print(f'a divisão dos valores é {resultado}');

#div(a,b);

def mult(a,b):
    resultado = a*b;
    print(f'a multiplicação dos valores é {resultado}');

#mult(a,b);

def subt(a,b):
    resultado = a-b;
    print(f'a subtração dos valores é {resultado}');

#subt(a,b);

a = int(input("escolha um numero: "));
b = int(input("escolha outro numero: "));

escolha = int(input("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n Escolha a formula: "));
if escolha == 1: 
    soma(a,b);
elif escolha == 2: 
    subt(a,b);
elif escolha == 3:
    mult(a,b);
elif escolha == 4:
    div(a,b);
else: 
    print("escolha inexistente, tente novamente");
    exit();

