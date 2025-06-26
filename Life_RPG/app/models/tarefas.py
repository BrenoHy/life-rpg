class Tarefa:
    def __init__(self, nome, dificuldade, habilidade=None):
        # Tabelas de referência
        dificuldade_xp = {
            "fácil": 50,
            "média": 100,
            "difícil": 200
        }

        dificuldade_moedas = {
            "fácil": 10,
            "média": 20,
            "difícil": 40
        }

        # Atributos da tarefa
        self.nome = nome
        self.dificuldade = dificuldade.lower()
        self.xp = dificuldade_xp.get(self.dificuldade, 0)
        self.moedas = dificuldade_moedas.get(self.dificuldade, 0)
        self.habilidade = habilidade
        self.concluida = False

    def concluir(self):
        """
        Marca a tarefa como concluída, se ainda não tiver sido.
        """
        if self.concluida:
            print(f"A tarefa '{self.nome}' já foi concluída.")
        else:
            self.concluida = True
            print(f"Tarefa '{self.nome}' concluída com sucesso!")

    def __str__(self):
        """
        Mostra a tarefa de forma amigável ao usar print().
        """
        return (
            f"Tarefa(nome='{self.nome}', dificuldade='{self.dificuldade}', "
            f"xp={self.xp}, moedas={self.moedas}, habilidade={self.habilidade}, "
            f"concluida={self.concluida})"
        )
