# 👨‍💼 Gestor de Empleados – PyCompany

## 📘 Descripción del Proyecto

Este proyecto fue desarrollado como parte de la **actividad grupal “Gestor de Empleados con Funciones”**, cuyo propósito es aplicar los conceptos fundamentales de **Python**, tales como **funciones**, **operadores**, **tipos de datos** (`int`, `float`, `str`) y **estructuras de control** (`while`, `if`, `else`).

El programa simula un sistema interno de la empresa ficticia **PyCompany**, el cual permite **registrar empleados**, **calcular bonos salariales** y **mostrar un resumen del trabajador**.  
Se ejecuta desde consola y presenta un **menú interactivo** fácil de usar.

---

## 🎯 Objetivos

- Implementar funciones modulares en Python.  
- Utilizar conversiones de tipo (`int`, `float`, `str`).  
- Aplicar estructuras de control (`while`, `if`, `else`).  
- Mostrar mensajes claros y amigables para el usuario.  
- Practicar trabajo colaborativo utilizando **GitHub**.

---

## ⚙️ Funcionalidades

El programa cuenta con un menú principal que permite al usuario:

1. **Ingresar datos del empleado**  
   - Solicita nombre, edad, cargo, sueldo base y porcentaje de bono.

2. **Calcular bono salarial**  
   - Calcula el bono a partir del sueldo base y porcentaje ingresado.

3. **Mostrar resumen del empleado**  
   - Despliega todos los datos junto al total a recibir (sueldo + bono).

4. **Salir del programa**  
   - Finaliza la ejecución mostrando un mensaje de despedida personalizado.

---

## 🧠 Estructura del Proyecto

Cada integrante del grupo fue responsable de desarrollar una parte del programa según las funciones asignadas:

| Integrante | Función / Tarea | Archivo |
|-------------|------------------|----------|
| 1️⃣ | `ingresar_datos()` | `datos.py` |
| 2️⃣ | `calcular_bono()` | `bono.py` |
| 3️⃣ | `mostrar_resumen()` | `resumen.py` |
| 4️⃣ | Menú principal y `mostrar_mensaje_despedida()` | `main.py` |

---

## 🧩 Estructura de Archivos

```bash
gestor-empleados/
│
├── bono.py # Función para calcular el bono salarial
├── datos.py # Función para ingresar datos del empleado
├── resumen.py # Función para mostrar resumen del trabajador
├── main.py # Contiene el menú principal y la función de salida
└── README.md # Documentación del proyecto
```

## ▶️ Ejecución del Programa

1. Clonar este repositorio:

```bash
   git clone https://github.com/madandev02/gestor-empleados.git
   cd gestor-empleados
```

2. Ejecutar el programa:
```bash
python main.py
```

3. Seguir las instrucciones del menú en consola.

## 🧾 Ejemplo del Menú

===== GESTOR DE EMPLEADOS - PYCOMPANY =====
1. Ingresar datos del empleado
2. Calcular bono
3. Mostrar resumen del trabajador
4. Salir
Seleccione una opción:

## 🏁 Criterios de la evaluación
| Criterio                          | Descripción                                                      | Ponderación |
| --------------------------------- | ---------------------------------------------------------------- | ----------- |
| ✅ Uso correcto de funciones       | Cada función cumple un propósito y devuelve datos correctamente. | 25%         |
| 🔢 Conversiones de tipo           | Se aplican `str`, `int`, `float` donde corresponde.              | 20%         |
| 🔁 Uso de `while` y menú          | El menú se repite correctamente y permite salir.                 | 20%         |
| 🗣️ Mensajes claros y formateados | El programa es legible y amigable para el usuario.               | 15%         |
| 💬 Mensaje final personalizado    | Incluye mensaje de cierre solicitado.                            | 10%         |
| 🧑‍💻 Trabajo en equipo (GitHub)  | Subida colaborativa y commits de cada integrante.                | 10%         |

## 👥 Autores
- madandev02
- Stotelary 
- Fraan97

## 🐍 Requisitos

- Python 3.8 o superior
- Consola o terminal compatible con entrada de texto