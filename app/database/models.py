from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

#Opcao 1 - Nova coluna - ID unico
estabelecimento_cnae = Table(
    "estabelecimento_cnaes",
    Base.metadata,
    Column("estabelecimento_uid", ForeignKey("estabelecimentos.uid"), primary_key=True),
    Column("cnae_id", ForeignKey("cnaes.cnae_id"), primary_key=True),
    Column("primario",Boolean, nullable=False)
)
    

class Estabelecimento(Base):
    __tablename__ = "estabelecimentos"

    uid: Mapped[str] = mapped_column(primary_key = True)
    cnpj: Mapped[str] = mapped_column(ForeignKey("empresas.cnpj"))
    id: Mapped[str]
    dv: Mapped[str]
    municipio_id: Mapped[str] = mapped_column(ForeignKey("municipios.municipio_id"))
    matriz: Mapped[bool|None]
    nome_fantasia: Mapped[str|None]
    situacao_cadastral: Mapped[int|None]
    pais: Mapped[str|None]
    data_inicio_atividade: Mapped[datetime|None]
    tipo_logradouro: Mapped[str|None]
    logradouro: Mapped[str|None]
    numero: Mapped[str|None]
    complemento: Mapped[str|None]
    bairro: Mapped[str|None]
    cep: Mapped[str|None]
    uf: Mapped[str|None]
    ddd_1: Mapped[str|None]
    telefone_1: Mapped[str|None]
    email: Mapped[str|None]
    latitude: Mapped[float|None]
    longitude: Mapped[float|None]
    
    cnaes: Mapped[List["Cnae"]] = relationship(
        secondary=estabelecimento_cnae
    )
    
class Municipio(Base):
    __tablename__ = "municipios"
    
    municipio_id: Mapped[str] = mapped_column(primary_key=True)
    nome: Mapped[str]
    
class Empresa(Base):
    __tablename__ = "empresas"
    
    estabelecimentos: Mapped[List["Estabelecimento"]] = relationship(back_populates=True)
    cnpj: Mapped[str] = mapped_column(primary_key=True)
    razao_social: Mapped[str|None]
    natureza_juridica: Mapped[int|None]
    porte: Mapped[int|None]
    

class Cnae(Base):
    
    __tablename__ = "cnaes"
    
    cnae_id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str|None]
    macro_categoria: Mapped[str|None]
    
    estabelecimentos: Mapped[List["Estabelecimento"]] = relationship(
        secondary=estabelecimento_cnae
    )    
    