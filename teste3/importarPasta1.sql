CREATE TEMP TABLE temp_plano_dados (
    data TEXT,
    reg_ans TEXT,
    cd_conta_contabil TEXT,
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\1T2023.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\1T2024.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\2T2023.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\2T2024.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\3T2023.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\3T2024.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\4T2023.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');
COPY temp_plano_dados FROM 'C:\Users\lucas\Desktop\TesteIntuitiveCare\teste3\pasta1\4T2024.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', ENCODING 'UTF8');

INSERT INTO tbl_plano_dados (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SELECT 
    data::DATE,  
    reg_ans,
    cd_conta_contabil,
    descricao,
    TO_NUMBER(REPLACE(vl_saldo_inicial, ',', '.'), '99999999999999999999.99'),
    TO_NUMBER(REPLACE(vl_saldo_final, ',', '.'), '99999999999999999999.99')
FROM temp_plano_dados;