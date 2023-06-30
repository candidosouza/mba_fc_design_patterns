# MBA - Arquitetura Full Cycle - Design Patterns

## SOLID e Design Patterns com python


> ## Metodologias e Designs

* DDD
* SOLID
* Code Review
* PR Request Template
* Conventional Commits


> ## Design Patterns
* DTO
* Repository
* Adapter
* Presenter
* Factory
* Mediator

> ## Bibliotecas e Ferramentas

* Flask
* kafka


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