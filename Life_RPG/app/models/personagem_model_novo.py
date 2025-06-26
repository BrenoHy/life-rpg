class PersonagemNovo:
    def __init__(self, nome):
        self.nome = nome
        self.xp = 0
        self.nivel = 1
        self.xp_necessario = 100
        self.moedas = 0
        self.atributos = {
            "disciplina": 1,
            "foco": 1,
            "energia": 1
        }
        self.habilidades = {} 

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        while self.xp >= self.xp_necessario:
            self.xp -= self.xp_necessario
            self.nivel += 1 
            self.xp_necessario = int(self.xp_necessario * 1.5)
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def ganhar_moedas(self, quantidade):
        self.moedas += quantidade

    def adicionar_habilidade(self, habilidade, xp_ganho):
        if habilidade not in self.habilidades:
            self.habilidades[habilidade] = 0
            self.habilidades[habilidade] += xp_ganho

    def __str__(self):
        return (f"Personagem(nome={self.nome}, nivel={self.nivel}, xp={self.xp}, "
                f"moedas={self.moedas}, atributos={self.atributos}, habilidades={self.habilidades})")

    