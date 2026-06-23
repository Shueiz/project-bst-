# Árvore Binária de Busca (BST) - Gerenciador de Estoque

* [🇺🇸 Read in English](README.md)

Este projeto é o trabalho final da disciplina de Estrutura de Dados. Trata-se de um sistema interativo de gerenciamento de estoque que utiliza uma **Árvore Binária de Busca (BST)** desenvolvida do zero, integrada a uma interface gráfica moderna feita com `CustomTkinter`.

## 📌 Funcionalidades
O sistema aplica os conceitos clássicos de árvores binárias para organizar nomes de produtos alfabeticamente. 
*   **Adicionar:** Insere produtos na árvore de forma ordenada.
*   **Buscar:** Verifica rapidamente se um produto está em estoque.
*   **Remover:** O maior desafio técnico do projeto. Trata a remoção de nós folha, nós com um filho e nós com dois filhos (utilizando o sucessor *in-order*).
*   **Visualização (Traversals):** Exibe o conteúdo da árvore em ordem alfabética (`In-Order`), além de pré-ordem (`Pre-Order`) e pós-ordem (`Post-Order`).

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca da interface gráfica executando no terminal:
```bash
   pip install customtkinter
```
1. Execute o arquivo principal:
```bash
    python main_gui.py
```
## 🎥 Vídeo de Apresentação
Para ver o sistema funcionando e entender a explicação da lógica de funcionamento (narrada em português), confira o post no meu LinkedIn: [Inserir Link do LinkedIn Aqui]