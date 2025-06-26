from app.models.tarefas import Tarefa

def criar_tarefa(nome, dificuldade, habilidade=None):
    """
    Cria e retorna um objeto da classe Tarefa.
    """
    return Tarefa(nome, dificuldade, habilidade)