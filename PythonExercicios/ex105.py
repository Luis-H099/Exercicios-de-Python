def notas(* num, sit=False):
    """
       -> Função para analisar funções e situações de vários alunos.
       :param n: uma ou mais notas dos alunos (aceita várias).
       :param sit: opcional, indica se deve ou não adicionar a situação da turma.
       :param tab: opcional, indica se deve ou não mostrar os dados em forma de tabela.
       :return: dicionário e/ou tabela com os dados solicitados.
       """
    cont = maior = menor = soma = 0
    aluno = dict()
    aluno['Total'] = len(num)
    aluno['Maior'] = max(num)
    aluno['Menor'] = min(num)
    aluno['Media'] = sum(num)/len(num)
    if sit:
        if aluno['Media'] >= 7:
            aluno['situação'] = 'Aprovado'
        elif 6 < aluno['Media'] < 7:
            aluno['situação'] = 'Recuperação'
        else:
            aluno['situação'] = 'Reprovado'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
