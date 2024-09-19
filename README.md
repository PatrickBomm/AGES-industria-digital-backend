# Indústria Digital Backend

Este é o backend do projeto Indústria Digital, desenvolvido com [FastAPI](https://fastapi.tiangolo.com/) e gerenciado com [Poetry](https://python-poetry.org/).

Aqui está o conteúdo completo formatado em Markdown:

## Padrões de Commit

Nosso padrão de commits será baseado no [Conventional Commits](https://www.conventionalcommits.org/pt-br/), uma convenção de mensagens de commit estruturada que facilita a comunicação e o rastreamento de alterações no código.

### Estrutura das Mensagens de Commit

Cada mensagem de commit deve ser estruturada da seguinte maneira:

1. **Tipo**: Comece com um tipo (`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`).
2. **ID da Task entre Parênteses**: Siga o tipo com o ID da tarefa entre parênteses, um dois-pontos e um espaço.
3. **Breve Descrição**: Forneça uma breve descrição do que foi alterado, começando com uma letra maiúscula e sem ponto final.

#### Limite de Caracteres

A mensagem de commit deve ter um limite de 75 caracteres para incentivar mensagens descritivas e relevantes.

### Tipos de Mensagens de Commit

O tipo deve ser escolhido com base no tipo de alteração que está sendo feita:

- **feat**: Para adicionar uma nova funcionalidade.
- **fix**: Para corrigir um bug.
- **docs**: Para alterações apenas na documentação.
- **style**: Para alterações de estilização.
- **refactor**: Para alterações de código que não adicionam uma nova funcionalidade ou corrigem um bug.
- **test**: Para adicionar ou alterar testes.
- **chore**: Para alterações em arquivos de configuração ou outras tarefas de manutenção.

### Exemplo

```plaintext
feat(1234): Adiciona a funcionalidade de busca por nome de usuário
```

No exemplo acima, o verbo "Adiciona" é utilizado para indicar que uma nova funcionalidade está sendo adicionada. Isso torna a mensagem mais clara e direta, facilitando a comunicação e o entendimento das alterações realizadas no código.

### Recursos Adicionais

Para saber mais sobre Conventional Commits, visite o site oficial dos [Conventional Commits](https://www.conventionalcommits.org/pt-br/).


## Padrões de Branch e Workflow

Para nosso fluxo de trabalho, usamos a branch `main` como a branch de produção principal. Nenhuma alteração direta deve ser feita nessa branch, exceto quando estivermos prontos para fazer um release.  
Para desenvolver novas funcionalidades e corrigir bugs, usamos a branch `develop` como nossa branch principal de desenvolvimento. A partir daqui, criamos novas branches para cada tarefa que precisa ser trabalhada.

- **feat**: Features novas.
- **fix**: Ajustes na aplicação.
- **chore ou arch**: Atualizações que não impactam na parte lógica da aplicação, e sim na arquitetura e organização.

O nome dessas branches devem seguir o padrão `feat/id-task/nome-da-feature`, `fix/id-task/nome-do-fix` ou `chore/id-task/objetivo-da-atualização`.

Exemplo: `feat/1234/adiciona-botao`.

**Importante:** Caso você não siga esses padrões, seus commits serão automaticamente rejeitados.

Ao final da sprint, todas as branches de feature e fixes devem ser revisadas e mescladas com a branch `develop` para integrar todas as alterações realizadas. Então, quando estamos prontos para fazer um release, a branch `main` é atualizada com a última versão de `develop` e o código é lançado para produção.

Este padrão foi inspirado no padrão [GitFlow](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow).

## Pré-requisitos

Antes de configurar o ambiente, você precisará instalar algumas ferramentas:

- **pyenv**: Ferramenta para gerenciar versões do Python.
  - [Instalação no Windows](https://pyenv-win.github.io/pyenv-win/)
  - [Instalação no GNU/Linux e macOS](https://github.com/pyenv/pyenv-installer)
  
- **pipx**: Ferramenta para instalar e gerenciar aplicativos Python.
  - [Guia de instalação](https://pipx.pypa.io/stable/installation/)

- **Poetry**: Ferramenta para gerenciamento de dependências e ambientes virtuais em projetos Python.
  - [Guia de instalação](https://python-poetry.org/docs/)

## Configuração do Ambiente

1. Abra a linha de comando na raiz do projeto.

2. Instale a versão 3.12 do Python usando pyenv:
   ```bash
   pyenv install 3.12
   ```

3. Instale as dependências do projeto e ative o ambiente virtual:
   ```bash
   poetry install
   ```

4. Create the Docker volume (only need to be done the first time):
    ```bash
    docker volume create industria-digital-db
    ```

## Executando o Projeto Localmente

Para rodar o servidor localmente:

1. Run the Docker compose file (Database):
    ```bash
    docker compose up
    ```

2. Inicie o servidor FastAPI:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

## Estrutura do Projeto

- `main.py`: Ponto de entrada do aplicativo FastAPI.
- `app/`: Contém a lógica do backend, incluindo os endpoints e a configuração do banco de dados.
