
# Code-Wars-II
___

## Projeto em equipe do Bootcamp Código[s] - Stone

#### Equipe 10

* Ligia de Oliveira
* Marcelo Lopes Valerio
* William Machado
* Larissa Chagas
* Lucas Valença
<h2 align="left"> Tabela de conteudo </h2>

  - [Definições do Projeto](#Definições-do-Projeto)
  - [Organizaçao Base de Dados](#Organizaçao-Base-de-Dados)
  
  
### Definições do Projeto

Implementar um sistema em python que cadastre holerites de funcionários, apresentando, para cada mês registrado, faltas, salário, comissão, e calculando descontos como INSS e IRRF. Após isso, salvá-las em um banco de dados MySQL, que possua informações sobre os cargos da empresa, e dos funcionários, além de permitir a alteração dos dados dos funcionários.

O programa possui como entrada as seguintes informações do funcionário: CPF, nome, data de admissão, código do cargo, e se ele recebe ou não a comissão, e, de acordo com as requisições do usuário, pode realizar alterações na base de dados, linkar dados de cargo com funcionário, e alterar o cargo do funcionário, por exemplo. Além disso, pode printar, no terminal python, uma holerite com os dados esquematizados. O programa gera automaticamente um numero de matricula para funcionários cadastrados,
servindo como chave primária para o MySQL

### Base de Dados 

**Para rodar o sistema, primeiramente é necessario gerar a base de dados, rodando o código disponibilizado na pasta SQL, e, após isso, colocar o cadastro do seu SQL na função conectar().**

A organização do cogigo e da base de dados encontras-se representados nas imagens abaixo

<p align="center">
<a><img src=https://user-images.githubusercontent.com/86573930/176080165-9f4ff77a-ca42-4591-a1a3-0258e90b6631.png  width="400px" ></a>
</p>
<p align="center">
<a><img src=https://user-images.githubusercontent.com/86573930/176080180-2adc5926-0874-4500-b8c2-629ed99434cc.PNG  width="400px" ></a>
</p>

### Codigo
- input
  ````

  ````

- terminal output
````
informe o mes do holerite(em numero)5
quantas faltas?2
+----+-------------+-------------------------+-------------+--------------------+-----------------------------+
|    |   Matricula | Nome                    |         CPF | Data de admissao   | Cargo                       |
|----+-------------+-------------------------+-------------+--------------------+-----------------------------|
|  0 |      100047 | Daiana Santana de Sousa | 11111111100 | 2002-04-09         | Desenvolvedor Mobile Sênior |
+----+-------------+-------------------------+-------------+--------------------+-----------------------------+
==========May/2022========
+----+----------------+--------------+-------------------+--------------------+
|    | Descrição      | Referência   | Provento          | Desconto           |
|----+----------------+--------------+-------------------+--------------------|
|  0 | Salário Base   | 22,5         | 6700.0            |                    |
|  1 | Comissão       | 7.0          | 469.0             |                    |
|  2 | Faltas         | 2            |                   | 446.6666666666667  |
|  3 | INSS Folha     | 0.14         |                   | 828.39             |
|  4 | IRRF Folha     | 0.275        |                   | 745.33             |
|  5 | Total          |              | 7169.0            | 2020.3866666666668 |
|  6 | liq. a receber |              | 5148.613333333333 |                    |
+----+----------------+--------------+-------------------+--------------------+
+----+------------------+------------------+---------------+------------------+
|    |   Base calc INSS |   Base calc FGTS |   FGTS do mês |   Base calc IRRF |
|----+------------------+------------------+---------------+------------------|
|  0 |             7169 |             7169 |        573.52 |          6340.61 |
+----+------------------+------------------+---------------+------------------+
````

