# 📋 Sistema de Ficha de Cadastro (CRUD em Python)

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="100" height="100"/>
</p>

> ⚠️ **NOTA SOBRE O DESENVOLVIMENTO:** 
> Este código poderia estar mais otimizado com a aplicação de **Funções (`def`)**, **Orientação a Objetos (Classes)** e **Laços de Repetição (`while` / `for`)**. No entanto, eu contrui ele assim propositalmente utilizando **apenas** os conceitos estudados até o momento no curso do **LanCode**: *Estruturas Condicionais, Match/Case e Estruturas de Dados (Listas, Tuplas e Dicionários)*. O objetivo foi desafiar minha lógica de programação e criar um sistema CRUD funcional respeitando o meu progresso acadêmico.

---

## 📱 Ambiente de Desenvolvimento
Este projeto foi **100% desenvolvido, testado e validado em um smartphone** (Samsung Galaxy A56 5G), demonstrando que o aprendizado da lógica de programação e a resolução de problemas não dependem de um setup avançado.

---

## 📚 Módulos Aplicados (Curso LanCode)
* **Tratamento de Strings & Dados:** Uso de `.strip()`, `.title()`, `.upper()` e tipagem inteira.
* **Estruturas Condicionais (`if` / `elif` / `else`):** Validação de regras de negócio (impedir CPFs duplicados, checar tamanho de entradas e campos vazios).
* **Estrutura de Seleção (`match / case`):** Construção do menu principal e submenus de navegação.
* **Estruturas de Dados (Dicionários & Listas):** Armazenamento de registros por listas sincronizadas (`ficha["nome"]`, `ficha["cpf"]`, etc.), busca via `.index()`, alteração por posição e remoção com `del` e `.clear()`.

---

## 🛠️ Funcionalidades do Sistema
O sistema utiliza o **CPF** como chave única de identificação:

1. **[1] Criar cadastro:** Valida se o CPF já existe, obriga o CPF a ter 11 dígitos e a sigla do estado a ter 2 caracteres antes de salvar os dados.
2. **[2] Verificar cadastro:** Exibe toda a base de dados ou pesquisa um cliente específico pelo CPF.
3. **[3] Atualizar cadastro:** Valida a existência do registro antes de permitir alterar pontualmente Nome, Idade, Cidade ou Estado.
4. **[4] Deletar cadastro:** Permite a remoção individual de um cliente via CPF ou a limpeza total da base de dados.

---

## 🚀 Próximos Passos
Com o encerramento do módulo de Estruturas de Dados, o próximo passo na jornada será aplicar **Laços de Repetição (`while` e `for`)** para manter o menu ativo em ciclo contínuo e refatorar as validações.
