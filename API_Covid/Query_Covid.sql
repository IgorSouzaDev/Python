-- Selecionar oS 10 Estado e a cidade com mais casos confirmados
SELECT  state,city,max(last_available_confirmed) Confirmados
FROM covid.stg_covid
GROUP BY state,city
ORDER BY Confirmados DESC LIMIT 10


--Calcular os casos confirmados  por estado
SELECT state,SUM(last_available_confirmed) Confirmados
FROM covid.stg_covid
GROUP BY state
ORDER BY Confirmados DESC

--Messes que tiveram mais casos confirmados


