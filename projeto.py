class Disciplina:
    def __init__(self, nome, creditos, total_aulas):
        self.nome = nome
        self.creditos = creditos
        self.total_aulas = total_aulas
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.adicionar_disciplina(self)
        else:
            print(f"O aluno {aluno.nome} já está matriculado na disciplina {self.nome}.")
            
    def __str__(self):
        return f"{self.nome} ({self.creditos} créditos, {self.total_aulas} aulas no total)"

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []
    
    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
    
    def __str__(self):
        return f"{self.nome} ({self.matricula})"