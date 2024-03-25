from django.db import connection

def mostrar_tablas():
    with connection.cursor() as cursor:
        
        #cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'oc_ordenes_cons';") saber los nombres de las columnas
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE' ")
        tablas = [fila[0] for fila in cursor.fetchall()]
    return tablas

# Llamamos a la función para obtener y mostrar las tablas
print(mostrar_tablas())
