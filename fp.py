sdp = eval(input('Escreva um inteiro positivo: \n?'))
#onde sdp (soma de digitos pares) e o numero inteiro que vai ser avaliado
sol1 = 0 #a solucao, isto tem de ser zero no inicio para não intervinir na soma.

while sdp > 0:
    digito = sdp%10 
    sdp = sdp//10
    #o codigo assima e um que o professor deu na aula teorica que separa cada digito de um numero
    
    if ((digito%2) == 0):
        sol1 = sol1 + digito
        #no if assima restringes a adição dos digitos a so digitos que tem resto da divisão por dois igual a zero ou seja são pares
        
print ('A soma dos digitos pares e', sol1)
