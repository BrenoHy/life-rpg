from app.models.personagem_model_novo import PersonagemNovo

def criar_personagem(nome):
    """
    Cria e retorna um objeto da classe Personagem com nome personalizado.
    """
    return PersonagemNovo(nome)