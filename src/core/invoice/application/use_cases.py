import psycopg2
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GenerateInvoices:
    def execute(self):
        conection = psycopg2.connect(
            host='db',
            database='invoices',
            user='postgres',
            password='root'
            )
        conection.cursor()
        contracts = conection.execute("SELECT * FROM invoices.contracts")
        print("###############################################")
        print("\n")
        print('Conn', conection)
        print("\n")
        print("###############################################")
