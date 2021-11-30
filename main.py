import Wheel as wh

rueda = wh.Wheel(10, 3, 5)
print("diametro rueda:", rueda.mm)
print("rodadura:", rueda.rod)
print("ancho:", rueda.pulgadas)
presion = float(input("presion:"))
rueda.set_pressure(presion)
print("presion neumatico:", rueda.presion)

