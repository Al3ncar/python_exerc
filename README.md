# 📚 Lista de Exercícios 1 – Introdução a Buscas

> Exercícios desenvolvidos para a disciplina de **Programação de Computadores**, cobrindo lógica condicional, operações matemáticas e interação com o usuário em Python.

---

## 🗂️ Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Exercícios](#-exercícios)
  - [Exercício 1 – Validação de Intervalo Numérico](#exercício-1--validação-de-intervalo-numérico)
  - [Exercício 2 – Sistema de Desconto em Compras](#exercício-2--sistema-de-desconto-em-compras)
  - [Exercício 3 – Sistema de Análise de Desempenho Escolar](#exercício-3--sistema-de-análise-de-desempenho-escolar)
  - [Exercício 4 – Conversor Universal de Unidades Térmicas](#exercício-4--conversor-universal-de-unidades-térmicas)
  - [Exercício 5 – Cálculo de Salário por Turno de Trabalho](#exercício-5--cálculo-de-salário-por-turno-de-trabalho)
  - [Exercício 6 – Verificador de Saldo e Pagamento de Contas](#exercício-6--verificador-de-saldo-e-pagamento-de-contas)
  - [Exercício 7 – Simulador de Empréstimo com Juros Simples](#exercício-7--simulador-de-empréstimo-com-juros-simples)
  - [Exercício 8 – Calculadora de IMC Personalizada (OMS)](#exercício-8--calculadora-de-imc-personalizada-oms)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)

---

## 💡 Sobre o Projeto

Este repositório contém as soluções da **Lista de Exercícios 1** da disciplina de Programação de Computadores. Os exercícios abordam conceitos fundamentais de lógica de programação com Python, como:

- Estruturas condicionais (`if`, `elif`, `else`)
- Entrada e saída de dados
- Operações matemáticas e formatação de valores
- Condicionais aninhadas e operadores lógicos

---

## 📝 Exercícios

### Exercício 1 – Validação de Intervalo Numérico

O programa solicita um número ao usuário e verifica se ele está dentro do intervalo de **0 a 9** (inclusive).

**Regras:**
- Número dentro do intervalo → exibe `"Valor correto"`
- Número fora do intervalo → exibe `"Valor incorreto"`

---

### Exercício 2 – Sistema de Desconto em Compras

O programa lê o valor total de uma compra e aplica um desconto automaticamente com base no valor informado.

**Regras:**
- Compras **acima de R$ 200,00** → desconto de **20%**
- Compras **até R$ 200,00** → sem desconto (exibe o valor original)

---

### Exercício 3 – Sistema de Análise de Desempenho Escolar

O programa recebe o nome do aluno e suas **3 notas bimestrais** (entre 0 e 10), calcula a média aritmética e determina a situação acadêmica.

**Critérios de classificação:**

| Média | Situação |
|---|---|
| ≥ 7,0 | ✅ Aprovado |
| 5,0 – 6,9 | ⚠️ Recuperação |
| < 5,0 | ❌ Reprovado |

A média é exibida com **2 casas decimais**.

---

### Exercício 4 – Conversor Universal de Unidades Térmicas

Ferramenta interativa para conversão de temperatura entre **Celsius** e **Fahrenheit**, simulando uma necessidade real de laboratório de pesquisa.

**Menu de opções:**
- `1` → Celsius para Fahrenheit
- `2` → Fahrenheit para Celsius
- Opção inválida → exibe mensagem de erro

**Fórmulas utilizadas:**

$$F = (C \times 1{,}8) + 32$$

$$C = (F - 32) / 1{,}8$$

---

### Exercício 5 – Cálculo de Salário por Turno de Trabalho

O programa solicita o turno de trabalho e a quantidade de horas trabalhadas, calculando o salário correspondente.

**Valor por hora:**

| Turno | Valor/hora |
|---|---|
| Matutino (`M`) | R$ 45,00 |
| Outros turnos | R$ 37,50 |

---

### Exercício 6 – Verificador de Saldo e Pagamento de Contas

Programa de auxílio ao controle financeiro pessoal. O usuário informa o valor de **3 contas domésticas** (ex: água, luz e telefone) e seu salário mensal.

**Lógica:**
- Soma o total das três contas
- Se o salário **não for suficiente** → exibe `"Salário insuficiente"`
- Se for suficiente → exibe o **saldo restante** após pagar as contas

---

### Exercício 7 – Simulador de Empréstimo com Juros Simples

Sistema de pré-aprovação de empréstimos para um banco digital, com simulação de parcelamento aplicando juros simples mensais.

**Fluxo do programa:**

1. **Análise de Crédito** → verifica salário e pendências financeiras
2. **Critério de Aprovação** → aprovado apenas se tiver **zero pendências**
   - Com pendências → `"Empréstimo Negado: Cliente possui pendências."`
3. **Simulação** (se aprovado) → solicita valor desejado e número de parcelas
4. **Cálculo com taxa de 0,9% ao mês:**

$$juros = valor\_emprestimo \times 0{,}009 \times n\_parcelas$$

$$valor\_total = valor\_emprestimo + juros$$

$$valor\_parcela = valor\_total / n\_parcelas$$

5. Exibe o valor de cada parcela e o total a pagar

**Requisitos técnicos aplicados:** condicionais aninhadas, fórmulas com múltiplas variáveis e formatação em moeda (R$).

---

### Exercício 8 – Calculadora de IMC Personalizada (OMS)

Calculadora de **Índice de Massa Corporal** com classificação diferenciada por sexo, seguindo os parâmetros da Organização Mundial da Saúde (OMS).

**Entradas:** peso (kg), altura (m) e sexo (`M` ou `F`)

**Fórmula:**

$$IMC = \frac{peso}{altura^2}$$

**Tabela de classificação:**

| Condição | IMC (Mulheres) | IMC (Homens) |
|---|---|---|
| Abaixo do peso | < 19,1 | < 20,7 |
| Peso normal | 19,1 – 25,8 | 20,7 – 26,4 |
| Marginalmente acima | 25,8 – 27,3 | 26,4 – 27,8 |
| Acima do peso ideal | 27,3 – 32,3 | 27,8 – 31,1 |
| Obeso | > 32,3 | > 31,1 |

O IMC é exibido com **1 casa decimal**, seguido da categoria correspondente.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Linguagem:** Python 3
- **Conceitos:** Condicionais, entrada/saída, operações matemáticas, formatação de strings

---

## ▶️ Como Executar

**Pré-requisito:** ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd seu-repositorio

# Execute o exercício desejado
python exercicio1.py
```

---

<p align="center">Desenvolvido para a disciplina de Programação de Computadores 🎓</p>
