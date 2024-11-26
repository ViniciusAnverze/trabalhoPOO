class Faltas:
    def __init__(self, numeroDeFaltas=0):
        self.numeroDeFaltas = numeroDeFaltas
    
    def adicionarFaltas(self, faltas):
        self.numeroDeFaltas += faltas
    
    def obterFaltas(self):
        return self.numeroDeFaltas

class SistemaGeralUFSC:
    def __init__(self):
        self.alunos = []
        
    def acharMatricula(self, matricula):
        for aluno in self.alunos:
            if aluno['matricula'] == matricula:
                return aluno
        print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
        return None
        
    def adicionarAluno(self, aluno):
        if self.acharMatricula(aluno.matricula) != None:
            print('Já existe um aluno com essa matrícula. Cada aluno deve ter uma matrícula única.')
            return
        self.alunos.append({'nome': aluno.nome, 'matricula': aluno.matricula, 'faltas': aluno.faltas.obterFaltas()})
        
    def atualizarFichaAluno(self, matricula):
        aluno = self.acharMatricula(matricula)
        if aluno is None:
            return
        else:
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matricula do aluno: ')
            numeroDeFaltas = int(input(f'Digite o número de faltas do aluno até hoje: '))
            aluno['nome'] = nome
            aluno['matricula'] = matricula
            aluno['faltas'] = numeroDeFaltas
            print(f'A ficha de {nome} foi atualizada!')

    def deletarFichaAluno(self, matricula):
        aluno = self.acharMatricula(matricula)
        if aluno is None:
            print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            return
        self.alunos.remove(aluno)
        print(f'Aluno de matrícula {matricula} foi deletado')
    
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = (self.creditosTotais * 0.25) - numeroDeFaltas
        if aulasFaltaveis < 0:
            return 'Aluno já foi reprovado por frequência insuficiente'
        return f'{aulasFaltaveis} dias'

class SistemaPOO(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 102
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais

class SistemaFMI(SistemaGeralUFSC):
    def __init__(self):
        super().__init__()
        self.creditosTotais = 72
        
    def numeroAulasFaltaveis(self, numeroDeFaltas):
        aulasFaltaveis = self.creditosTotais - numeroDeFaltas
        return f'Você pode faltar {aulasFaltaveis} dias (todas as aulas), desde que sua média final não seja menor que 6, caso passar direto, ou menor do que 3, em caso de recuperação'
        
    def porcentagemMaximaPossivel(self, numeroDeFaltas):
        return (self.creditosTotais - numeroDeFaltas) / self.creditosTotais

class Aluno:
    def __init__(self, nome, matricula, numeroDeFaltas):
        self.nome = nome
        self.matricula = matricula
        self.faltas = Faltas(numeroDeFaltas)  # Composição: Aluno tem uma instância de Faltas

# Criação dos sistemas
SistemaGeralUFSC = SistemaGeralUFSC()
SistemaPOO = SistemaPOO()
SistemaFMI = SistemaFMI()

# Loop principal
while True:
    try:
        opcao = int(input('1 - adicionar aluno \n2 - buscar aluno \n3 - atualizar ficha do aluno \n4 - deletar ficha de aluno \n5 - Verificar porcentagem máxima possível \n6 - Verificar quantos dias o aluno ainda pode faltar para não reprovar \n7 - sair do programa \n'))
        
        if opcao == 1:
            nome = input('Digite o nome do aluno: ')
            numeroDeFaltas = int(input('Digite o número de faltas do aluno: '))
            matricula = input('Digite a matricula do aluno: ')
            aluno = Aluno(nome, matricula, numeroDeFaltas)
            SistemaGeralUFSC.adicionarAluno(aluno)
            
        elif opcao == 2:
            matricula = input('Digite a matrícula do aluno que você quer buscar: \n')
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            if aluno:
                print(aluno)
        
        elif opcao == 3:
            matricula = input('Digite a matrícula do aluno que você quer atualizar a ficha: \n')
            SistemaGeralUFSC.atualizarFichaAluno(matricula)
                
        elif opcao == 4:
            matricula = input('Digite a matrícula do aluno que você quer deletar: \n')
            SistemaGeralUFSC.deletarFichaAluno(matricula)
        
        elif opcao == 5:
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            if aluno is None:
                print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            else:
                if opcaoMateria == '1':
                    porcentagemMaximaPossivel = SistemaPOO.porcentagemMaximaPossivel(aluno['faltas'])
                    print(f'{porcentagemMaximaPossivel*100:.2f}%')
                elif opcaoMateria == '2':
                    porcentagemMaximaPossivel = SistemaFMI.porcentagemMaximaPossivel(aluno['faltas'])
                    print(f'{porcentagemMaximaPossivel*100:.2f}%')
                else:
                    print('ERRO: Você deve digitar 1 ou 2')

        elif opcao == 6:
            opcaoMateria = input('Digite 1 para verificar POO e 2 para verificar FMI: \n')
            matricula = input('Digite a matrícula do aluno que você quer verificar: \n')
            aluno = SistemaGeralUFSC.acharMatricula(matricula)
            if aluno is None:
                print(f'Nenhum aluno foi encontrado com a matrícula {matricula}\n')
            else:
                if opcaoMateria == '1':
                    numeroAulasFaltaveis = SistemaPOO.numeroAulasFaltaveis(aluno['faltas'])
                    print(numeroAulasFaltaveis)
                elif opcaoMateria == '2':
                    numeroAulasFaltaveis = SistemaFMI.numeroAulasFaltaveis(aluno['faltas'])
                    print(numeroAulasFaltaveis)
                else:
                    print('ERRO: Você deve digitar 1 ou 2')

        elif opcao == 7:
            break
        
        else:
            print('Opção inválida.')
            
    except ValueError:
        print('Você deve digitar um número, não uma letra. Digite o numero 1, 2, 3, 4 ou 5')

