# MBA - Arquitetura Full Cycle - Colaboradores FC

> ## SOLID e Design Patterns com python


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

* Autopep8
* Pylint
* pytest
* pytest-cov
* psycopg2
* python-dateutil
* Flask


> ## Instalação

Download do projeto

```bash
git clone https://github.com/candidosouza/mba_fc_design_patterns.git && cd mba_fc_design_patterns
```

docker

```bash
docker-compose up -d
```

entrar no container
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

> ## Estudo/Projeto em desenvolvimento...

...