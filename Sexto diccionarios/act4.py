fecha= input("Dime una fecha en formato dd/mm/aaaa: ")
dia=fecha.split("/")[0]
mes=fecha.split("/")[1]
anio=fecha.split("/")[2]
diccionario = {'01': "Enero", '02': "Febrero", '03': "Marzo", '04': "Abril", '05': "Mayo", '06': "Junio", '07': "Julio", '08': "Agosto", '09': "Septiembre", '10': "Octubre", '11': "Noviembre", '12': "Diciembre"}
print(dia, " de ", diccionario[mes] , " de ", anio)
