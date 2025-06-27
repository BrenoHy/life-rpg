from datetime import datetime

def concluir_tarefa(personagem, tarefa):
    """
    Faz o personagem ganhar XP e moedas ao concluir uma tarefa.
    """
    if tarefa.concluida:
        print(f"A tarefa '{tarefa.nome}' já foi concluída.")
        return personagem, tarefa
    
    tarefa.concluir() # Marca como concluída

    personagem.ganhar_xp(tarefa.xp)
    personagem.ganhar_moedas(tarefa.moedas)

    if tarefa.habilidade:
        personagem.adicionar_habilidade(tarefa.habilidade, tarefa.xp)

    registro = {
        "nome": tarefa.nome,
        "categoria": tarefa.categoria,
        "habilidade": tarefa.habilidade,
        "xp_ganho": tarefa.xp,
        "moedas_ganhas": tarefa.moedas,
        "data_conclusao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    personagem.historico.append(registro)
    
    return personagem, tarefa