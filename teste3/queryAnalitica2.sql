WITH filtro_trimestre AS (
    SELECT 
        reg_ans, 
        SUM(vl_saldo_final) AS total_despesas
    FROM tbl_plano_dados
    WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND data >= '2024-01-01' AND data <= '2024-12-31'
    GROUP BY reg_ans
)
SELECT 
    o.razao_social, 
    f.total_despesas
FROM filtro_trimestre f
JOIN tbl_operadoras_registro_ativo o ON f.reg_ans = o.reg_operadora
ORDER BY f.total_despesas DESC
LIMIT 10;