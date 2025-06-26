import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

from app.services.personagem_service import criar_personagem
from app.services.tarefa_service import criar_tarefa
from app.controllers.game_controller import concluir_tarefa


# Criando personagem
personagem = criar_personagem("Keria")

# Criando tarefas
tarefa1 = criar_tarefa("Estudar programação", "média", habilidade="Programação")
tarefa2 = criar_tarefa("Estudar inglês", "fácil", habilidade="Inglês")

# Estado inicial
print("\n--- Estado inicial ---")
print(personagem)
print(tarefa1)

# Concluindo tarefa
personagem, tarefa1 = concluir_tarefa(personagem, tarefa1)

# Estado final
print("\n--- Após concluir tarefa ---")
print(personagem)
print(tarefa1)


