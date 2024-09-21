import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import Mapped
from sqlalchemy import create_engine
from sqlalchemy import select

Base = automap_base()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

Base.prepare(autoload_with=engine, schema="sampled")


Empresa = Base.classes.empresas
Municipio = Base.classes.municipios
Estabelecimento = Base.classes.estabelecimentos
Cnae = Base.classes.cnaes

# estabelecimento cnae is not mapped automatically
# because it doesn't have a primary key
class EstabelecimentoCnae(Base):
    __tablename__ = "estabelecimento_cnaes"
    cnpj: Mapped[int]
    id: Mapped[int]
    dv: Mapped[int]
    cnae: Mapped[int]
    primario: Mapped[bool]


# Example queries

# session = Session(engine)

# query = select(Cnae)

# res = session.execute(query).scalars().all()

# for i in res:
#     print(i.id, i.description)
