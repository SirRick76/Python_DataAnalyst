'''
Módulo: funcoes_aluno
Descrição: Contém funções para recolher informações sobre os alunos, calcular a média das notas e determinar a sua classificação

Funções:
    mediaAluno(): Calcula a média das 3 notas de um aluno.
    classificacaoAluno(): Determina a classificação do aluno com base na sua média.
    pedido_informacoes_aluno(): Recolhe o nome e as 3 notas do aluno.
'''

def mediaAluno(nota1,nota2,nota3):
        '''
        Calcula a média das 3 notas de um aluno.

        Args:
            nota1 (float): A primeira nota do aluno.
            nota2 (float): A segunda nota do aluno.
            nota3 (float): A terceira nota do aluno.

        Returns:
            float: A média das 3 notas do aluno.

        '''
        media=(nota1+nota2+nota3)/3
        return media

def classificacaoAluno(media):
    '''
    Determina a classificação do aluno com base na sua média.

    Args:
        media (float): A média das notas do aluno.

    Returns:
        str: A classificação do aluno ("Aprovado" ou "Reprovado").

    '''
    if media>=10:
        return "Aprovado"
    else:
        return "Reprovado"

def pedido_informacoes_aluno():
    '''
    Solicita ao utilizador o nome e as 3 notas do aluno, garantindo que as notas estão no intervalo válido (0 a 20).

    Args:
        Nao recebe argumentos.

        Returns:
        tupple: Uma tupla contendo o nome do aluno e as 3 notas (nome, nota1, nota2, nota3).    

    '''
    
    nome=str(input("Insira o nome do aluno: "))
    while True:
        nota1= float(input("Insira a primeira nota: "))
        if 0 <= nota1 <= 20:
            break  
        print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")
    while True:
        nota2= float(input("Insira a segunda nota: "))
        if 0 <= nota2 <= 20:
            break  
        print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")
    while True:
        nota3= float(input("Insira a terceira nota: "))
        if 0 <= nota3 <= 20:
            break  
        print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")
    return nome, nota1, nota2, nota3