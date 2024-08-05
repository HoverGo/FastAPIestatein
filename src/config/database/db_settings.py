DB_USER = "postgres"
DB_PASSWORD = "SideGame"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "apihouse"

# Константа, содержащая актуальную ссылку на базу данных
DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
