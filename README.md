# Laboratório de Programação — Atividade Prática em Python

**Aluno:** Heleno Lisboa
**Disciplina:** Laboratório de Programação
**Professor:** Josimar dos Santos

## 1. Visão geral

Sistema de linha de comando para cadastro de alunos e cálculo de médias, desenvolvido em Python conforme o enunciado da atividade prática (Ações de Aprendizagem 1 e 2). O foco do enunciado é o uso de estruturas de dados compostas e a modularização por funções.

O projeto está dividido em duas entregas independentes. A segunda estende a primeira, como o enunciado pede, e cada arquivo executa sozinho, sem importar o outro.

```
.
├── acao1_cadastro_e_media/
│   └── programa1.py
├── acao2_estatisticas_turma/
│   └── programa2.py
└── README.md
```

## 2. Requisitos do enunciado e como foram atendidos

### Ação de Aprendizagem 1 — `programa1.py`

| Requisito | Implementação |
|---|---|
| Solicitar a quantidade de alunos, obrigatoriamente entre 2 e 7 | `ler_inteiro(mensagem, minimo, maximo)` repete a pergunta até receber um inteiro dentro do intervalo |
| Solicitar o nome de cada aluno de forma individual e interativa | Laço `for` que percorre os alunos e lê o nome com `input()` |
| Solicitar duas notas por aluno, aceitando apenas valores de 0,0 a 10,0 | `ler_nota(mensagem)` valida o intervalo e rejeita texto não numérico |
| Armazenar os dados em lista, matriz ou dicionário | Lista de dicionários, um por aluno (`nome`, `nota1`, `nota2`, `media`) |
| Função dedicada para calcular a média | `calcular_media(nota1, nota2)`, média aritmética simples |
| Exibir os dados e a média de cada aluno | Saída no formato do exemplo do enunciado |

### Ação de Aprendizagem 2 — `programa2.py`

Mantém toda a lógica da Ação 1 e acrescenta, ao final, as informações consolidadas da turma:

| Requisito | Implementação |
|---|---|
| Média da turma | Média das médias individuais: `sum(...) / len(alunos)` |
| Total de alunos | `len(alunos)` |
| Aluno com a maior média | `max(alunos, key=...)` |
| Aluno com a menor média | `min(alunos, key=...)` |

> Sobre a Ação de Aprendizagem 3 do PDF: o slide correspondente apenas apresenta o resultado esperado e as diretrizes de entrega da Ação 2, sem requisito novo. Por isso não há um terceiro programa.

## 3. Decisões de projeto

- **Estrutura de dados:** lista de dicionários. É legível, acessa os campos pelo nome (`aluno["media"]`) e funciona bem com `max`/`min` por `key`, sem índices numéricos.
- **Validação por laço de repetição:** a entrada inválida nunca interrompe o programa. As funções `ler_inteiro` e `ler_nota` repetem o pedido com uma mensagem clara. Os tipos inválidos são tratados com `try/except ValueError`.
- **Vírgula decimal:** a nota aceita tanto `9.8` quanto `9,8` (`replace(",", ".")`), já que o enunciado usa a notação brasileira.
- **Separação de responsabilidades:** leitura, validação, cálculo e exibição ficam em funções distintas, e a execução é protegida por `if __name__ == "__main__"`.
- **Formato de saída:** notas e médias dos alunos com uma casa decimal e estatísticas da turma com duas casas e vírgula, como nos exemplos do PDF.
- **Média da turma:** como cada aluno tem o mesmo número de notas (duas), a média das médias é igual à média de todas as notas registradas.

## 4. Como executar

**Requisito:** Python 3.8 ou superior. Não há dependências externas.

Pelo terminal, a partir da pasta principal do projeto:

```bash
python acao1_cadastro_e_media/programa1.py
```

```bash
python acao2_estatisticas_turma/programa2.py
```

Ou entrando em cada pasta:

```bash
cd acao1_cadastro_e_media
python programa1.py
```

## 5. Roteiro de testes

### Teste 1 — Ação 1: validação e exemplo do enunciado

Entradas, na ordem:

| Pergunta | Digitar | Esperado |
|---|---|---|
| Quantidade de alunos | `1` | Recusado (fora de 2 a 7) |
| Quantidade de alunos | `2` | Aceito |
| Aluno 1 | `João`, `8`, `9,8` | |
| Aluno 2 | `Maria`, nota 1 `11` | Recusado (fora de 0 a 10) |
| Aluno 2 | nota 1 `3`, nota 2 `4` | |

Saída esperada:

```
Aluno: João
Nota 1 8.0 | Nota 2 9.8
Média: 8.9

Aluno: Maria
Nota 1 3.0 | Nota 2 4.0
Média: 3.5
```

### Teste 2 — Ação 2: estatísticas da turma

Entradas, na ordem:

| Pergunta | Digitar | Esperado |
|---|---|---|
| Quantidade de alunos | `9` | Recusado |
| Quantidade de alunos | `4` | Aceito |
| Aluno 1 | `Pedro`, `7`, `5` | média 6.0 |
| Aluno 2 | `Ana`, `9`, `10` | média 9.5 |
| Aluno 3 | `Lucas`, nota 1 `-1` | Recusado |
| Aluno 3 | `Lucas`, `1`, `3` | média 2.0 |
| Aluno 4 | `Bia`, nota 1 `abc` | Recusado |
| Aluno 4 | `Bia`, `6,5`, `8,5` | média 7.5 |

Saída esperada ao final:

```
Média da Turma: 6,25
Total de Alunos: 4
Maior média da turma:
Ana com 9,50
Menor média da turma:
Lucas com 2,00
```

### Casos-limite

- Quantidade `2` e `7` devem ser aceitas. `0`, `8` e texto devem ser recusados.
- Notas `0` e `10` devem ser aceitas.
- Em caso de empate de médias, o programa exibe o primeiro aluno cadastrado com aquele valor.

## 6. Observação sobre o exemplo do enunciado

O exemplo de resultado final do PDF mostra "Média da Turma: 6,30" com "Total de Alunos: 3", mas lista apenas João (8,9) e Maria (3,5), cuja média seria 6,20. Os valores do exemplo são ilustrativos e não fecham entre si. O programa calcula corretamente a partir dos dados digitados.
