-- gera uid para dados novos
ALTER TABLE estabelecimentos
ADD COLUMN uid UUID DEFAULT gen_random_uuid();

-- popula os dados antigos com uids (executar somente 1 vez)
UPDATE estabelecimentos
SET uid = gen_random_uuid()
WHERE uid IS NOT NULL;

-- preenche cnpj com zeros à esquerda
UPDATE estabelecimentos
SET cnpj = LPAD(cnpj::text, 8, '0')
WHERE LENGTH(cnpj::text) < 8;

-- transforma para varchar
ALTER TABLE estabelecimentos
ALTER COLUMN cnpj TYPE VARCHAR(8);


-- preenche dv com zeros à esquerda
UPDATE estabelecimentos
SET dv = LPAD(dv::text, 2, '0')
WHERE LENGTH(dv::text) < 2;

--transforma para varchar
ALTER TABLE estabelecimentos
ALTER COLUMN dv TYPE VARCHAR(2);

-- preenche id com zeros à esquerda
UPDATE estabelecimentos
SET id = LPAD(id::text, 4, '0')
WHERE LENGTH(id::text) < 4;

--transforma para varchar
ALTER TABLE estabelecimentos
ALTER COLUMN id TYPE VARCHAR(4);


--transforma em null os dds e telefones = '0'
UPDATE estabelecimentos
SET 
    ddd_1 = NULLIF(ddd_1, '0'),
    ddd_2 = NULLIF(ddd_2, '0')
    telefone_1 = NULLIF(telefone_1, '0'),
    telefone_2 = NULLIF(telefone_2, '0')
WHERE 
    telefone_1 = '0' OR
    telefone_2 = '0' OR
    ddd_1 = '0' OR
    ddd_2 = '0';


-- adiciona colunas latitude e longitude
ALTER TABLE estabelecimentos
ADD COLUMN latitude FLOAT8, --double precision (ideal)
ADD COLUMN longitude FLOAT8;

-- preenche cep com zeros à esquerda 
UPDATE estabelecimentos
SET cep = LPAD(cep::text, 8, '0')
WHERE LENGTH(cep::text) < 8;

-- transforma data_inicio_atividade para formato TO_DATE
UPDATE estabelecimentos
SET data_inicio_atividade = TO_DATE(data_inicio_atividade, 'YYYYMMDD')
WHERE data_inicio_atividade ~ '^\d{8}$';

-- altera o tipo de dado para DATE
ALTER TABLE estabelecimentos
ALTER COLUMN data_inicio_atividade TYPE DATE
USING TO_DATE(data_inicio_atividade, 'YYYYMMDD');

--Remove
ALTER TABLE estabelecimentos
DROP COLUMN ddd_2;

ALTER TABLE estabelecimentos
DROP COLUMN telefone_2;

ALTER TABLE estabelecimentos
DROP COLUMN telefone_fax;

ALTER TABLE estabelecimentos
DROP COLUMN ddd_fax;

ALTER TABLE estabelecimentos
DROP COLUMN data_situacao_especial;

ALTER TABLE estabelecimentos
DROP COLUMN situacao_especial;

ALTER TABLE estabelecimentos
DROP COLUMN motivo_situacao_cadastral;

ALTER TABLE estabelecimentos
DROP COLUMN nome_cidade_exterior;

ALTER TABLE estabelecimentos
DROP COLUMN data_situacao_cadastral;



