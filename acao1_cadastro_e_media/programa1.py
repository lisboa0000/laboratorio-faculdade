"""
Aluno: Heleno Lisboa
Disciplina: Laboratório de Programação
Professor: Josimar dos Santos
Ação de Aprendizagem 1: cadastro de alunos e cálculo de médias
"""

def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
        except ValueError:
            pass
        print(f"Valor inválido. Digite um número inteiro entre {minimo} e {maximo}.")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if 0.0 <= nota <= 10.0:
                return nota
        except ValueError:
            pass
        print("Nota inválida. Digite um valor entre 0,0 e 10,0.")


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def main():
    quantidade = ler_inteiro("Quantidade de alunos (2 a 7): ", 2, 7)

    alunos = []  # lista de dicionários
    for i in range(1, quantidade + 1):
        print(f"\n--- Aluno {i} ---")
        nome = input("Nome: ").strip()
        nota1 = ler_nota("Nota 1: ")
        nota2 = ler_nota("Nota 2: ")
        alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2,
                       "media": calcular_media(nota1, nota2)})

    print("\n===== RESULTADO =====")
    for a in alunos:
        print(f"Aluno: {a['nome']}")
        print(f"Nota 1 {a['nota1']:.1f} | Nota 2 {a['nota2']:.1f}")
        print(f"Média: {a['media']:.1f}\n")


if __name__ == "__main__":
    main()
