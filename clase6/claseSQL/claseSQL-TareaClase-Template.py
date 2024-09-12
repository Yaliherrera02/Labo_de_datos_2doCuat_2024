# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2024-03-25
"""
#%%===========================================================================

# Importamos bibliotecas
import pandas as pd
#from inline_sql import sql, sql_val
import duckdb

#%%===========================================================================

carpeta = ""

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")

# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")


#%%===========================================================================
# Ejemplo inicial
#=============================================================================
consultaSQL = """
             SELECT DISTINCT DNI,Salario,Nombre
             FROM empleado;
              """

dataframeResultado = duckdb.sql(consultaSQL)
print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
             SELECT DISTINCT DNI,Salario
             FROM empleado;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
             SELECT DISTINCT Sexo
             FROM empleado;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
             SELECT Sexo
             FROM empleado;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
             SELECT DISTINCT DNI,Nombre,Sexo,Salario 
             FROM empleado
             WHERE Sexo='F';
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """
             SELECT DISTINCT *
             FROM empleado
             WHERE Sexo='F' AND Salario>15000;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
              SELECT DISTINCT DNI as id, Salario as Ingreso
              FROM empleado;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
             SELECT DISTINCT Codigo,Nombre
             FROM aeropuerto
             WHERE Ciudad='Londres';
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
              SELECT DISTINCT Ciudad AS City 
              FROM aeropuerto 
              WHERE Codigo='ORY' OR Codigo='CDG';
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
              SELECT DISTINCT Numero
              FROM vuelo
              WHERE Origen='CDG' AND Destino='LHR';
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
              SELECT DISTINCT Numero
              FROM vuelo
              WHERE (Origen='CDG' AND Destino='LHR') OR (Origen='LHR' AND Destino='CDG');
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)


# Ejercicio 01.4 bis.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
#Esta es oTRA forma de hacer el ejercicio"
consultaSQL = """
              SELECT DISTINCT Numero
              FROM vuelo
              WHERE Origen='CDG' AND Destino='LHR'
            UNION
              SELECT DISTINCT Numero
              FROM vuelo
              WHERE Origen='LHR' AND Destino='CDG';
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
              SELECT DISTINCT Fecha
              from reserva
              WHERE Precio>200;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
            SELECT *
            FROM alumnosBD
        UNION
            SELECT *
            FROM alumnosTLeng;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
            SELECT *
            FROM alumnosBD
        UNION ALL
            SELECT *
            FROM alumnosTLeng;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
            SELECT DISTINCT *
            FROM alumnosBD
        INTERSECT
            SELECT DISTINCT *
            FROM alumnosTLeng;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
            SELECT DISTINCT *
            FROM alumnosBD
        EXCEPT
            SELECT DISTINCT *
            FROM alumnosTLeng;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
             SELECT DISTINCT Numero
             FROM vuelo
          INTERSECT
             SELECT DISTINCT NroVuelo
             FROM reserva;
              """
dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
             SELECT Numero
             FROM vuelo
          EXCEPT
             SELECT NroVuelo
             FROM reserva;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos 
consultaSQL = """
            SELECT DISTINCT Codigo
            FROM aeropuerto
        INTERSECT
            SELECT DISTINCT Origen
            FROM vuelo
         UNION 
            SELECT DISTINCT Destino
            FROM vuelo;
              """
              
dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
            SELECT DISTINCT *
            FROM persona
            CROSS JOIN nacionalidades;
            """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
            SELECT DISTINCT *
            FROM persona,nacionalidades;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)


#%% --------------------------------------------------------------------------------------------
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN
print("PRUEBA:")
consultaSQL = """
            SELECT DISTINCT *
            FROM persona
            INNER JOIN nacionalidades
            ON Nacionalidad=IDN;
            """

dataframeResultado = duckdb.sql( consultaSQL)
#print(dataframeResultado)
"""
            SELECT DISTINCT *
            FROM nacionalidades
            INNER JOIN persona
            ON IDN=Nacionalidad;
            """

#print(dataframeResultado)
#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
            SELECT DISTINCT *
            FROM persona AS p, nacionalidades AS n
            WHERE Nacionalidad=IDN;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)
#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
            SELECT DISTINCT *
            FROM persona
            LEFT OUTER JOIN nacionalidades
            ON Nacionalidad=IDN;
              """

dataframeResultado = duckdb.sql(consultaSQL)
#print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia
#OJO: Nombre esta en la tabla materia y lo agrego igual porque lo quiero en mi df
consultaSQL = """
            SELECT DISTINCT LU,Nombre 
            FROM se_inscribe_en
            INNER JOIN materia
            ON se_inscribe_en.Codigo_materia=
            materia.Codigo_materia;
             """

dataframeResultado = duckdb.sql(consultaSQL)

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
              SELECT Ciudad
              From aeropuerto
              INNER JOIN vuelo
              ON aeropuerto.Codigo=vuelo.Origen
              WHERE vuelo.Numero=165
              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
            SELECT Nombre
            FROM pasajero
            LEFT OUTER JOIN reserva
            ON pasajero.DNI=reserva.DNI
            WHERE reserva.Precio<200

              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid
#vuelos q salen desde madrid y destino
vuelosDesdeMadrid = """ 
              SELECT vuelo.Numero, vuelo.Destino
              FROM vuelo
              INNER JOIN aeropuerto
              ON vuelo.Origen=aeropuerto.Codigo
              WHERE aeropuerto.Ciudad='Madrid';
              """
#agarro dni y fecha de vuelos desde madrid
dniPersonasDesdeMadrid = """
              SELECT DNI,Fecha,vuelosDesdeMadrid.Destino
              FROM vuelosDesdeMadrid
              INNER JOIN reserva
              ON vuelosDesdeMadrid.Numero=reserva.NroVuelo;
              """

consultaSQL = """
              SELECT pasajero.Nombre,dniPersonasDesdeMadrid.Fecha,dniPersonasDesdeMadrid.Destino
              FROM dniPersonasDesdeMadrid
              INNER JOIN pasajero
              ON pasajero.DNI=dniPersonasDesdeMadrid.DNI
              """

vuelosDesdeMadrid = duckdb.sql(vuelosDesdeMadrid)
dniPersonasDesdeMadrid= duckdb.sql(dniPersonasDesdeMadrid)
dataframeResultado =  duckdb.sql(consultaSQL)

print(dataframeResultado)

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
            SELECT DISTINCT r.Fecha, v.Salida, p.Nombre
            FROM reserva AS r, pasajero AS p, vuelo AS v
            WHERE r.DNI=p.DNI AND r.Nro_Vuelo=v.Número;
              """

dataframeResultado = duckdb.sql(consultaSQL)

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
            SELECT DISTINCT er.empleado, er.rol, rp.proyecto
            FROM EmpleadoRol AS er
            INNER JOIN RolProyecto rp
            ON er.rol=rp.rol;

              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
              SELECT count(*) AS cantidadExamenes
              FROM examen;
              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS Asistieron
              FROM Examen
              GROUP BY Instancia;
              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS Asistieron
              FROM Examen
              GROUP BY Instancia;
              ORDER BY Instancia ASC
              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS Asistieron
              FROM Examen
              GROUP BY Instancia
              HAVING Asistieron < 4
              ORDER BY Instancia;
              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - LIKE")



"""HASTA ACA TERMINO MI TAREA DEL DIAAAAAAAAAAA :)"""
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
              SELECT Instancia,
              AVG(Edad) AS PromedioEdad
              FROM Examen
              GROUP BY Instancia
              ORDER BY Instancia;

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """

              """


dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """

              """


dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """

              """


dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """

              """


dataframeResultado = duckdb.sql(consultaSQL)


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """

              """


dataframeResultado = duckdb.sql(consultaSQL)

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """

              """

dataframeResultado = duckdb.sql(consultaSQL)


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
consultaSQL = """

              """


desafio_01 = consultaSQL



#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
                 
              """

desafio_02 = duckdb.sql(consultaSQL)



#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """

              """

desafio_03 = duckdb.sql(consultaSQL)