import Wheel as wh
import classcar as cc

mercedes_r350 = cc.Car("mercedes", "r350", "gasolina", "3500")
print("marca coche:", mercedes_r350.mar)
print("modelo del coche:", mercedes_r350.mod)
print("Tipo de combustible que lleva:", mercedes_r350.comb)
print("cilindrada del coche:", mercedes_r350.cili)

rueda = wh.Wheel(100, 8, 8)

prin = (print("rueda: ", rueda.pulgadas,"/",rueda.rod, "R",rueda.mm))
presion = float(input("presion:"))
rueda.set_pressure(presion)
print("presion neumatico:", rueda.presion)

