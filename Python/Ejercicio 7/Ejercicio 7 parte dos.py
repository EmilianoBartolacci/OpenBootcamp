# Bartolacci Emiliano
# Ejercicio 7 parte dos

import time

tiempo_segundos = time.time()
tiempo_st = time.gmtime(tiempo_segundos)

horaDeIrse = 19 * 60 * 60
segundosActuales = (tiempo_st.tm_hour * 3600) + (tiempo_st.tm_min * 60) + tiempo_st.tm_sec
diferenciaHoraria = horaDeIrse - segundosActuales

print(tiempo_st.tm_hour)
print(diferenciaHoraria)
if tiempo_st.tm_hour >= 19 :
    print("Es hora de ir a casa!")
elif tiempo_st.tm_hour <= 9 :
    print("Muy temprano para trabajar! mejor anda a dormir...")
elif diferenciaHoraria > 0 :
        if diferenciaHoraria % 3600 == 0 :
            horas = diferenciaHoraria / 3600
            print("Faltan", int(horas), "horas para ir a casa!")
        elif diferenciaHoraria % 3600 != 0 :
            horas = diferenciaHoraria / 3600
            minutos = (diferenciaHoraria % 3600) / 60
            print("Faltan", int(horas), "horas y", int(minutos), "minutos para ir a casa!" )

# output =
# Muy temprano para trabajar! mejor anda a dormir...
