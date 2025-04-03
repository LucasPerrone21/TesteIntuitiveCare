CREATE TEMP TABLE temp_operadoras_registro_ativo (
    reg_operadora TEXT,
    cnpj TEXT,
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf TEXT,
    cep TEXT,
    ddd TEXT,
    telefone TEXT,
    fax TEXT,
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao TEXT,
    data_registro_ans TEXT
);


COPY temp_operadoras_registro_ativo FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta2\Relatorio_cadop.csv' 
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ';',
    ENCODING 'UTF8'
);

INSERT INTO tbl_operadoras_registro_ativo (
    reg_operadora, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, 
    bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, 
    cargo_representante, regiao_de_comercializacao, data_registro_ans
)
SELECT 
    reg_operadora,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    CAST(NULLIF(regiao_de_Comercializacao, '') AS INTEGER),
    CAST(NULLIF(data_registro_ans, '') AS DATE)
FROM temp_operadoras_registro_ativo;







