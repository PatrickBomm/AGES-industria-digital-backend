import app.scripts.sample_models as sample_models
from sqlalchemy import select
import app.database.models as models

# Transferindo os dados
def transfer_data():
    
    cnaes_query = select(sample_models.Cnae)

    cnaes = sample_models.session.execute(cnaes_query).scalars().all()

    for i in cnaes:
        cnae = models.Cnae(
            cnae_id = i.id,
            descricao = i.description
            # macro_categoria = 
        )
        
    models.session.commit()
    
    
    
    municipios_query = select(sample_models.Municipio)
    
    municipios = sample_models.session.execute(municipios_query).scalars().all()
    
    for i in municipios:
        municipio = models.Municipio(
            municipio_id = i.id,
            nome = i.name
        )
        
    models.session.commit()
    
    
    
    empresas_query = select(sample_models.Empresa)

    empresas = sample_models.session.execute(empresas_query).scalars().all()
    
    for i in empresas:
        empresa = models.Empresa(
            cnpj = i.cnpj,
            razao_social = i.razao_social,
            natureza_juridica = i.natureza_juridica,
            porte = i.porte
        )
        
    models.session.commit()
    
    
    
    estabelecimentos_query = select(sample_models.Estabelecimento)
    
    estabelecimentos = sample_models.session.execute(estabelecimentos_query).scalars().all()
    
    for i in estabelecimentos:
        estabelecimento = models.Estabelecimento(
            uid = i. ,
            cnpj = i. ,
            id = i. ,
            dv = i. , 
            municipio_id = i. ,
            matriz = i. ,
            nome_fantasia = i. ,
            situacao_cadastral = i. ,
            pais = i. ,
            data_inicio_atividade = i. ,
            tipo_logradouro = i. ,
            logradouro = i. ,
            numero = i. ,
            complemento = i. ,
            bairro = i. ,
            cep = i. ,
            uf = i. ,
            ddd_1 = i. ,
            telefone_1 = i. ,
            email = i. ,
            latitude = i. ,
            longitude = i. 
        )
    
## criar conexão de transferencia de dados para com a tabela associativa estabelecimento_cnae

## fazer tratamentos de colunas inline (ver sql_files)


    

