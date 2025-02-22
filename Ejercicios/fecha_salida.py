from datetime import datetime, timedelta

# Fecha de ingreso
fecha_ingreso = datetime(2023, 7, 24)

# Añadir 9 años, 6 meses y 29 días
fecha_salida = fecha_ingreso + timedelta(days=(9*365 + 6*30 + 29))  # Aprox. años y meses

fecha_salida.strftime("%d-%m-%Y")  # Formato de fecha: DD-MM-YYYY

print(fecha_salida)