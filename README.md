# MBA - Arquitetura Full Cycle - Design Patterns

## SOLID e Design Patterns com python

## Visão Geral do Projeto

O projeto de geração de faturas tem como objetivo fornecer uma solução para a criação de faturas relacionadas a contratos de pagamento. O contrato define os termos e condições do pagamento, e a fatura é gerada com base nesse contrato.

Existem duas formas de geração de faturas:

- **Pagamento à vista**: Nesse caso, a fatura é gerada com o valor total do contrato a ser pago de uma só vez.

- **Pagamento parcelado**: Nesse caso, a fatura é gerada com o valor total do contrato dividido em parcelas. Cada parcela possui uma data de vencimento e um valor específico.

A geração das faturas segue os padrões de projetos mencionados anteriormente, garantindo uma arquitetura flexível, modular e de fácil manutenção.

## Arquitetura do Projeto

A arquitetura do projeto segue uma abordagem baseada em camadas, com a separação clara das responsabilidades. A estrutura do projeto é organizada da seguinte forma:

- Camada de Aplicação: Responsável por lidar com a interação do usuário e a lógica da aplicação. Nesta camada, são implementados os controladores, as rotas e as views da interface web. Ela se comunica com a camada de domínio para executar as operações necessárias.

- Camada de Domínio: Contém as regras de negócio e as entidades do domínio. Aqui são implementados os contratos, as faturas e as operações relacionadas a eles.

- Camada de Infraestrutura: Responsável pela comunicação com elementos externos, como bancos de dados e serviços de terceiros. Aqui são implementados os adaptadores para acesso aos dados e a integração com o Kafka.

## Requisitos do Projeto

Os requisitos do projeto de geração de faturas são os seguintes:

1. O sistema deve permitir a criação de contratos relacionados a pagamentos.
2. Os contratos devem conter informações sobre o valor a ser pago, as datas de vencimento e outras informações relevantes.
3. O sistema deve ser capaz de gerar faturas com base nos contratos existentes.
4. As faturas podem ser geradas tanto com pagamento à vista quanto parcelado.
5. No caso de pagamento parcelado, o sistema deve calcular o valor de cada parcela e definir suas respectivas datas de vencimento.
6. As faturas geradas devem ser armazenadas e disponibilizadas para consulta.
7. O sistema deve permitir a visualização das faturas geradas, bem como a busca por faturas específicas.

## Design e Implementação

O design e a implementação do projeto de geração de faturas seguem as práticas e os padrões de projetos mencionados anteriormente. A estrutura do código-fonte é organizada de forma modular e coesa, facilitando a compreensão e a manutenção do sistema.

A comunicação entre as diferentes camadas do sistema é realizada através de interfaces bem definidas, seguindo o princípio de inversão de dependência. Isso permite uma maior flexibilidade na substituição de componentes e facilita os testes unitários.

As bibliotecas Flask e Kafka são utilizadas para fornecer a infraestrutura necessária para a criação da interface web e o processamento assíncrono de eventos, respectivamente.

## Metodologia e Design

O projeto adota as seguintes metodologias e design:


**DDD (Domain-Driven Design):** O projeto segue os princípios e conceitos do Domain-Driven Design (DDD), alinhando o design do software com as necessidades do domínio do problema. Isso promove uma melhor compreensão do negócio, modularidade e reutilização de código.


**SOLID:** Os princípios SOLID são aplicados no design do projeto, visando a criação de código coeso, flexível e de fácil manutenção. São seguidos os princípios SRP (Single Responsibility Principle), OCP (Open-Closed Principle), LSP (Liskov Substitution Principle), ISP (Interface Segregation Principle) e DIP (Dependency Inversion Principle). Isso garante a escalabilidade e extensibilidade do sistema.

**Code Review:** O projeto adota a prática de revisão de código, em que os desenvolvedores revisam e discutem o código uns dos outros. Isso contribui para a identificação de problemas, melhoria da qualidade do código e compartilhamento de conhecimento.

**PR (Pull Request) Request Template:** É utilizado um template de Pull Request para facilitar o processo de revisão de código. Esse template fornece um guia para documentar as alterações realizadas, os testes efetuados e outras informações relevantes.

**Conventional Commits:** O padrão de mensagens de commit Conventional Commits é adotado no projeto. Isso padroniza as mensagens de commit e facilita a geração de changelogs automáticos.

### Padrões de Projetos Utilizados

O projeto utiliza os seguintes padrões de projetos:

- **DTO (Data Transfer Object)**: Utilizado para transferir dados entre as diferentes camadas do sistema, encapsulando os dados em objetos simples e independentes da lógica de negócio.

- **Repository**: Utilizado para abstrair o acesso aos dados, fornecendo uma interface comum para interagir com o banco de dados, desacoplando a lógica de negócio da implementação específica do mecanismo de armazenamento.

- **Adapter**: Utilizado para adaptar a interface de uma classe existente para uma nova interface, permitindo que classes incompatíveis trabalhem juntas sem modificar o código existente.

- **Presenter**: Utilizado para separar a lógica de apresentação da lógica de negócio, recebendo os dados do domínio e transformando-os em uma forma adequada para serem exibidos na interface do usuário.

- **Factory**: Utilizado para encapsular a lógica de criação de objetos complexos, fornecendo uma interface para criar objetos de diferentes tipos e ocultando a lógica de criação.

- **Mediator**: Utilizado para facilitar a comunicação entre diferentes componentes do sistema, definindo um objeto centralizado responsável por coordenar e controlar a interação entre os componentes, reduzindo o acoplamento e promovendo a flexibilidade.

### Bibliotecas Utilizadas

O projeto de geração de faturas utiliza as seguintes bibliotecas:

- Flask: Biblioteca em Python utilizada para desenvolvimento de aplicações web, fornecendo uma estrutura simples e flexível para criar aplicativos web eficientes e escaláveis.

- Kafka: Plataforma de streaming distribuído utilizada para criação e processamento de streams de dados em tempo real. É utilizado neste projeto para o process


> ## Instalação

Download do projeto

```bash
git clone https://github.com/candidosouza/mba_fc_design_patterns.git && cd mba_fc_design_patterns
```

docker

```bash
docker-compose up -d
```

entrar no container kafka
```bash
docker compose exec kafka bash
```

criar o tópico
```bash
kafka-topics --create --bootstrap-server=kafka:9092 --topic=invoices_generated --partitions=3
```

criar o consumer
```bash
kafka-console-consumer --bootstrap-server=kafka:9092 --topic=invoices_generated
```

entrar no container app
```bash
docker compose exec app bash
```

rodar a migração
```bash
python src/core/invoice/infra/migrations/migrate.py

```

rodar flask

```bash
python ./src/core/app.py
```

no navegador

GET

```bash
http://localhost:8000/generate_invoices/?month=1&year=2022&type=accrual
```

POST

```bash
http://localhost:8000/generate_invoices/

{
    "month": 1,
    "year": 2022,
    "type": "accrual"
}

ou 

{
    "month": 1,
    "year": 2022,
    "type": "cash"
}
```

> ## Docs

[Padrões de projetos usados](https://github.com/candidosouza/mba_fc_design_patterns/blob/main/resources/patterns.md)


[Padrões de projetos para aplicações Enterprises](https://github.com/candidosouza/mba_fc_design_patterns/blob/main/resources/patterns_of_Enterprise_application_architecture.md)

## Manutenção e Suporte
Este projeto consiste apenas em estudo e NÃO possui manutenção e suporte.

## Contribuição
Este projeto consiste apenas em estudo e NÃO aceita contribuições.

## Licença
Este projeto consiste apenas em estudo e NÃO possui licença.

## Conclusão

O projeto de geração de faturas é uma aplicação de estudo que utiliza padrões de projetos e boas práticas de desenvolvimento. Ele visa fornecer uma solução flexível, modular e de fácil manutenção para a geração de faturas relacionadas a contratos de pagamento.

A aplicação dos padrões de projetos, a adoção das metodologias e a utilização das bibliotecas mencionadas contribuem para a criação de um sistema robusto, escalável e de alta qualidade.
