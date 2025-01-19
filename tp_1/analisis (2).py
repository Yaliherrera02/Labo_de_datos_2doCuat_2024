#%%%
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
from   matplotlib import ticker
import seaborn as sns
#%%
ruta  = '~/Documents/FACULTAD_2024/Labo_de_datos_2doCuat_2024/tp_1//enunciado_tablas/'

equipo_A = pd.read_csv(ruta + 'equipo_A.csv')
equipo_B = pd.read_csv(ruta + 'equipo_B.csv')
equipo_C = pd.read_csv(ruta + 'equipo_C.csv')
es_local_en = pd.read_csv(ruta + 'es_local_en.csv')
es_visitante_en = pd.read_csv(ruta + 'es_visitante_en.csv')
jugador = pd.read_csv(ruta + 'jugador.csv')
jugador_atributos = pd.read_csv(ruta + 'jugador_atributos.csv')
partido = pd.read_csv(ruta + 'partido.csv')
temporada = pd.read_csv(ruta + 'temporada.csv')
componen_plantel = pd.read_csv(ruta + 'componen_plantel.csv')
disputan = pd.read_csv(ruta + 'disputan.csv')

# 1) ¿Cuál es el equipo con mayor cantidad de partidos ganados?
query = '''SELECT b.NOMBRE, count(*) as PARTIDOS_GANADOS 
from (select ID_PARTIDO,
      case when goles_local > goles_visitante then ID_EQUIPO_LOCAL ELSE ID_EQUIPO_VISITANTE END AS GANADOR
      FROM partido a
      where ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')
      and GOLES_LOCAL <> GOLES_VISITANTE) a
join equipo_A b on a.GANADOR = b.ID_EQUIPO
where PAIS ='Belgium'
          group by 1 
          order by 2 desc
          '''
print("el equipo mas ganador es: ")
print(duckdb.sql(query))

###############################################################################

#2 ¿Cuál es el equipo con mayor cantidad de partidos perdidos de cada año?

query_1 = '''SELECT 
        b.NOMBRE, 
        ID_TEMPORADA, 
        COUNT(*) AS PARTIDOS_PERDIDOS
    FROM (
        SELECT 
            ID_PARTIDO,
            ID_TEMPORADA,
            CASE 
                WHEN goles_local > goles_visitante THEN ID_EQUIPO_VISITANTE 
                ELSE ID_EQUIPO_LOCAL 
            END AS PERDEDOR
        FROM partido a
        WHERE ID_TEMPORADA IN ('2009/2010','2010/2011','2011/2012','2012/2013')
        AND GOLES_LOCAL <> GOLES_VISITANTE
    ) a
    JOIN equipo_A b ON a.PERDEDOR = b.ID_EQUIPO
    WHERE PAIS = 'Belgium'
    GROUP BY b.NOMBRE, ID_TEMPORADA
'''
query_2 = f'''SELECT 
    NOMBRE, 
    ID_TEMPORADA, 
    PARTIDOS_PERDIDOS
FROM (
    SELECT 
        NOMBRE, 
        ID_TEMPORADA, 
        PARTIDOS_PERDIDOS,
        ROW_NUMBER() OVER (PARTITION BY ID_TEMPORADA ORDER BY PARTIDOS_PERDIDOS DESC) AS RANK
    FROM ({query_1})
) ranked_teams
WHERE RANK = 1
ORDER BY ID_TEMPORADA DESC
'''

print("los equipos que mas partidos perdieron en cada año son: ")
print(duckdb.sql(query_2))

###############################################################################

#3 ¿Cuál es el equipo con mayor cantidad de partidos empatados en el último año?

query1c = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')
                    
#Obtengo los equipos de Belgica solamente.

query2c = duckdb.sql(      '''
                          Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                          From partido 
                          INNER JOIN query1c as EQUIPOS_BELGAS
                          ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                          Order By ID_EQUIPO_LOCAL asc;
                          ''')
                          
#Obtengo todos los datos q necesite de los equipos belgas.

query3c = duckdb.sql('''
                       Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, (Case When GOLES_LOCAL = GOLES_VISITANTE
                                                                                               Then ID_EQUIPO_LOCAL
                                                                                               Else NULL
                                                                                               END) As EMPATE
                       From query2c
                       Where ID_TEMPORADA = '2012/2013';
                       ''')
                       
#Diferencio entre los partidos en donde hubo empates y los q no.

query4c = duckdb.sql('''
                    Select *
                    From query3c as q3c
                    INNER JOIN query2c as q2c
                    ON q3c.ID_PARTIDO = q2c.ID_PARTIDO
                    and
                    q3c.EMPATE = q2c.ID_EQUIPO_LOCAL;
                    ''')

#Obtengo los partidos en donde si hubo empates.

query5c = duckdb.sql ('''
                     Select ID_EQUIPO_LOCAL, Count (*) as Empate_local
                     From query4c
                     Group By ID_EQUIPO_LOCAL;
                     ''')
                     
#Ordeno la cantidad de partidos empatados q tuvieron los equipos q jugaron de local.

query6c = duckdb.sql ('''
                     Select ID_EQUIPO_VISITANTE, Count (*) as Empate_visitante
                     From query4c
                     Group By ID_EQUIPO_VISITANTE;
                     ''')
                     
#Ordeno la cantidad de partidos empatados q tuvieron los equipos q jugaron de visitante.

query7c = duckdb.sql ('''
                     Select *
                     From query5c
                     INER JOIN query6c 
                     ON ID_EQUIPO_LOCAL = ID_EQUIPO_VISITANTE;
                     ''')
                     
#Junto sus tablas.

query8c = duckdb.sql ('''
                     Select ID_EQUIPO_LOCAL as Id_equipo, (Case When ID_EQUIPO_LOCAL = ID_EQUIPO_VISITANTE
                                                           Then Empate_local + Empate_visitante
                                                           END) as Empates_total
                     From query7c
                     Order By Empates_total asc;
                     ''')

#Obtengo la cantidad de partidos empatados en total por los equipos

query9c = duckdb.sql ('''
                     Select MAX(Empates_total) as Maxima_cantidad_de_empates
                     From query8c;
                     ''')

query10c = duckdb.sql ('''
                      Select Id_equipo, Empates_total
                      From query8c as q8c
                      INNER JOIN query9c as q9c
                      ON q8c.Empates_total = q9c.Maxima_cantidad_de_empates;
                      ''')
                      
                      
#Los q mas empataron entre los partidos de local y visitante.

query11c = duckdb.sql ('''
                      Select MAX(Empate_local) as Maxima_cantidad_de_empates_local
                      From query5c;
                      ''')

query12c = duckdb.sql ('''
                      Select ID_EQUIPO_LOCAL as Id_equipo, Empate_local as Empates_total
                      From query5c as q5c
                      INNER JOIN query11c as q11c
                      ON q5c.Empate_local = q11c.Maxima_cantidad_de_empates_local;
                      ''')

#Los q mas veces empataron de local.

query13c = duckdb.sql ('''
                      Select MAX(Empate_visitante) as Maxima_cantidad_de_empates_visitante
                      From query6c;
                      ''')

query14c = duckdb.sql ('''
                      Select ID_EQUIPO_VISITANTE as Id_equipo, Empate_visitante as Empates_total
                      From query6c as q6c
                      INNER JOIN query13c as q13c
                      ON q6c.Empate_visitante = q13c.Maxima_cantidad_de_empates_visitante;
                      ''')
#Los q mas veces empataron de visitante.

query15c = duckdb.sql ('''
                      Select *
                      From query10c
                      Union
                      Select *
                      From query12c
                      Union
                      Select *
                      From query14c;
                      ''')

#Unimos todo para saber quien fue el q mas veces empato en total, ya q un equipo 
#podria haber empatado mucho de visitante y nada de local por ejemplo.

query16c = duckdb.sql ('''
                      Select MAX(Empates_total) as Maxima_cantidad_de_empates
                      From query15c;
                      ''')

query17c = duckdb.sql ('''
                      Select Id_equipo, Empates_total
                      From query15c as q15c
                      INNER JOIN query16c as q16c
                      ON q15c.Empates_total = q16c.Maxima_cantidad_de_empates;
                      ''')

query18c = duckdb.sql ('''
                      Select NOMBRE, Empates_total
                      From query17c as q17c
                      INNER JOIN equipo_A as Equipos
                      ON q17c.Id_equipo = Equipos.ID_EQUIPO;
                      ''')
print("el equipo con mayor cantidad de partidos empatados en el último año es:  ")
print(query18c)
###############################################################################

#4 ¿Cuál es el equipo con mayor cantidad de goles a favor?

query1d = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2d = duckdb.sql('''
                    Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                    From partido 
                    INNER JOIN query1d as EQUIPOS_BELGAS
                    ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_EQUIPO_LOCAL asc;
                    ''')
                          
#Obtengo todos los datos q necesite de los equipos belgas.

query3d = duckdb.sql ('''
                     Select ID_EQUIPO_LOCAL as Equipo, SUM(GOLES_LOCAL) as Goles_hechos
                     From query2d
                     Group By ID_EQUIPO_LOCAL
                     Order By ID_EQUIPO_LOCAL asc;
                     ''')
                     
#Goles q metierons los equipos q jugaron de local.                     

query4d = duckdb.sql ('''
                     Select ID_EQUIPO_VISITANTE as Equipo, SUM(GOLES_VISITANTE) as Goles_hechos
                     From query2d
                     Group By ID_EQUIPO_VISITANTE
                     Order By ID_EQUIPO_VISITANTE asc;
                     ''')

#Goles q metieron los equipos q jugaron de visitante.

query5d = duckdb.sql ('''
                     Select * 
                     From query3d
                     UNION ALL
                     Select * 
                     From query4d;
                     ''')

#Unimos todos los goles de los equipos en una sola tabla.

query6d = duckdb.sql ('''
                     Select Equipo, SUM (Goles_hechos) as Goles_totales_hechos
                     From query5d
                     Group By Equipo
                     Order By Goles_totales_hechos desc;
                     ''')

#Terminamos de sumarlos.

query7d = duckdb.sql ('''
                     Select Max(Goles_totales_hechos) as Maxima_cantidad_de_goles_que_hizo_un_equipo
                     From query6d;
                     ''')
                     
#Maxima cantidad de goles que hizo un equipo.

query8d = duckdb.sql ('''
                     Select Equipo, Goles_totales_hechos
                     From query6d as q6d
                     INNER JOIN query7d as q7d
                     ON q6d.Goles_totales_hechos = q7d.Maxima_cantidad_de_goles_que_hizo_un_equipo;
                     ''')
                     
#Obtengo el ID del equipo q mas goles metio.

query9d = duckdb.sql ('''
                     Select Nombre, Goles_totales_hechos
                     From query8d as q8d
                     INNER JOIN equipo_A 
                     ON q8d.Equipo = equipo_A.ID_EQUIPO;
                     ''')

#Obtengo el nombre del equipo apartir de su ID.
print("el equipo con mayor cantidad de goles a favor es: ")
print(query9d)
###############################################################################

#5 ¿Cuál es el equipo con mayor diferencia de goles?

query1e = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2e = duckdb.sql('''
                    Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                    From partido 
                    INNER JOIN query1e as EQUIPOS_BELGAS
                    ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_EQUIPO_LOCAL asc;
                    ''')

#Obtengo todos los datos q necesite de los equipos belgas.

query3e = duckdb.sql ('''
                     Select ID_EQUIPO_LOCAL as Equipo, SUM(GOLES_VISITANTE) as Goles_recibidos
                     From query2e
                     Group By ID_EQUIPO_LOCAL
                     Order By ID_EQUIPO_LOCAL asc;
                     ''')

#Goles q recibieron los equipos q jugaron de local.

query4e = duckdb.sql ('''
                     Select ID_EQUIPO_VISITANTE as Equipo, SUM(GOLES_LOCAL) as Goles_local
                     From query2e
                     Group By ID_EQUIPO_VISITANTE
                     Order By ID_EQUIPO_VISITANTE asc;
                     ''')

#Goles q recibieron los equipos q jugaron de visitante.

query5e = duckdb.sql ('''
                     Select * 
                     From query3e
                     UNION ALL
                     Select * 
                     From query4e;
                     ''')

#Unimos todos los goles recibidos de los equipos en una sola tabla.

query6e = duckdb.sql ('''
                     Select Equipo, SUM (Goles_recibidos) as Goles_totales_recibidos
                     From query5e
                     Group By Equipo
                     Order By Equipo asc;
                     ''')

#Terminamos de sumarlos.

query7e = duckdb.sql ('''
                     Select q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo
                     Order By q6e.Equipo asc;
                     ''')

#Ahora tenemos una tabla con todos los goles q recibio un equipo y todos los q hizo, habria q restarlos.

query8e = duckdb.sql ('''
                     Select Equipo, (Goles_totales_hechos - Goles_totales_recibidos) as Diferencia_de_gol
                     From query7e
                     Order By Equipo asc;
                     ''')

#Hago la resta asi obtengo la diferencia de gol.

query9e = duckdb.sql ('''
                     Select MAX(Diferencia_de_gol) as Maxima_diferencia_de_gol
                     From query8e;
                     ''')

#Obtengo la Maxima diferencia de gol.

query10e = duckdb.sql ('''
                      Select Equipo, Diferencia_de_gol
                      From query8e as q8e
                      INNER JOIN query9e as q9e
                      ON q8e.Diferencia_de_gol = q9e.Maxima_diferencia_de_gol;
                      ''')
                      
#Obtengo el ID del equipo con mayor diferencia de gol.

query11e = duckdb.sql ('''
                      Select NOMBRE, Diferencia_de_gol
                      From query10e as q10e
                      INNER JOIN equipo_A
                      ON q10e.Equipo = equipo_A.ID_EQUIPO;
                      ''')

#Obtengo el Nombre apartir del ID.
print("el equipo con mayor diferencia de goles es: ")
print(query11e)
###############################################################################

#6 ¿Cuántos jugadores tuvo durante el período de tiempo seleccionado cada equipo en su plantel?

query1f = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2f = duckdb.sql('''
                    Select Distinct ID_TEMPORADA, cp.ID_EQUIPO, ID_JUGADOR
                    From componen_plantel as cp
                    INNER JOIN query1f as q1f
                    ON cp.ID_EQUIPO = q1f.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_TEMPORADA asc;
                    ''')
#Filtro todo segun las temporadas y agrego los equipos para poder ver en q equipo jugo cada jugador.

query3f = duckdb.sql ('''
                     Select ID_EQUIPO, COUNT(ID_JUGADOR) as Cantidad_jugadores
                     From query2f 
                     Group By ID_EQUIPO
                     Order By ID_EQUIPO asc;
                     ''')
#Obtengo la cantidad de jugadores q pasaron por los distintos equipos.

query4f = duckdb.sql ('''
                     Select NOMBRE, Cantidad_jugadores
                     From query3f as q3f
                     INNER JOIN equipo_A 
                     ON q3f.ID_EQUIPO = equipo_A.ID_EQUIPO
                     Order By Cantidad_jugadores desc;
                     ''')

#A partir del ID del equipo obtengo su nombre.
print("la cantidad de jugadores que tuvieron los equipos en el periodo de tiempo seleccionado es:")
print(query4f)

# ¿Cuáles son los jugadores que más partido ganó su equipo?
# i) parte: obtener la suma de partidos ganado por equipo en cada semestre y temporada
query = '''
    --Cantidad de partidos ganados por equipo en cada temporada y semestre:

    SELECT a.ID_TEMPORADA,
    b.ID_EQUIPO AS ID_EQUIPO_GANADOR,
    b.NOMBRE as NOMBRE_EQUIPO_GANADOR,

    --el siguiente case lo puedo hacer porque todas las temporadas se juegan anualmente (filtre Belgica 2013/2014)
    --semestre me indica en que equipo jugó en cada mitad de temporada, lo cual es importante para contabilizar partidos ganadosw
    case when a.FECHA < (DURACION_LIGA/2)+1 then 1 else 2 end as SEMESTRE,
    count(*) as PARTIDOS_GANADOS
    FROM
    (SELECT ID_TEMPORADA,
    FECHA,
    case when GOLES_LOCAL>GOLES_VISITANTE then ID_EQUIPO_LOCAL
            when GOLES_LOCAL<GOLES_VISITANTE then ID_EQUIPO_VISITANTE
            end as EQUIPO_GANADOR,
    FROM partido
    WHERE GOLES_LOCAL <> GOLES_VISITANTE) a

    --A continuacion los siguientes joins son solo para filtrar por la liga asignada
    JOIN
    equipo_A b on b.ID_EQUIPO = a.EQUIPO_GANADOR
    JOIN
    equipo_C c on c.PAIS = b.PAIS
    and c.LIGA = 'Belgium Jupiler League'

    --A continuacion el siguiente join es para obtener la duracion de la liga en cada temporada
    JOIN
    (
    SELECT ID_TEMPORADA,
    MAX(FECHA) AS DURACION_LIGA
    FROM partido as a

    --A continuacion los siguientes joins son solo para filtrar por la liga asignada
    JOIN equipo_A b
    on b.ID_EQUIPO = a.ID_EQUIPO_LOCAL
    JOIN
    equipo_C c on c.PAIS = b.PAIS
    and c.LIGA = 'Belgium Jupiler League'
    Where ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')
    group by a.ID_TEMPORADA
    ) d
    on a.ID_TEMPORADA = d.ID_TEMPORADA
    GROUP BY ALL
    ORDER BY ALL
'''
# ii): obtener la suma historica de los partidos ganado por jugador
query = f'''
--Cantidad de partidos ganados por jugador en todas las temporadas y semestres:
SELECT NOMBRE, sum(PARTIDOS_GANADOS) as PARTIDOS_GANADOS
FROM (SELECT a.*,b.ID_JUGADOR, c.NOMBRE FROM ({query}) as a
JOIN componen_plantel as bs
on a.ID_TEMPORADA = b.ID_TEMPORADA
and a.ID_EQUIPO_GANADOR = b.ID_EQUIPO
and a.SEMESTRE=b.SEMESTRE
JOIN jugador c
on c.ID_JUGADOR = b.ID_JUGADOR
)
group by 1
order by 2 desc limit 3
'''
print("los jugadores que más partidos ganó su equipo son: ")

############################################################################################

# ¿Cuál es el jugador que estuvo en más equipos?
query = '''SELECT a.ID_JUGADOR,b.NOMBRE,COUNT(*) as numero_equipos
FROM (select distinct id_jugador,id_equipo from componen_plantel Where ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')) a
JOIN jugador b
on b.ID_JUGADOR = a.ID_JUGADOR
group by 1,2
order by 3 desc
limit 1
'''
print("el jugador que estuvo en mas equipos es: ")
print(duckdb.sql(query)) #RESPUESTA

############################################################################################

# ¿Cuál es el jugador que menor variación de potencia ha tenido a lo largo de los años?

# i) como sabemos que un jugador puede haber estado en mas de una liga hay que segmentar jugadores_atributo
#por semestre y id_temporada para filtrar solo por los que juegan en BELGICA

query=''' SELECT e.NOMBRE,
    max(potencia_maxima) as MAXIMO_HISTORICO,
    MIN(potencia_minima) as MINIMO_HISTORICO
    FROM
    (--De jugador_atributos me genero temporada y semestre para joinear con componen_plantel y filtrar por liga
        SELECT
        ID_JUGADOR,
        CASE
            WHEN CAST(SPLIT(fecha_calendario, '-')[2] AS INTEGER) >= 7 THEN 1
            ELSE 2
        END AS semestre_temporada,
        CASE
            WHEN CAST(SPLIT(fecha_calendario, '-')[2] AS INTEGER) >= 7
                THEN CONCAT(SPLIT(fecha_calendario, '-')[1], '/', CAST(CAST(SPLIT(fecha_calendario, '-')[1] AS INTEGER) + 1 AS VARCHAR))
            ELSE CONCAT(CAST(CAST(SPLIT(fecha_calendario, '-')[1] AS INTEGER) - 1 AS VARCHAR), '/', SPLIT(fecha_calendario, '-')[1])
        END AS ID_TEMPORADA,
        --maxima y minima potencia por temporada y semestre
        MAX(POTENCIA) as potencia_maxima,
        MIN(POTENCIA) as potencia_minima
        FROM jugador_atributos
        group by 1,2,3
        order by all
     ) a
    JOIN componen_plantel b
    on b.ID_TEMPORADA = A.ID_TEMPORADA
    and b.SEMESTRE = a.SEMESTRE_TEMPORADA
    and b.ID_JUGADOR = a.ID_JUGADOR
    JOIN jugador e
    on e.ID_JUGADOR = a.ID_JUGADOR

    --A continuacion los siguientes joins son solo para filtrar por la liga asignada
    JOIN equipo_A c
    on c.ID_EQUIPO = b.ID_EQUIPO
    JOIN equipo_C d
    on d.PAIS = c.PAIS
    and d.LIGA = 'Belgium Jupiler League'
    Where b.ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')
    group by all
    order by all
'''
# ii)
query = f'''select NOMBRE, MAXIMO_HISTORICO-MINIMO_HISTORICO AS DIFERENCIA_POTENCIA_HISTORICA
from ({query})
ORDER BY 2
limit 1 
'''
print("el jugador que menor variación de potencia ha tenido a lo largo de los años es: ")
print(duckdb.sql(query)) #RESPUESTA

##############################################################################

# ¿Hay algún equipo que haya sido a la vez el más goleador y el que tenga mayor valor de alguno
# de los atributos (considerando la suma de todos los jugadores)?

# i): veo el equipo mas goleador
query_0 = '''
			  SELECT ID_PARTIDO, equipos,
              case when equipo = 'ID_EQUIPO_LOCAL' then GOLES_LOCAL else GOLES_VISITANTE end as goles
			  FROM partido
			  UNPIVOT
			  (equipos for equipo in
						(ID_EQUIPO_LOCAL,ID_EQUIPO_VISITANTE)
			) 
          where ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')
      order by 1
'''
query_1 = f'''
SELECT EQUIPOS as ID_EQUIPO,c.NOMBRE, sum(goles) as goles_a_favor,
ROW_NUMBER() OVER (ORDER BY GOLES_A_FAVOR DESC) AS RANKING
        FROM
		({query_0}) b

        --A continuacion los siguientes joins son solo para filtrar por la liga asignada
        JOIN equipo_A c
        on c.ID_EQUIPO = b.EQUIPOS
        JOIN equipo_C d
        on d.PAIS = c.PAIS
        and d.LIGA = 'Belgium Jupiler League'
        group by 1,2
        order by 3

'''
# ii): veo el equipo con mayor suma de atributos (potencia y dribbling)
query_2 = '''
SELECT ID_EQUIPO,NOMBRE, sum(potencia_total_equipo+dribbling_total_equipo) as puntaje_historico,
ROW_NUMBER() OVER (ORDER BY puntaje_historico DESC) AS RANKING
FROM

(SELECT b.ID_EQUIPO,
c.NOMBRE,
    --Ahora con los promedios de los jugadores por cada temporada de la liga Belga,
    --hago la suma de ellos por temporada
    sum(potencia_promedio) as potencia_total_equipo,
    sum(dribbling_promedio) as dribbling_total_equipo
    FROM
    (--De jugador_atributos me genero temporada y semestre para joinear con componen_plantel y filtrar por liga
        SELECT
        ID_JUGADOR,
        
        CASE
            WHEN CAST(SPLIT(fecha_calendario, '-')[2] AS INTEGER) >= 7 THEN 1
            ELSE 2
        END AS semestre_temporada,
        CASE
            WHEN CAST(SPLIT(fecha_calendario, '-')[2] AS INTEGER) >= 7
                THEN CONCAT(SPLIT(fecha_calendario, '-')[1], '/', CAST(CAST(SPLIT(fecha_calendario, '-')[1] AS INTEGER) + 1 AS VARCHAR))
            ELSE CONCAT(CAST(CAST(SPLIT(fecha_calendario, '-')[1] AS INTEGER) - 1 AS VARCHAR), '/', SPLIT(fecha_calendario, '-')[1])
        END AS ID_TEMPORADA,
        --promedio de las mediciones de potencia y dribbling por temporada
        mean(POTENCIA) as potencia_promedio,
        mean(dribbling) as dribbling_promedio
        FROM jugador_atributos
        group by 1,2,3
     ) a
    JOIN componen_plantel b
    on b.ID_TEMPORADA = A.ID_TEMPORADA
    and b.SEMESTRE = a.SEMESTRE_TEMPORADA
    and b.ID_JUGADOR = a.ID_JUGADOR
    
    --A continuacion los siguientes joins son solo para filtrar por la liga asignada
    JOIN equipo_A c
    on c.ID_EQUIPO = b.ID_EQUIPO
    JOIN equipo_C d
    on d.PAIS = c.PAIS
    and d.LIGA = 'Belgium Jupiler League'
    where a.ID_TEMPORADA in ('2009/2010','2010/2011','2011/2012','2012/2013')
    group by all)
    GROUP BY ALL
'''
query = f''' select a.NOMBRE,a.goles_a_favor,b.puntaje_historico,b.RANKING 
from ({query_1}) a
join ({query_2}) b
on b.ranking = a.ranking
and b.ID_EQUIPO = a.ID_EQUIPO

'''
print("el equipo mas goleador y con plantel mas talentoso es: ")
print(duckdb.sql(query))
print("RTA: no hay equipo historicamente que sea el mas goleador y el mas talentoso al mismo tiempo ")

##############################################################################


# 1) Graficar la cantidad de goles a favor y en contra de cada equipo a lo largo de los años que elijan
    #ARMO MI TABLA PARA LUEGO HACER LA VISUALIZACION.
    #OBTENGO LOS GOLES HECHOS POR TEMPORADAS DE CADA EQUIPO.


query1d = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2d = duckdb.sql('''
                    Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                    From partido 
                    INNER JOIN query1d as EQUIPOS_BELGAS
                    ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_EQUIPO_LOCAL asc;
                    ''')
                          
#Obtengo todos los datos q necesite de los equipos belgas.

query3d = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_LOCAL as Equipo, SUM(GOLES_LOCAL) as Goles_hechos_local
                     From query2d
                     Group By ID_EQUIPO_LOCAL, ID_TEMPORADA
                     Order By ID_EQUIPO_LOCAL asc;
                     ''')
                     
#Goles q metierons los equipos q jugaron de local.                     

query4d = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_VISITANTE as Equipo, SUM(GOLES_VISITANTE) as Goles_hechos_visitante
                     From query2d
                     Group By ID_EQUIPO_VISITANTE, ID_TEMPORADA
                     Order By ID_EQUIPO_VISITANTE asc;
                     ''')

#Goles q metieron los equipos q jugaron de visitante.

query5d = duckdb.sql ('''
                     Select * 
                     From query3d
                     UNION ALL
                     Select * 
                     From query4d;
                     ''')

#Unimos todos los goles de los equipos en una sola tabla.

query6d = duckdb.sql ('''
                     Select ID_TEMPORADA, Equipo, SUM (Goles_hechos_local) as Goles_totales_hechos
                     From query5d
                     Group By Equipo, ID_TEMPORADA
                     Order By Equipo asc;
                     ''')

#Terminamos de sumarlos.

#-----------------------------------------------------------------------------#
#OBTENGO LOS GOLES RECIBIDOS POR CADA EQUIPO EN CADA TEMPORADA Y LO UNO A LA TABLA DE
#GOLES A FAVOR.

query1e = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2e = duckdb.sql('''
                    Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                    From partido 
                    INNER JOIN query1e as EQUIPOS_BELGAS
                    ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_EQUIPO_LOCAL asc;
                    ''')

#Obtengo todos los datos q necesite de los equipos belgas.

query3e = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_LOCAL as Equipo, SUM(GOLES_VISITANTE) as Goles_recibidos_visitantes
                     From query2e
                     Group By ID_EQUIPO_LOCAL, ID_TEMPORADA
                     Order By ID_EQUIPO_LOCAL asc;
                     ''')

#Goles q recibieron los equipos q jugaron de local segun la temporada.

query4e = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_VISITANTE as Equipo, SUM(GOLES_LOCAL) as Goles_recibidos_locales
                     From query2e
                     Group By ID_EQUIPO_VISITANTE, ID_TEMPORADA
                     Order By ID_EQUIPO_VISITANTE asc;
                     ''')

#Goles q recibieron los equipos q jugaron de visitante segun la temporada.

query5e = duckdb.sql ('''
                     Select ID_TEMPORADA, Equipo, Goles_recibidos_visitantes as Goles_recibidos
                     From query3e
                     UNION ALL
                     Select * 
                     From query4e
                     Order By ID_TEMPORADA asc;
                     ''')

#Unimos todos los goles recibidos de los equipos en una sola tabla.

query6e = duckdb.sql ('''
                     Select ID_TEMPORADA, Equipo, SUM (Goles_recibidos) as Goles_totales_recibidos
                     From query5e
                     Group By Equipo, ID_TEMPORADA
                     Order By ID_TEMPORADA asc;
                     ''')

#Terminamos de sumarlos.

###############################################################################

#1° Mitad de mas goleadores.

query7e0a = duckdb.sql ('''
                     Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                     Where q6d.Equipo in [8635, 8342, 9987, 9991, 9985, 9994, 10000, 8203, 8571, 9984, 9993]
                     Order By q6e.ID_TEMPORADA asc;
                     ''')
                     
query8e0a = duckdb.sql ('''
                       Select ID_TEMPORADA, NOMBRE, Goles_totales_hechos, Goles_totales_recibidos
                       From query7e0a as q7e0a
                       INNER JOIN equipo_A
                       ON q7e0a.Equipo = equipo_A.ID_EQUIPO
                       Order By ID_TEMPORADA, NOMBRE asc;
                       ''')
                       
#2° Mitad mas goleadores.
                       
query7e0b = duckdb.sql ('''
                       Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                       From query6d as q6d
                       INNER JOIN query6e as q6e
                       ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                       Where q6d.Equipo in [9998, 10001, 9997, 1773, 9986, 9989, 9999, 6351, 8475]
                       Order By q6e.ID_TEMPORADA asc;
                       ''')
                           
query8e0b = duckdb.sql ('''
                       Select ID_TEMPORADA, NOMBRE, Goles_totales_hechos, Goles_totales_recibidos
                       From query7e0b as q7e0b
                       INNER JOIN equipo_A
                       ON q7e0b.Equipo = equipo_A.ID_EQUIPO
                       Order By ID_TEMPORADA, NOMBRE asc;
                       ''')                 

###############################################################################

query7e1 = duckdb.sql ('''
                     Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                     Where q6e.ID_TEMPORADA = '2009/2010'
                     Order By q6e.Equipo asc;
                     ''')
                     
query7e2 = duckdb.sql ('''
                     Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                     Where q6e.ID_TEMPORADA = '2010/2011'
                     Order By q6e.Equipo asc;
                     ''')

query7e3 = duckdb.sql ('''
                     Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                     Where q6e.ID_TEMPORADA = '2011/2012'
                     Order By q6e.Equipo asc;
                     ''')

query7e4 = duckdb.sql ('''
                     Select q6d.ID_TEMPORADA, q6d.Equipo, Goles_totales_hechos, Goles_totales_recibidos
                     From query6d as q6d
                     INNER JOIN query6e as q6e
                     ON q6d.Equipo = q6e.Equipo and q6d.ID_TEMPORADA = q6e.ID_TEMPORADA
                     Where q6e.ID_TEMPORADA = '2012/2013'
                     Order By q6e.Equipo asc;
                     ''')
                     
#Ahora tenemos una tabla con todos los goles q recibio un equipo y todos los q hizo
#separados por temporada.


###############################################################################
# Cargamos el primer dataset
historial_goles_historico_1 = query8e0a
historial_goles_historico_1_df = historial_goles_historico_1.df()
historial_goles_historico_1_df.to_csv('historial_goles_historico_1.csv', index = False)


historial_goles_historico_1 = pd.read_csv ('historial_goles_historico_1.csv')
#-----------------------------------------------------------------------------#
# Cargamos el segundo dataset
historial_goles_historico_2 = query8e0b
historial_goles_historico_2_df = historial_goles_historico_2.df()
historial_goles_historico_2_df.to_csv('historial_goles_historico_2.csv', index = False)


historial_goles_historico_2 = pd.read_csv ('historial_goles_historico_2.csv')

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in historial_goles_historico_1['NOMBRE'].unique():
    equipo_data = historial_goles_historico_1[historial_goles_historico_1['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Goles_totales_hechos'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('GOLES HECHOS POR EQUIPOS QUE JUGARON TODAS LAS TEMPORADAS', fontsize = 10)
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles hechos')

plt.text(0, 1, 'Standar de Liege arranca y termina mas arriba.', fontsize = 8)
plt.text(0, -2, 'Beerschot AC arranca y termina mas abajo.', fontsize = 8)

# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in historial_goles_historico_1['NOMBRE'].unique():
    equipo_data = historial_goles_historico_1[historial_goles_historico_1['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Goles_totales_recibidos'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('GOLES RECIBIDOS POR EQUIPOS QUE JUGARON TODAS LAS TEMPORADAS', fontsize = 10)
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles recibidos')

plt.text(0, 1, 'Standar de Liege arranca y termina mas abajo.', fontsize = 8)
plt.text(0, -2, 'Beerschot AC arranca y termina mas arriba.', fontsize = 8)

# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in historial_goles_historico_2['NOMBRE'].unique():
    equipo_data = historial_goles_historico_2[historial_goles_historico_2['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Goles_totales_hechos'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('GOLES HECHOS POR EQUIPOS QUE NO JUGARON TODAS LAS TEMPORADAS', fontsize = 10)
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles hechos')


# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in historial_goles_historico_2['NOMBRE'].unique():
    equipo_data = historial_goles_historico_2[historial_goles_historico_2['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Goles_totales_recibidos'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('GOLES RECIBIDOS POR EQUIPOS QUE NO JUGARON TODAS LAS TEMPORADAS', fontsize = 10)
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles recibidos')


# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#####################################33

# 2) Graficar el promedio de gol de los equipos a lo largo de los años que elijan 

###############################################################################
#ARMO MI TABLA PARA LUEGO HACER LA VISUALIZACION.

#ARMO MI TABLA PARA LUEGO HACER LA VISUALIZACION.

#OBTENGO EL PROMEDIO DE GOL DE CADA EQUIPO.

query1d = duckdb.sql('''
                    Select Distinct ID_EQUIPO
                    From equipo_A
                    Where PAIS = 'Belgium'
                    Order by ID_EQUIPO asc;
                    ''')

#Obtengo los equipos de Belgica solamente.

query2d = duckdb.sql('''
                    Select ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE, GOLES_LOCAL, GOLES_VISITANTE
                    From partido 
                    INNER JOIN query1d as EQUIPOS_BELGAS
                    ON partido.ID_EQUIPO_LOCAL = EQUIPOS_BELGAS.ID_EQUIPO
                    Where ID_TEMPORADA = '2009/2010'
                    Or ID_TEMPORADA = '2010/2011'
                    Or ID_TEMPORADA = '2011/2012'
                    Or ID_TEMPORADA = '2012/2013'
                    Order By ID_EQUIPO_LOCAL asc;
                    ''')
                          
#Obtengo todos los datos q necesite de los equipos belgas.

query3d = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_LOCAL as Equipo, SUM(GOLES_LOCAL) as Goles_hechos_local
                     From query2d
                     Group By ID_EQUIPO_LOCAL, ID_TEMPORADA
                     Order By ID_EQUIPO_LOCAL asc;
                     ''')
                     
#Goles q metierons los equipos q jugaron de local.                     

query4d = duckdb.sql ('''
                     Select ID_TEMPORADA, ID_EQUIPO_VISITANTE as Equipo, SUM(GOLES_VISITANTE) as Goles_hechos_visitante
                     From query2d
                     Group By ID_EQUIPO_VISITANTE, ID_TEMPORADA
                     Order By ID_EQUIPO_VISITANTE asc;
                     ''')

#Goles q metieron los equipos q jugaron de visitante.

query5d = duckdb.sql ('''
                     Select * 
                     From query3d
                     UNION ALL
                     Select * 
                     From query4d;
                     ''')

#Unimos todos los goles de los equipos en una sola tabla.

query6d = duckdb.sql ('''
                     Select ID_TEMPORADA, Equipo, SUM (Goles_hechos_local) as Goles_totales_hechos
                     From query5d
                     Group By Equipo, ID_TEMPORADA
                     Order By Equipo asc;
                     ''')

#Terminamos de sumarlos.

query7d = duckdb.sql ('''
                      Select ID_TEMPORADA, NOMBRE, Goles_totales_hechos, Equipo
                      From query6d
                      INNER JOIN equipo_A
                      ON Equipo = ID_EQUIPO;
                      ''')
                      
#Les cambio el nombre.

query8da = duckdb.sql ('''
                      Select ID_TEMPORADA, NOMBRE, (Case When ID_TEMPORADA in ['2010/2011','2011/2012','2012/2013']
                                                    Then Goles_totales_hechos/30
                                                    Else Goles_totales_hechos/28
                                                    END) as Promedio_de_gol
                      From query7d
                      Where Equipo in [8635, 8342, 9987, 9991, 9985, 9994, 10000, 8203, 8571, 9984, 9993]
                      Order By ID_TEMPORADA asc, NOMBRE asc;
                      ''')
                      
#Selecciono a los mas goleadores y q jugaron las 4 temporadas.

query8db = duckdb.sql ('''
                      Select ID_TEMPORADA, NOMBRE, (Case When ID_TEMPORADA in ['2010/2011','2011/2012','2012/2013']
                                                    Then Goles_totales_hechos/30
                                                    Else Goles_totales_hechos/28
                                                    END) as Promedio_de_gol
                      From query7d
                      Where Equipo in [9998, 10001, 9997, 1773, 9986, 9989, 9999, 6351, 8475]
                      Order By ID_TEMPORADA asc, NOMBRE asc;
                      ''')
                      
#Selecciono a los menos goleadores y no jugaron las 4 termporadas.         

#-----------------------------------------------------------------------------#

query7da1 = duckdb.sql ('''
                      Select NOMBRE, Goles_totales_hechos, Equipo
                      From query6d
                      INNER JOIN equipo_A
                      ON Equipo = ID_EQUIPO
                      Where Equipo in [8635, 8342, 9987, 9991, 9985, 9994, 10000, 8203, 8571, 9984, 9993];
                      ''')
                      
query7db1 = duckdb.sql ('''
                      Select NOMBRE, Equipo, Goles_totales_hechos
                      From query6d
                      INNER JOIN equipo_A
                      ON Equipo = ID_EQUIPO
                      Where Equipo in [9998, 10001, 9997, 1773, 9986, 9989, 9999, 6351, 8475];
                      ''')
                      
query7db2 = duckdb.sql ('''
                        Select NOMBRE, SUM(Goles_totales_hechos) as Goles_totales_hechos
                        From query7db1
                        Group By NOMBRE;
                        ''')

query8da1 = duckdb.sql ('''
                      Select NOMBRE, SUM(Goles_totales_hechos)/108 as Promedio_de_gol
                      From query7da1
                      Group By NOMBRE
                      Order By NOMBRE asc;
                      ''')
                      
#Selecciono a los mas goleadores y q jugaron las 4 temporadas.

query8db1 = duckdb.sql ('''
                        Select NOMBRE, (Case When Nombre in ['KSV Roeselare']
                                        Then Goles_totales_hechos/28
                                        When NOMBRE in ['Sint-Truidense VV', 'Sporting Charleroi', 'KVC Westerlo']
                                        Then Goles_totales_hechos/88
                                        When NOMBRE in ['KAS Eupen', 'Waasland-Beveren']
                                        Then Goles_totales_hechos/30
                                        When NOMBRE in ['Lierse SK']
                                        Then Goles_totales_hechos/90
                                        When NOMBRE in ['Oud-Heverlee Leuven', 'RAEC Mons']
                                        Then Goles_totales_hechos/60
                                        END) as Promedio_de_gol
                      From query7db2
                      Order By  NOMBRE asc;
                      ''')
                      
#Selecciono a los menos goleadores y no jugaron las 4 termporadas.                       


###############################################################################

#Cantidad de partidos jugados por cada temporada

query1e =  duckdb.sql( '''
                      Select ID_TEMPORADA, FECHA, ID_PARTIDO, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE
                      From partido
                      INNER JOIN query1d as q1d
                      ON ID_EQUIPO_LOCAL = q1d.ID_EQUIPO
                      Where ID_TEMPORADA IN ['2009/2010'] and (ID_EQUIPO_LOCAL = 9999 or ID_EQUIPO_VISITANTE = 9999)
                      Order By Fecha asc;
                      ''')

#TODOS LOS EQUIPOS JUGARON 28 FECHAS, HUBO UN ERROR EN LISTAR LAS FECHAS PORQ ESTAN REGISTRADOS HASTA 
#LA FECHA 30 Y FALTAN EL REGISTRO DE 2 FECHAS EN TODOS LOS EQUIPOS, LO CUAL ME HACE PENSAR Q SON EN 
#REALIDAD 28 FECHAS LO SE PORQ CAMBIANDO EL ID DEL EQUIPO LOCAL Y VISITANTE A LA VEZ EN LA CONSULTA 
#PODEMOS VER Q SIEMRPE FALTAN 2 FECHAS, ADEMAS SI PRINTEAMOS ESTA CONSULTA NOS SALTA Q HAY 28 FILAS.

query2e =  duckdb.sql( '''
                      Select ID_TEMPORADA, FECHA, ID_PARTIDO, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE
                      From partido
                      INNER JOIN query1d as q1d
                      ON ID_EQUIPO_LOCAL = q1d.ID_EQUIPO
                      Where ID_TEMPORADA IN ['2010/2011'] and (ID_EQUIPO_LOCAL = 6351 or ID_EQUIPO_VISITANTE = 6351)
                      Order By Fecha asc;
                      ''')
                      
#TODOS LOS EQUIPOS JUGARON 30 FECHAS, SI PRINTEAMOS ESTA CONSULTA NOS 
#SALTA Q HAY 30 FILAS, SIN IMPORTAR DE Q EQUIPO HABLEMOS (Q HAYA JUGADO LA TEMPORADA).

query3e =  duckdb.sql( '''
                      Select ID_TEMPORADA, FECHA, ID_PARTIDO, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE
                      From partido
                      INNER JOIN query1d as q1d
                      ON ID_EQUIPO_LOCAL = q1d.ID_EQUIPO
                      Where ID_TEMPORADA IN ['2011/2012'] and (ID_EQUIPO_LOCAL = 9987 or ID_EQUIPO_VISITANTE = 9987)
                      Order By Fecha asc;
                      ''')

#TODOS LOS EQUIPOS JUGARON 30 FECHAS.

query4e =  duckdb.sql( '''
                      Select ID_TEMPORADA, FECHA, ID_PARTIDO, ID_EQUIPO_LOCAL, ID_EQUIPO_VISITANTE
                      From partido
                      INNER JOIN query1d as q1d
                      ON ID_EQUIPO_LOCAL = q1d.ID_EQUIPO
                      Where ID_TEMPORADA IN ['2012/2013'] and (ID_EQUIPO_LOCAL = 8203 or ID_EQUIPO_VISITANTE = 8203)
                      Order By Fecha asc;
                      ''')
#TODOS LOS EQUIPOS JUGARON 30 FECHAS.



###############################################################################

#Visualizaciones

#Graficar el promedio de gol de los equipos a lo largo de los años que elijan.

#-----------------------------------------------------------------------------#

'''# Cargamos el primer dataset
promedio_de_gol_1 = query8da
promedio_de_gol_1_df = promedio_de_gol_1.df()
promedio_de_gol_1_df.to_csv('promedio_de_gol_1.csv', index = False)

promedio_de_gol_1 = pd.read_csv ('promedio_de_gol_1.csv')

#-----------------------------------------------------------------------------#

# Cargamos el segundo dataset
promedio_de_gol_2 = query8db
promedio_de_gol_2_df = promedio_de_gol_2.df()
promedio_de_gol_2_df.to_csv('promedio_de_gol_2.csv', index = False)

promedio_de_gol_2 = pd.read_csv ('promedio_de_gol_2.csv')

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in promedio_de_gol_1['NOMBRE'].unique():
    equipo_data = promedio_de_gol_1[promedio_de_gol_1['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Promedio_de_gol'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('Promedio de gol de los equipos más goleadores')
ax.set_xlabel('Temporada')
ax.set_ylabel('Promedio de gol')


# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#STANDARD DE LIEGE ES EL Q ARRANCA Y TERMINA MAS ARRIBA 
#BEERSCHOT AC ES EL Q ARRANCA Y TERMINA MAS ABAJO

###############################################################################

# Genera el gráfico de líneas, una línea por cada equipo
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'  # Configuración de la fuente

# Graficar cada equipo por separado
for equipo in promedio_de_gol_2['NOMBRE'].unique():
    equipo_data = promedio_de_gol_2[promedio_de_gol_2['NOMBRE'] == equipo]
    
    ax.plot(equipo_data['ID_TEMPORADA'], equipo_data['Promedio_de_gol'], 
            marker='o',      # Tipo de punto
            linestyle='-',   # Tipo de línea
            linewidth=1,   # Grosor de la línea
            label=f'{equipo}')  # Etiqueta para cada equipo

# Agrega título, etiquetas a los ejes y otras configuraciones
ax.set_title('Promedio de gol de los equipos menos goleadores')
ax.set_xlabel('Temporada')
ax.set_ylabel('Promedio de gol')


# Muestra la leyenda para identificar a cada equipo
ax.legend(title='Equipos')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()
'''
###############################################################################
#%%%
query8dc1 = duckdb.sql('''
                       Select *
                       From query8da1
                       Union All
                       Select *
                       From query8db1;
                       ''')


###############################################################################

#-----------------------------------------------------------------------------#

# Cargamos el TERCER dataset
promedio_de_gol_3 = query8da1
promedio_de_gol_3_df = promedio_de_gol_3.df()
promedio_de_gol_3_df.to_csv('promedio_de_gol_3.csv', index = False)

promedio_de_gol_3 = pd.read_csv ('promedio_de_gol_3.csv')

#-----------------------------------------------------------------------------#

# Cargamos el CUARTO dataset
promedio_de_gol_4 = query8db1
promedio_de_gol_4_df = promedio_de_gol_4.df()
promedio_de_gol_4_df.to_csv('promedio_de_gol_4.csv', index = False)

promedio_de_gol_4 = pd.read_csv ('promedio_de_gol_4.csv')

#-----------------------------------------------------------------------------#
#%%
# Cargamos el QUINTO dataset
promedio_de_gol_5 = query8dc1
promedio_de_gol_5_df = promedio_de_gol_5.df()
promedio_de_gol_5_df.to_csv('promedio_de_gol_5.csv', index = False)

promedio_de_gol_5 = pd.read_csv ('promedio_de_gol_5.csv')

#-----------------------------------------------------------------------------#

# Genera el grafico de barras de ambas series temporales (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

promedio_de_gol_3.plot(x='NOMBRE', 
                    y=['Promedio_de_gol'], 
                    kind='bar',
                    label=['Promedio de gol'],   # Agrega etiquetas a la serie
                    color = 'aqua',
                    ax = ax)
ax.set_title('PROMEDIO DE GOL EN EQUIPOS QUE JUGARON TODAS LAS TEMPORADAS')
ax.set_xlabel('Equipos')
ax.set_ylabel('Promedio de gol')

ax.set_ylim(0, 2.5)

#-----------------------------------------------------------------------------#


# Genera el grafico de barras de ambas series temporales (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

promedio_de_gol_4.plot(x='NOMBRE', 
                    y=['Promedio_de_gol'], 
                    kind='bar',
                    label=['Promedio de gol'],   # Agrega etiquetas a la serie
                    color = 'deeppink',
                    ax = ax)
ax.set_title('PROMEDIO DE GOL EN EQUIPOS QUE NO JUGARON TODAS LAS TEMPORADAS')
ax.set_xlabel('Equipos')
ax.set_ylabel('Promedio de gol')

ax.set_ylim(0, 2.5)

#-----------------------------------------------------------------------------#
#%%

color1 = 11*["aqua"] + 9*["deeppink"]

fig, ax = plt.subplots()
plt.rcParams['font.family'] = 'sans-serif'

ax.bar(promedio_de_gol_5['NOMBRE'], promedio_de_gol_5['Promedio_de_gol'], 
       color=color1)

ax.set_title('PROMEDIO DE GOL DE LA LIGA', size = 14)
ax.set_ylabel('Promedio de gol', size = 10)
ax.set_xlabel('Equipos', size = 10)
ax.set_ylim(0, 2.5)
ax.tick_params(axis='x', rotation=90, labelsize = 10)  # Rotar etiquetas eje x
ax.tick_params(axis='y', labelsize = 8)

plt.text(-3.5, -1.7, 'Equipos que participaron de todas las temporadas en aqua.', fontsize = 9)
plt.text(-3.5, -1.9, 'Equipos que participaron algunas de ellas en deeppink.', fontsize = 9)
plt.text(-3.5, -3, ' ', fontsize = 10)

plt.tight_layout()
plt.show()



#############################################################
#%%
# 3) Graficar la diferencia de goles convertidos jugando de local vs visitante a lo largo del tiempo
#Goles como local
goles_local = duckdb.sql('''
    SELECT
        b.ID_TEMPORADA AS TEMPORADA,
        b.ID_EQUIPO_LOCAL AS ID_EQUIPO,
        a.NOMBRE,
        SUM(b.GOLES_LOCAL) AS GOLES_A_FAVOR_LOCAL,
        count(ID_PARTIDO) as cantidad_partidos
    FROM partido b
    INNER JOIN equipo_A a ON a.ID_EQUIPO = b.ID_EQUIPO_LOCAL
    WHERE a.PAIS = 'Belgium'
    AND b.ID_TEMPORADA IN ('2009/2010', '2010/2011', '2011/2012', '2012/2013')
    GROUP BY b.ID_TEMPORADA, b.ID_EQUIPO_LOCAL, a.NOMBRE
''')
print(goles_local)

#-- Goles como visitante
goles_visitante = duckdb.sql('''
    SELECT
        b.ID_TEMPORADA AS TEMPORADA,
        b.ID_EQUIPO_VISITANTE AS ID_EQUIPO,
        a.NOMBRE,
        SUM(b.GOLES_VISITANTE) AS GOLES_A_FAVOR_VISITANTE,
        count(ID_PARTIDO) as cantidad_partidos
    FROM partido b
    INNER JOIN equipo_A a ON a.ID_EQUIPO = b.ID_EQUIPO_VISITANTE
    WHERE a.PAIS = 'Belgium'
    AND b.ID_TEMPORADA IN ('2009/2010', '2010/2011', '2011/2012', '2012/2013')
    GROUP BY b.ID_TEMPORADA, b.ID_EQUIPO_VISITANTE, a.NOMBRE
''')
# %%
goles_totales_por_equipo = duckdb.sql('''
    SELECT
        a.TEMPORADA AS TEMPORADA,
        a.ID_EQUIPO AS ID_EQUIPO,
        a.NOMBRE AS NOMBRE,
        a.GOLES_A_FAVOR_LOCAL,
        a.cantidad_partidos as CANTIDAD_PARTIDOS_LOCAL,
        b.GOLES_A_FAVOR_VISITANTE,
        b.cantidad_partidos as CANTIDAD_PARTIDOS_VISITANTE
    FROM goles_local a
    INNER JOIN goles_visitante b ON a.ID_EQUIPO = b.ID_EQUIPO AND a.TEMPORADA = b.TEMPORADA
    ORDER BY TEMPORADA, ID_EQUIPO
''')
print("los goles totales por equipo son ",goles_totales_por_equipo)

# %%
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
goles_totales_por_equipo_df = pd.read_csv("goles_totales_por_equipo.csv")

# Crear la figura y los ejes del gráfico para los goles como local
fig, ax = plt.subplots(figsize=(12, 8))  # Tamaño del gráfico

# Obtener los equipos únicos para graficar una línea por equipo
equipos = goles_totales_por_equipo_df['NOMBRE'].unique()

# Configuración de fuente
plt.rcParams['font.family'] = 'sans-serif'

# Graficar una línea por cada equipo (goles como local)
for equipo in equipos:
    # Filtrar los datos del equipo
    data_equipo = goles_totales_por_equipo_df[goles_totales_por_equipo_df['NOMBRE'] == equipo]

    # Graficar los goles como local por temporada
    ax.plot(data_equipo['TEMPORADA'],
            data_equipo['GOLES_A_FAVOR_LOCAL'],
            marker='.',
            linestyle='-',
            linewidth=1.2,
            label=equipo)

# Agregar título y etiquetas
ax.set_title('Goles como Local por equipo en Bélgica')
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles como Local')

# Configurar los ticks y etiquetas del eje X
ax.set_xticks(goles_totales_por_equipo_df['TEMPORADA'].unique())
ax.set_xticklabels(goles_totales_por_equipo_df['TEMPORADA'].unique(), rotation=45)

# Mostrar leyenda fuera del gráfico
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Crear la figura y los ejes del gráfico para los goles como visitante
fig, ax = plt.subplots(figsize=(12, 8))  # Tamaño del gráfico

# Graficar una línea por cada equipo (goles como visitante)
for equipo in equipos:
    # Filtrar los datos del equipo
    data_equipo = goles_totales_por_equipo_df[goles_totales_por_equipo_df['NOMBRE'] == equipo]

    # Graficar los goles como visitante por temporada
    ax.plot(data_equipo['TEMPORADA'],
            data_equipo['GOLES_A_FAVOR_VISITANTE'],
            marker='.',
            linestyle='-',
            linewidth=1.2,
            label=equipo)

# Agregar título y etiquetas
ax.set_title('Goles como Visitante por equipo en Bélgica')
ax.set_xlabel('Temporada')
ax.set_ylabel('Goles como Visitante')

# Configurar los ticks y etiquetas del eje X
ax.set_xticks(goles_totales_por_equipo_df['TEMPORADA'].unique())
ax.set_xticklabels(goles_totales_por_equipo_df['TEMPORADA'].unique(), rotation=45)

# Mostrar leyenda fuera del gráfico
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Mostrar el gráfico
plt.tight_layout()
plt.show()
# 4) Graficar el número de goles convertidos por cada equipo en función de la suma de todos sus atributos.
# Cargar los datos desde el archivo CSV
#%%

equipos_de_belgica = duckdb.sql('''
    SELECT DISTINCT a.ID_EQUIPO, a.NOMBRE
    FROM equipo_A a
    INNER JOIN equipo_C b ON a.PAIS = b.PAIS
    WHERE b.PAIS='Belgium'
''')

jugadores_liga_belga = duckdb.sql (''' Select distinct a.ID_JUGADOR, a.ID_TEMPORADA, a.ID_EQUIPO, b.NOMBRE
                        FROM componen_plantel a
                        INNER JOIN equipos_de_belgica b
                        ON a.ID_EQUIPO=b.ID_EQUIPO
                        where a.ID_TEMPORADA IN ('2009/2010', '2010/2011', '2011/2012', '2012/2013')
                     ''')

atributos_jugadores_belgica=duckdb.sql('''SELECT a.ID_EQUIPO,b.* from (SELECT DISTINCT ID_JUGADOR,
                                CASE
                                 WHEN FECHA_CALENDARIO LIKE '2009%' THEN '2009/2010'
                                 WHEN FECHA_CALENDARIO LIKE '2010%' THEN '2010/2011'
                                 WHEN FECHA_CALENDARIO LIKE '2011%' THEN '2011/2012'
                                 WHEN FECHA_CALENDARIO LIKE '2012%' THEN '2012/2013'
                                 END AS ID_TEMPORADA,
                                 mean(POTENCIA) as PROMEDIO_POTENCIA,
                                 mean(DRIBBLING) as PROMEDIO_DRIBBLING
                                FROM jugador_atributos
                                WHERE FECHA_CALENDARIO LIKE '2009%'
                                OR FECHA_CALENDARIO LIKE '2010%'
                                OR FECHA_CALENDARIO LIKE '2011%'
                                OR FECHA_CALENDARIO LIKE '2012%'
                                group by all) b
                                INNER JOIN jugadores_liga_belga a
                                ON b.ID_JUGADOR = a.ID_JUGADOR
                                and b.ID_TEMPORADA = a.ID_TEMPORADA


                              ''')
print("la tabla atributos_jugadores_belgica es : ",atributos_jugadores_belgica)
#%%
partidos_de_belgica = duckdb.sql('''
    SELECT ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_LOCAL as ID_EQUIPO
    FROM partido b
    JOIN equipos_de_belgica a ON (b.ID_EQUIPO_LOCAL = a.ID_EQUIPO)
    WHERE ID_TEMPORADA IN ('2009/2010', '2010/2011', '2011/2012', '2012/2013')
    UNION ALL
    SELECT ID_PARTIDO, ID_TEMPORADA, ID_EQUIPO_VISITANTE as ID_EQUIPO
    FROM partido b
    JOIN equipos_de_belgica ON (b.ID_EQUIPO_VISITANTE = ID_EQUIPO)
    WHERE ID_TEMPORADA IN ('2009/2010', '2010/2011', '2011/2012', '2012/2013')
    ''')
print("los partidos_de_belgica son : ",partidos_de_belgica)
#HOLA
#%%%
partidos_por_equipo = duckdb.sql('''
    SELECT ID_EQUIPO,count(ID_PARTIDO) as CANTIDAD_PARTIDOS
    FROM partidos_de_belgica
    group BY ID_EQUIPO
    ORDER BY ID_EQUIPO
    ''')
print("LOS PARTIDOS POR EQUIPO SON, ",partidos_por_equipo)

####  REVISAR ESTA
#%%%
metricas_por_equipo_belga = duckdb.sql('''
    SELECT
        a.ID_EQUIPO,
        SUM(a.PROMEDIO_POTENCIA+a.PROMEDIO_DRIBBLING) as prom_suma_atributos
    FROM
        atributos_jugadores_belgica a

    GROUP BY
       a.ID_EQUIPO
    ORDER BY
        a.ID_EQUIPO;
''')

print("la tabla metricas_por_equipo_belga es : ",metricas_por_equipo_belga)
#%%
promedio_metricas_por_equipo_belga=duckdb.sql('''
    SELECT a.ID_EQUIPO, a.prom_suma_atributos as PROMEDIO_ATRIBUTOS, count(b.ID_PARTIDO) as CANTIDAD_PARTIDOS
    FROM metricas_por_equipo_belga a
    join partidos_de_belgica b
    on a.ID_EQUIPO = b.ID_EQUIPO
    group by all
    order by a.ID_EQUIPO

''')
print("el promedio_metricas_por_equipo_belga es : ",promedio_metricas_por_equipo_belga)
# %%
goles_en_total_con_promedio = duckdb.sql('''
    SELECT
        l.ID_EQUIPO,
        l.NOMBRE,
        SUM(l.GOLES_A_FAVOR_LOCAL + l.GOLES_A_FAVOR_VISITANTE) AS GOLES_TOTALES_A_FAVOR
        ,sum(cantidad_partidos_local+cantidad_partidos_visitante) as PARTIDOS_JUGADOS
        ,(goles_totales_a_favor/partidos_jugados) as PROMEDIO_DE_GOL
    FROM goles_totales_por_equipo l
    GROUP BY l.ID_EQUIPO, l.NOMBRE
    ORDER BY l.ID_EQUIPO
''')


print("los goles en total son ",goles_en_total_con_promedio)
#%%=
promedio_metricas_goles_por_equipo = duckdb.sql('''
    SELECT a.ID_EQUIPO,
           a.PROMEDIO_ATRIBUTOS,
            ROUND (b.PROMEDIO_DE_GOL,2) as PROMEDIO_DE_GOL
    FROM promedio_metricas_por_equipo_belga a
    INNER JOIN goles_en_total_con_promedio b ON a.ID_EQUIPO = b.ID_EQUIPO
    GROUP BY a.ID_EQUIPO, a.PROMEDIO_ATRIBUTOS, b.PROMEDIO_DE_GOL
    ORDER BY a.ID_EQUIPO
''')

print(promedio_metricas_goles_por_equipo)
promedio_metrica_goles_por_equipo_df = promedio_metricas_goles_por_equipo.df()
promedio_metrica_goles_por_equipo_df.to_csv('promedio_metrica_goles_por_equipo.csv', index=False)
promedio_metrica_goles_por_equipo_df = pd.read_csv("promedio_metrica_goles_por_equipo.csv")
#%%=

import pandas as pd
import matplotlib.pyplot as plt

# Carga de los datos
promedio_metrica_goles_por_equipo_df = pd.read_csv("metrica_goles_por_equipo.csv")

# Configuración de la figura y ejes
fig, ax = plt.subplots()

# Personalización de la fuente
plt.rcParams['font.family'] = 'sans-serif'

# Gráfico de dispersión
ax.scatter(data=promedio_metrica_goles_por_equipo_df,
           x='PROMEDIO_DE_GOL',       # Eje X
           y='PROMEDIO_ATRIBUTOS',     # Eje Y
           s=8,                        # Tamaño de los puntos
           color='magenta')            # Color de los puntos

# Configuración del gráfico
ax.set_title('Promedio de goles Totales a Favor vs. Promedio de Métricas')  # Título del gráfico
ax.set_xlabel('Promedio de goles Totales a Favor', fontsize='medium')       # Etiqueta eje X
ax.set_ylabel('Promedio de suma de Métricas', fontsize='medium')            # Etiqueta eje Y

# Ajuste del límite del eje X para incluir todos los puntos
max_x_value = max(promedio_metrica_goles_por_equipo_df['PROMEDIO_DE_GOL'])
ax.set_xlim(0, max(max_x_value + 0.5, 2))  # Ajusta el límite a 2.5 o al valor máximo + 0.5


# Muestra el gráfico
plt.show()

# %%