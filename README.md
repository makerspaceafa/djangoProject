# Projeto Tasks - 1º Workshop Django MS
Este repositório contem o projeto exemplo desenvolvido nos workshops da semana 1 a 5 de Março de 2021.

Está aqui para servir de base ao workshop prático de Git/GitHub também.

## Setup:
(Só é necessário correr a primeira vez, ou após fazer alterações aos models)
- Criar venv: `python -m venv xxx`, onde `xxx` é o nome da pasta onde vai ficar o ambiente.  
  O padrão é chamá-la `venv` também.  
- `python manage.py makemigrations`
- `python manage.py migrate`

## Como correr
Basta correr no IDE como sempre vimos...  
Ou podem usar `python manage.py runserver` na linha de comandos.
  
### Para criar utilizadores
(Só os campos `Username` e `Password` são necessários preencher)
- `python manage.py createsuperuser`

## Desafios:
(Ordenados desde relativamente simples / acessíveis até Super Ninja Wizard Level)
1. Criar página de registo de utilizador.
2. O visual está a precisar de um jeitinho.
3. Já experimentaram brincar com tarefas com o mesmo nome?
   Na lista privada está a funcionar tudo bem? De certeza?
4. E redesenhar o front-end para ser mobile first?
5. Encontrar e arranjar as inúmeras vulnerabilidades que existem neste website:
   - Crashes quando os utilizadores fazem algo fora do "percurso planeado";
   - Vulnerabilidades de segurança (possibilidade de ver/editar tasks de outros users).
6. Sistema de “prioridades” para ranking das tarefas (prioridade mais elevada aparece primeiro na lista)
7. Permitir aos users reordenar tarefas (click and drag) e automaticamente ajustar a sua prioridade na base de dados (requires JavaScript).

## Como contribuir
Este repositório segue os princípios do [GitHub Flow](https://guides.github.com/introduction/flow/) mas com algumas alterações.  

### Estrutura do repositório
**2 branches permanentes:**
- develop (default branch).
- production (commits bloqueadas - só entra código via pull request).

**Vários branches temporários:**  
A nomenclatura destes branches deve ser apropriada e intuitiva.
- Desenvolver nova feature: `feature/XX`.
- Resolver um problema de uma feature existente: `fix/XX`.
- Outras situações...

## Flow
O código flui da seguinte maneira:

<table>
  <tbody>
    <tr>
      <td>feature/XX</td> <td>⇨</td> <td>develop</td> <td>⇨</td> <td>production</td>
    </tr>
    <tr>
      <td>fix/XX</td> <td>⇨</td> <td>⇧</td>
    </tr>
    <tr>
      <td>etc</td> <td>⇨</td> <td>⇧</td>
    </tr>
  </tbody>
</table>

### Exemplos
#### A) Adicionar uma nova feature (ex: notificações push)
1. Fazer pull do main mais recente: `git pull origin develop`.
2. Criar o meu feature branch: `git checkout -b feature/push-notifications`.
3. Escrever código, adicionar commits etc...
5. Abrir Pull Request `feature/push-notifications` -> `develop`.
6. Discutir PR, alterar branch, etc...
7. Se PR foi aprovado: merge to `develop`.

#### B) Arranjar bug/crash no main (ex: issue #XX - user crashes on login)
1. Fazer pull do main mais recente: `git pull origin develop`.
2. Criar o meu fix branch com o numero do issue se existir: `git checkout -b fix/XX-login-crash`.
3. Escrever código, adicionar commits etc...
5. Abrir Pull Request `fix/XX-login-crash` -> `develop`.
6. Discutir PR, alterar branch, etc...
7. Se PR foi aprovado: merge to `develop`.

#### C) Criar uma release a partir do main
2. Abrir PR para o `production`.
4. Quando o PR for aprovado, merge to `production`.