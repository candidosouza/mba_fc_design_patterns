from dataclasses import dataclass, field
# import mysql.connector
from core.invoice.infra.database.database_adapter import DatabaseAdapter


@dataclass(slots=True, kw_only=True, frozen=True)
class MySqlAdapter(DatabaseAdapter):
    db_type: str = field(init=False, default="mysql")
    host: str
    port: str
    database: str
    user: str
    password: str
    connection = None

    # def connect(self):
    #     try:
    #         self.connection = mysql.connector.connect(
    #             host=self.host,
    #             port=self.port,
    #             database=self.database,
    #             user=self.user,
    #             password=self.password
    #         )
    #         print("Conexão com o MySQL estabelecida!")
    #     except mysql.connector.Error as e:
    #         print(f"Erro ao conectar ao MySQL: {e}")

    # def execute_query(self, query):
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute(query)
    #         self.connection.commit()
    #         print("Consulta executada com sucesso no MySQL!")
    #     except mysql.connector.Error as e:
    #         print(f"Erro ao executar a consulta no MySQL: {e}")

    # def close_connection(self):
    #     if self.connection:
    #         self.connection.close()
    #         print("Conexão com o MySQL fechada.")
