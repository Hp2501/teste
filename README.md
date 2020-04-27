# teste

# Gerando changelog com o Towncrier

* [Link Pypi Towncrier](https://pypi.org/project/towncrier/)

O Towncrier possui alguns tipos de changelogs, significados pela extensão do arquivo. Esses são:

```
.feature: significando um novo recurso.
.bugfix: significando uma correção de bug.
.doc: significando uma melhoria na documentação.
.removal: significando uma descontinuação ou remoção da API pública.
.misc: um ticket foi fechado, mas não interessa aos usuários.
```
Exemplo de um arquivo 25.feature, em que 25 é o número da issue e .feature e o tipo de issue, 
se deseja incluir algum texto no changelog ao lado da issue basta colocar dentro do arquivo.
A versão será lida em __init__ dentro de changes