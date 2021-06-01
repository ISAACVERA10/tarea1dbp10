import psycopg2
import MySQLdb
connection = psycopg2.connect('dbname=ejercicio1db user=postgres password=admin')
#connection = MySQLdb.connect(host='localhost',user='root',password='admin',db='ejercicio1db')
cursor = connection.cursor()
cursor.execute('drop table if exists profesor;')
cursor.execute('drop table if exists estudiante;')
cursor.execute('drop table if exists curso;')
cursor.execute('drop table if exists seccion;')

cursor.execute('''
    create table profesor(
        id INTEGER PRIMARY KEY,
        Name VARCHAR)
''')

cursor.execute('''
    create table estudiante(
        id INTEGER PRIMARY KEY,
        Name VARCHAR)
''')

cursor.execute('''
    create table curso(
        id INTEGER PRIMARY KEY,
        Name VARCHAR,
        Creditos INTEGER)
''')

cursor.execute('''
    create table seccion(
        id INTEGER PRIMARY KEY,
        Codigo VARCHAR)
''')

NAME1 = ['E. Cuadros','J. FIestas','M. Abisrror','J. Perez','K. yhin','P. Coehlo', 'L. Ramirez', 'J. Bustamante','C. Torres','P. Vargas']
ID1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    data1 = {'id':ID1[i], 'Name':NAME1[i]}
    SQL_INSERT = 'insert into profesor(id, Name) values(%(id)s,%(Name)s);'
    cursor.execute(SQL_INSERT,data1)


NAME2 = ['Isaac','Christian','José','Jorge','Piero','Joshua', 'Jake', 'Juan','Erick','Cristopher']
ID2 = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    data2 = {'id':ID2[i], 'Name':NAME2[i]}
    SQL_INSERT = 'insert into estudiante(id, Name) values(%(id)s,%(Name)s);'
    cursor.execute(SQL_INSERT,data2)


NAME3 = ['POO2','POO1','Matematica 1','Matematica 2','Matematica 3','DBP', 'Fisica 1', 'Fisica 2','ED 1','ED 2']
ID3 = [1,2,3,4,5,6,7,8,9,10]
CRED = [4,4,4,4,4,4,3,3,4,4]
for i in range(10):
    data3 = {'id':ID3[i], 'Name':NAME3[i],'Creditos':CRED[i]}
    SQL_INSERT = 'insert into curso(id, Name, Creditos) values(%(id)s,%(Name)s,%(Creditos)s);'
    cursor.execute(SQL_INSERT,data3)

COD = ['CSDB10','EG0006','CS2B01','CS1DO2','EG005','CS1103', 'CS1FI4', 'GHOOO8','CSJTU8','PORRF3']
ID4 = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    data4 = {'id':ID4[i], 'Codigo':COD[i]}
    SQL_INSERT = 'insert into seccion(id, Codigo) values(%(id)s,%(Codigo)s);'
    cursor.execute(SQL_INSERT,data4)

cursor.execute('select * from profesor;')
result1 = cursor.fetchall()
print('Profesores: ', result1)

cursor.execute('select * from estudiante;')
result2 = cursor.fetchall()
print('Estudiantes: ', result2)

cursor.execute('select * from curso;')
result3 = cursor.fetchall()
print('Curso: ', result3)

cursor.execute('select * from seccion;')
result4 = cursor.fetchall()
print('Seccion: ', result4)



connection.commit()
connection.close()
cursor.close()