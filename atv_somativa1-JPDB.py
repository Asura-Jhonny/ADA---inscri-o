# João Pedro Dal'Boit Pires        Inteligência Artificial Aplicada
# objetivo -> criar um menu para uma escola, desenvolver apenas o menu de estudantes no momento
students = []
disciplines = []
professors = []
classes = []
enrollments = []
def menu_pri():
    print('---MENU PRINCIPAL ---  '
          '(1) ESTUDANTE  '
          '(2) DISCIPLINAS  '
          '(3) PROFESSORES  '
          '(4) TURMAS  '
          '(5) MATRÍCULAS  '
          '(0) SAIR')
    b = int(input('O QUE GOSTARIA DE FAZER? '))
    if b == 1:
        menu_est()
    elif b == 2:
        print('EM DESENVOLVIMENTO')
        menu_pri()
    elif b == 3:
        print('EM DESENVOLVIMENTO')
        menu_pri()
    elif b == 4:
        print('EM DESENVOLVIMENTO')
        menu_pri()
    elif b == 5:
        print('EM DESENVOLVIMENTO')
        menu_pri()
    elif b == 0:
        exit()
    else:
        print('OPÇÃO INVÁLIDA')
        menu_pri()

def menu_est():
    print('--- MENU ESTUDANTE ---  '
          '(1) INCLUIR  '
          '(2) LISTAR  '
          '(3) ATUALIZAR  '
          '(4) EXCLUIR  '
          '(0) VOLTAR')
    a = int(input('O QUE DESEJA FAZER? '))
    if a == 1:
        students.append(add_student())
        menu_est()
    elif a == 2:
        if students == 0:
            print('NENHUM ALUNO LISTADO')
        else:
            print(students)
        menu_est()
    elif a == 3:
        print('EM DESENVOLVIMENTO')
        menu_est()
    elif a == 4:
        print('EM DESENVOLVIMENTO')
        menu_est()
    elif a == 0:
        menu_pri()
    else:
        print('OPÇÃO INVÁLIDA')
        menu_est()

def display_menu(options):
    print('--- MENU ---')
    for i, option in enumerate(options):
        print(f'({i+1}) {option}')
    print('(0) Sair')
    return int(input('O que deseja fazer? '))

def add_student():
    student = {
        'codigo': input('Código do Aluno: '),
        'nome': input('Nome do Aluno: '),
        'cpf': input('CPF do Aluno: ')
    }
    students.append(student)
    print('Aluno adicionado com sucesso!')

def update_student():
    codigo = input('Código do Aluno: ')
    for student in students:
        if student['codigo'] == codigo:
            student['nome'] = input('Nome do Aluno: ')
            student['cpf'] = input('CPF do Aluno: ')
            print('Dados atualizados com sucesso!')
            return
    print('Aluno não encontrado.')

def remove_student():
    codigo = input('Código do Aluno: ')
    for i, student in enumerate(students):
        if student['codigo'] == codigo:
            del students[i]
            print('Aluno removido com sucesso!')
            return
    print('Aluno não encontrado.')

def list_students():
    if not students:
        print('Nenhum aluno listado.')
    else:
        for student in students:
            print(student)

def add_discipline():
    discipline = {
        'codigo': input('Código da Disciplina: '),
        'nome': input('Nome da Disciplina: ')
    }
    disciplines.append(discipline)
    print('Disciplina adicionada com sucesso!')

def update_discipline():
    codigo = input('Código da Disciplina: ')
    for discipline in disciplines:
        if discipline['codigo'] == codigo:
            discipline['nome'] = input('Nome da Disciplina: ')
            print('Dados atualizados com sucesso!')
            return
    print('Disciplina não encontrada.')



print(menu_pri())



