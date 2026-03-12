#format specifiers = {:flags} format a value based on that flags are inserted.

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces (dejar espacio a la izquierda si es que hacen falta si el numero es muy bajo).
# :03 = allocate and zero pad that many spaces (lo mismo que el de arriba, pero agrgando ceros (0).
# :< = left justify (margen a la izquierda)
# :> = right justify (margen a la derecha)
# :^ = center justify (centrado)
# :+ = use a plus sign to indicate positive value (va a indicar que es positivo)
# := = place sign to leftmost position
# :  = insert a space before positive numbers (solo agrega un espacio antes de mostrar la cantidad)
# :, = comma separator (esta es la más interesante, muestra las comas (,) para indicar miles o millones)

value1 = 2399.25
value2 = -1532.45687
value3 = 128.3534532

#feel free to practice below.

#we can also mix this.

print(f"{value2:020,.2f}") 