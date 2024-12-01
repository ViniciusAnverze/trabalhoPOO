class Disciplina:
    def __init__(self, nome, total_aulas):
        self.nome = nome
        self.total_aulas = total_aulas
        self.alunos = []  # Agregação: cada Disciplina mantém uma lista de alunos matriculados

    def adicionar_aluno(self, aluno):
        for a in self.alunos:
            if a.matricula == aluno.matricula:
                print("Já existe um aluno com essa matrícula")
                return
            if a.cpf == aluno.cpf:
                print(f"Aluno de cpf {aluno.cpf} já cadastrado")
                return
        self.alunos.append(aluno)
        aluno.adicionar_disciplina(self)
        print(f"Aluno {aluno.nome} adicionado à disciplina {self.nome}.")

    def listar_alunos(self):
        if not self.alunos:
            return f"Não há alunos matriculados na disciplina {self.nome}."
        return [f"{aluno.nome} ({aluno.matricula})" for aluno in self.alunos]

    def remover_aluno(self, matricula):
        aluno_encontrado = None
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno_encontrado = aluno
                break
        
        if aluno_encontrado:
            self.alunos.remove(aluno_encontrado)
            aluno_encontrado.remover_disciplina(self)
            print(f"Aluno {aluno_encontrado.nome} removido da disciplina {self.nome}.")
        else:
            print(f"Nenhum aluno com matrícula {matricula} encontrado na disciplina {self.nome}.")

    def faltas_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno.faltas.get(self.nome, 0)
        print("Aluno não encontrado.")
        return None

    def __str__(self):
        return f"{self.nome}, {self.total_aulas} aulas no total)"
    
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def __str__(self):
        return f"{self.nome} - ({self.cpf})"

class Aluno(Pessoa): #Herança: Classe Aluno herdando da classe Pessoa
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.faltas = {}
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            self.faltas[disciplina.nome] = 0

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            if disciplina.nome in self.faltas:
                del self.faltas[disciplina.nome]

    def registrar_faltas(self, disciplina_nome, quantidade):
        if disciplina_nome in self.faltas:
            self.faltas[disciplina_nome] += quantidade
        else:
            print(f"O aluno não está matriculado na disciplina {disciplina_nome}.")

    def __str__(self):
        return f"{self.nome} - ({self.matricula})" #Polimorfismo: funcionalidade do método __str__ da classe filho foi alterada
    
class SistemaAcademico:
    def __init__(self):
        self.disciplinas = []

    def criar_disciplina(self, nome, total_aulas):
        disciplina = Disciplina(nome, total_aulas)
        self.disciplinas.append(disciplina)
        print(f"Disciplina {nome} criada com sucesso.")

    def listar_disciplinas(self):
        if not self.disciplinas:
            print("Nenhuma disciplina cadastrada.")
        else:
            for i, disc in enumerate(self.disciplinas, 1):
                print(f"{i}. {disc}")

    def buscar_disciplina(self, nome):
        for disciplina in self.disciplinas:
            if disciplina.nome == nome:
                return disciplina
        return None

    def excluir_disciplina(self, nome):
        disciplina_encontrada = None
        for disciplina in self.disciplinas:
            if disciplina.nome == nome:
                disciplina_encontrada = disciplina
                break
        
        if disciplina_encontrada:
            self.disciplinas.remove(disciplina_encontrada)
            print(f"Disciplina {disciplina_encontrada.nome} excluída com sucesso.")
        else:
            print(f"Disciplina {nome} não encontrada.")

    def alterar_nome_disciplina(self, nome_atual, novo_nome):
        disciplina = self.buscar_disciplina(nome_atual)
        if disciplina:
            disciplina.nome = novo_nome
            print(f"Nome da disciplina alterado para {novo_nome}.")
        else:
            print(f"Disciplina {nome_atual} não encontrada.")

    def porcentagem_presenca(self, disciplina, matricula):
        for aluno in disciplina.alunos:
            if aluno.matricula == matricula:
                faltas = disciplina.faltas_aluno(matricula)
                if faltas is not None:
                    return ((disciplina.total_aulas - faltas) / disciplina.total_aulas) * 100
        print("Aluno não encontrado.")
        return None

    def aulas_restantes(self, disciplina, matricula):
        for aluno in disciplina.alunos:
            if aluno.matricula == matricula:
                faltas = disciplina.faltas_aluno(matricula)
                if faltas is not None:
                    limite_faltas = disciplina.total_aulas * 0.25
                    restante = limite_faltas - faltas
                    return max(0, restante)
        print("Aluno não encontrado.")
        return None

sistema = SistemaAcademico()

while True:
    print("\n---- SISTEMA UFSC ----")
    print("--- Menu Principal ---")
    print("1. Criar disciplina")
    print("2. Listar disciplinas")
    print("3. Gerenciar disciplina")
    print("4. Excluir disciplina")
    print("5. Alterar nome da disciplina")
    print("6. Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Nome da disciplina: ")
            total_aulas = int(input("Quantidade total de aulas: "))
            sistema.criar_disciplina(nome, total_aulas)
        
        elif opcao == 2:
            sistema.listar_disciplinas()
        
        elif opcao == 3:
            nome_disciplina = input("Digite o nome da disciplina: ")
            disciplina = sistema.buscar_disciplina(nome_disciplina)
            if disciplina:
                while True:
                    print(f"\n--- Gerenciamento da Disciplina {disciplina.nome} ---")
                    print("1. Adicionar aluno")
                    print("2. Listar alunos")
                    print("3. Registrar faltas")
                    print("4. Ver faltas de aluno")
                    print("5. Ver porcentagem máxima de presença")
                    print("6. Ver aulas restantes")
                    print("7. Remover aluno")
                    print("8. Voltar")
                    
                    sub_opcao = int(input("Escolha uma opção: "))
                    
                    if sub_opcao == 1:
                        nome_aluno = input("Nome do aluno: ")
                        cpf_aluno = input("Cpf do aluno: ")
                        matricula = input("Matrícula: ")
                        aluno = Aluno(nome_aluno, cpf_aluno, matricula) 
                        disciplina.adicionar_aluno(aluno) #agregação de Aluno
                    
                    elif sub_opcao == 2:
                        print("Alunos matriculados:", disciplina.listar_alunos())
                    
                    elif sub_opcao == 3:
                        matricula = input("Matrícula do aluno: ")
                        quantidade = int(input("Quantidade de faltas: "))
                        for aluno in disciplina.alunos:
                            if aluno.matricula == matricula:
                                aluno.registrar_faltas(disciplina.nome, quantidade)
                                break
                        else:
                            print("Aluno não encontrado.")
                    
                    elif sub_opcao == 4:
                        matricula = input("Matrícula do aluno: ")
                        faltas = disciplina.faltas_aluno(matricula)
                        if faltas is not None:
                            print(f"Faltas do aluno: {faltas}")
                    
                    elif sub_opcao == 5:
                        matricula = input("Matrícula do aluno: ")
                        porcentagem = sistema.porcentagem_presenca(disciplina, matricula)
                        if porcentagem is not None:
                            print(f"Porcentagem máxima de presença: {porcentagem:.2f}%")
                    
                    elif sub_opcao == 6:
                        matricula = input("Matrícula do aluno: ")
                        restantes = sistema.aulas_restantes(disciplina, matricula)
                        if restantes is not None:
                            print(f"Aulas que o aluno ainda pode faltar: {restantes:.2f}")
                    
                    elif sub_opcao == 7:
                        matricula = input("Matrícula do aluno a ser removido: ")
                        disciplina.remover_aluno(matricula)
                    
                    elif sub_opcao == 8:
                        break
                    else:
                        print("Opção inválida.")
            else:
                print("Disciplina não encontrada.")
        
        elif opcao == 4:
            nome = input("Digite o nome da disciplina a ser excluída: ")
            sistema.excluir_disciplina(nome)
        
        elif opcao == 5:
            nome_atual = input("Digite o nome atual da disciplina: ")
            novo_nome = input("Digite o novo nome da disciplina: ")
            sistema.alterar_nome_disciplina(nome_atual, novo_nome)
        
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    
    except ValueError:
        print("Erro: entrada inválida.")
