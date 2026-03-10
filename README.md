# 💰 Controle de Gastos

Este projeto é um sistema de gestão financeira pessoal desenvolvido para colocar em prática conceitos de **Arquitetura de Software** e **DevOps/SRE**. A aplicação utiliza uma estrutura organizada para garantir que o código seja fácil de manter e escalar.

---

## 🏗️ Arquitetura do Sistema

A aplicação segue o padrão **MVC (Model-View-Controller)**. Essa separação permite que cada parte do código tenha uma responsabilidade única, facilitando testes e futuras integrações com bancos de dados ou nuvem.

![Arquitetura em Camadas](./docs/image_673620.png)

### 🧩 Divisão de Camadas:
* **Model**: Define a estrutura do objeto `Gasto` (Atributos como Descrição, Valor e Data).
* **Service**: Onde fica a "inteligência" do app, como o cálculo de totais mensais.
* **Repository**: Responsável por salvar e buscar os dados.
* **Controller**: A ponte que recebe os comandos do usuário e devolve o relatório.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x 🐍
* **Containerização:** Docker 🐳
* **Versionamento:** Git & GitHub 📂

---

## 🚀 Como Executar o Projeto

Para rodar a aplicação via **Docker**, utilize os comandos abaixo no seu terminal:

### 1. Build da Imagem
Cria a imagem do container baseada no Dockerfile:
```bash
docker build -t controle-gastos .
