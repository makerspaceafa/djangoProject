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