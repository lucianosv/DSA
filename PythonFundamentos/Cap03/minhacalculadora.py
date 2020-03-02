#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Função calculadora
def calc(operacao, priNum, segNum):
    
    if operacao == 1:
        resultado = int(priNum) + int(segNum)
        descOpe   = 'Soma = '
    elif operacao == 2:
        resultado = int(priNum) - int(segNum)
        descOpe   = 'Subtração = '       
    elif operacao == 3:
        resultado = int(priNum) * int(segNum)
        descOpe   = 'Multiplicação = '       
    else:
        resultado = int(priNum) / int(segNum)
        descOpe   = 'Divisão = '
    retorno = descOpe + str(resultado)
        
    return(retorno)


# In[2]:


### Tela para entrada de dados
print("***************  Minha Calculadora Python  ***************")
print("")
print("\nSelecione o número da operação desejada:\n")
print("")
print("1-Soma")
print("2-Subtração")
print("3-Multiplicação")
print("4-Divisão")
print("")
print("")
operacao = input("\nDigite sua opção(1/2/3/4):\n")
print("")
priNum = input("\nDigite o primeiro número:\n")
print("")
segNum = input("\nDigite o segundo número:\n")
print("")


# In[3]:


# Validação dos dados de entrada e chamada da função calc
if operacao.isalnum():
    if int(operacao) <= 0 or int(operacao) >= 5:
        print("Operação inválida")
    else:
        if priNum.isalnum():
            if segNum.isalnum():
                Resultado = calc(operacao, priNum, segNum)
                print(Resultado)   
            else:
                print("Segundo argumento não numérico.") 
        else:                
            print("Primeiro argumento não numérico.")   
else:
    print("Operação digitada não numérica.")

