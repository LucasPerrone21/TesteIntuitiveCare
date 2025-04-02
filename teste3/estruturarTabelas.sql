CREATE TABLE IF NOT EXISTS "tbl_plano_dados" (
    "id" SERIAL PRIMARY KEY,
    "data" DATE NOT NULL,
    "reg_ans" VARCHAR(8) NOT NULL,
    "cd_conta_contabil" VARCHAR(9) NOT NULL,
    "descricao" VARCHAR(150) NOT NULL,
    "vl_saldo_inicial" NUMERIC(20,2) NOT NULL,
    "vl_saldo_final" NUMERIC(20,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS "tbl_operadoras_registro_ativo"(
    "id" SERIAL PRIMARY KEY,
    "reg_operadora" VARCHAR(6),
    "cnpj" VARCHAR(14),
    "razao_social" VARCHAR(140),
    "nome_fantasia" VARCHAR(140),
    "modalidade" VARCHAR(140),
    "logradouro" VARCHAR(40),
    "numero" VARCHAR(20),
    "complemento" VARCHAR(40),
    "bairro" VARCHAR(30),
    "cidade" VARCHAR(30),
    "uf" VARCHAR(2),
    "cep" VARCHAR(8),
    "ddd" VARCHAR(4),
    "telefone" VARCHAR(20),
    "fax" VARCHAR(20),
    "endereco_eletronico" VARCHAR(255),
    "representante" VARCHAR(50),
    "cargo_representante" VARCHAR(40),
    "regiao_de_comercializacao" INTEGER,
    "data_registro_ans" DATE
);