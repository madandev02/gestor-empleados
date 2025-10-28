from datos import ingresar_datos # eliminar en caso que sea innecesario
from bono import calcular_bono # eliminar en caso que sea innecesario
from resumen import mostrar_resumen # eliminar en caso que sea innecesario


def mostrar_mensaje_despedida():
	print("\nGracias por usar el Gestor de Empleados de PyCompany.")
	print("Recuerda: programar es colaborar. ¡Hasta pronto!\n")


def main():
	nombre = edad = cargo = sueldo = porcentaje = None
	total = None

	while True:
		print("\n===== Gestor de Empleados - PyCompany =====")
		print("1. Ingresar datos del empleado")
		print("2. Calcular bono")
		print("3. Mostrar resumen")
		print("4. Salir")
		opcion = input("Elija una opción (1-4): ").strip()

		if opcion == '1':
			nombre, edad, cargo, sueldo, porcentaje = ingresar_datos()
			total = None
			print("\nDatos guardados correctamente.\n")

		elif opcion == '2':
			if sueldo is None or porcentaje is None:
				print("\nPrimero debe ingresar los datos del empleado (opción 1).\n")
			else:
				total = calcular_bono(sueldo, porcentaje)
				print(f"\nBono calculado. Sueldo total con bono: ${total:.2f}\n")

		elif opcion == '3':
			if nombre is None or total is None:
				print("\nAsegúrese de ingresar datos y calcular el bono antes de mostrar el resumen.\n")
			else:
				mostrar_resumen(nombre, edad, cargo, total)

		elif opcion == '4':
			mostrar_mensaje_despedida()
			break

		else:
			print("\nOpción no válida. Por favor ingrese 1, 2, 3 o 4.\n")


if __name__ == '__main__':
	main()

