import funcoes_aluno 


'''
help(funcoes_aluno.mediaAluno)
'''

nome, nota1, nota2, nota3 = funcoes_aluno.pedido_informacoes_aluno()
media_Final = funcoes_aluno.mediaAluno(nota1, nota2, nota3)
classificacao = funcoes_aluno.classificacaoAluno(media_Final)

print(f"O aluno {nome}  tem {media_Final:.2f}  de media e encontra-se {classificacao}")
