-- Selecionar o Estado e a cidade com mais casos confirmados
SELECT  state,city,max(confirmed) FROM covid.stg_covid
GROUP BY state,city order by max desc limit 1

--Calcular o total de casos por estado
SELEC state,confir
