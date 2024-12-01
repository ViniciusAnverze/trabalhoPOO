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
    
class SistemaAcademico:
    def __init__(self):
        self.disciplinas = []

    def criar_disciplina(self, nome, creditos, total_aulas):
        disciplina = Disciplina(nome, creditos, total_aulas)
        self.disciplinas.append(disciplina)
        print(f"Disciplina {nome} criada com sucesso.")

    def listar_disciplinas(self):
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
        else:
            for i, disc in enumerate(self.disciplinas, 1):
                print(f"{i}. {disc}")

sistema = SistemaAcademico()

while True:
    print("\n--- Menu Principal ---")
    print("1. Criar disciplina")
    print("2. Listar disciplinas")
    print("3. Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Nome da disciplina: ")
            creditos = int(input("Quantidade de créditos: "))
            total_aulas = int(input("Quantidade total de aulas: "))
            sistema.criar_disciplina(nome, creditos, total_aulas)
        
        elif opcao == 2:
            sistema.listar_disciplinas()
        
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Erro: entrada inválida.")