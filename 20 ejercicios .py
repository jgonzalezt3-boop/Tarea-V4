# 20 EJERCICIOS — CLASES Y COLECCIONES CON
#MÉTODOS REUTILIZABLES
# EJERCICIO 1 — Validador de notas con promedio
# Clase: Calificador
# Nivel: Básico

#Entrada
#Una o varias notas mediante *args.
#Proceso
#Recibir las notas.
#Validar cada nota.
#Si está entre 0 y 100, guardarla.
#Ignorar las notas inválidas.
#Calcular el promedio de las notas válidas.
#Salida
#True o False al validar una nota.
#Lista con las notas válidas.
#Promedio de las notas almacenadas.

#Bosquejo
#85  -> válida  (0 <= 85 <= 100)
#92  -> válida
#110 -> inválida (> 100)
#78  -> válida
#-5  -> inválida (< 0)
#88  -> válida
#Entonces la lista queda: [85, 92, 78, 88]
#Suma: 85 + 92 + 78 + 88 = 343
#Cantidad de notas: 4
#Promedio: 343 / 4 = 85.75

#Identificar el patrón
#1. Método validar_nota(nota): Es un validador que usa una condición if. 
# Comprueba si la nota está entre 0 y 100. Si cumple la condición, retorna True; si no, retorna False.
#2. Método cargar_notas(*args): Recibe varias notas mediante *args. 
# Recorre todas las notas con un bucle for, llama al método validar_nota() para cada una y, si la nota es válida, la añade a la lista. 
# Aquí se aplica la reutilización del método validar_nota().
#3. Atributo notas: Es una lista que almacena las notas válidas. 
# Se inicializa vacía en __init__ y se va llenando cada vez que se encuentra una nota válida.
#4. Método promedio(): Calcula el promedio de las notas guardadas. 
# Usa sum() para sumar las notas y len() para saber cuántas notas hay. Si no hay notas, retorna 0.
#5. Constructor __init__: Inicializa la lista notas vacía. Su función es preparar el estado inicial del objeto.
#6. Conceptos aplicados: operadores de comparación (<=, >=), control de flujo (for, if), 
# funciones dentro de clases, colecciones (listas), *args, reutilización de métodos y cálculo de promedio.

class Calificador:
    
    def __init__(self,):
        self.notas = []
    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
# --- Programa principal ---

c = Calificador()
notas_validas = c.cargar_notas(85, 92, 110, 78, -5, 88)
suma = sum(notas_validas)
promedio = c.promedio()

print(f"Las notas válidas son: {notas_validas}")
print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")
print("-" * 50)

#Prueba de escritorio

#Paso	Nota	¿0 ≤ nota ≤ 100?	Acción	Lista de notas
#1	     85	           Sí	       Se agrega	[85]
#2	     92	           Sí	       Se agrega	[85, 92]
#3	    110	           No	      Se descarta	[85, 92]
#4	     78	           Sí	       Se agrega	[85, 92, 78]
#5	    -5	           No	       Se descarta	[85, 92, 78]
#6	    88	           Sí	       Se agrega	[85, 92, 78, 88]

#__________________________________________________________________________________________________

#EJERCICIO 2 — Contador de palabras únicas
#Clase: AnalizadorTexto
#Nivel: Básico
#Entrada
#Palabras individuales o en lotes (*args).
#Proceso
#Guardar cada palabra en un conjunto (evita duplicados) y en una lista
#(conserva el orden en que llegaron).
#Contar cuántas palabras únicas hay.
#Salida
#Cantidad de palabras únicas.

#Bosquejo
#Entrada: "hola", "mundo", "hola"
#Lista (orden):["hola", "mundo", "hola"]
#Conjunto (únicas): {"hola", "mundo"}
#Cantidad de palabras únicas: 2

#Descubrir el patrón
#1. Constructor __init__: Inicializa dos atributos.
#palabras_unicas es un conjunto (set) que almacena las palabras sin duplicados.
#historial_orden es una lista que guarda las palabras en el orden en que fueron agregadas.
#2. Método agregar_palabra(palabra): Agrega una palabra evitando duplicados.
#Primero utiliza if palabra not in self.palabras_unicas para comprobar si la palabra todavía no existe.
#Si no existe, la agrega tanto a la lista historial_orden como al conjunto palabras_unicas.
#Aquí se aplica la comprobación para evitar que la lista tenga palabras repetidas.
#3. Método contar_palabras(): Cuenta la cantidad de palabras únicas.
#Utiliza len(self.palabras_unicas) para conocer cuántos elementos tiene el conjunto.
#4. Método agregar_multiples(*args): Permite agregar varias palabras de una sola vez.
#Recibe las palabras mediante *args y utiliza un bucle for para recorrerlas.
#Por cada palabra llama al método agregar_palabra(), reutilizando ese método para evitar duplicados.
#5. Atributo palabras_unicas: Es un conjunto (set) que almacena únicamente las palabras que no se repiten.
#Por ejemplo, si se intenta agregar "hola" dos veces, el conjunto solamente conserva una.
#6. Atributo historial_orden: Es una lista que conserva las palabras en el orden en que fueron agregadas.
#La condición if palabra not in self.palabras_unicas es importante porque evita que una palabra repetida también se agregue nuevamente a esta lista.
#7. Conceptos aplicados: conjuntos (set), listas, if, operador not in, bucle for, *args, funciones dentro de clases, len(), atributos, constructor __init__ y reutilización de métodos.

class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.historial_orden = []
    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:   #Esto es importante porque set si elimina los duplicado por si solo, pero la lista no.
            self.historial_orden.append(palabra)
            self.palabras_unicas.add(palabra)
    def contar_palabras(self):
        return len(self.palabras_unicas)
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
        return self.historial_orden
    
# --- Programa principal ---
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola", "Pedro", "Pedro", "Ecuador")
print(f"Las palabras en orden son: {at.historial_orden}")
print(f"Las palabras únicas son: {at.palabras_unicas}")
print(f"La cantidad de palabras únicas es: {at.contar_palabras()}")
print("-" * 50)

#Prueba de escritorio 
#Paso	Palabra	¿Ya existe?	Acción	          Lista historial_orden	              Set palabras_unicas
#1	     "hola"	    No	   Se agrega	["hola"]	                                  {"hola"}
#2	     "mundo"	No	   Se agrega	["hola", "mundo"]	                       {"hola", "mundo"}
#3	     "hola"	    Sí	   Se descarta	["hola", "mundo"]	                       {"hola", "mundo"}
#4	    "Pedro"	    No	   Se agrega	["hola", "mundo", "Pedro"]	               {"hola", "mundo", "Pedro"}
#5	    "Pedro"	    Sí	   Se descarta	["hola", "mundo", "Pedro"]	               {"hola", "mundo", "Pedro"}
#6	   "Ecuador"	No	   Se agrega	["hola", "mundo", "Pedro", "Ecuador"]	   {"hola", "mundo", "Pedro",
#_________________________________________________________________________________________

#EJERCICIO 3 — Gestor de compras con totales
#Clase: CarroCompras
#Nivel: Básico

#Entrada
#Nombres de artículos y sus precios.
#Proceso
#Guardar cada artículo en un diccionario {nombre: precio}.
#Sumar todos los precios para obtener el total.
#Filtrar artículos cuyo precio esté dentro de un rango.
#Salida
#Total del carrito.
#Lista de artículos dentro de un rango de precio.

#Bosquejo
#Agregar_articulo("pan", 2.50) -> {"pan": 2.50}
#Agregar_articulo("leche", 3.00) -> {"pan": 2.50, "leche": 3.00}
#Total_carrito() = 2.50 + 3.00 = 5.50
#Articulos_por_rango(2, 3): ambos precios (2.50 y 3.00) están en [2, 3] -> ["pan", "leche"]

#Descubrir el patrón
#1. Constructor __init__: Inicializa el atributo articulos como un diccionario vacío.
#El diccionario almacenará el nombre de cada artículo como clave y su precio como valor.
#2. Método agregar_articulo(nombre, precio): Agrega un artículo al diccionario.
#Utiliza nombre como clave y precio como valor.
#Por ejemplo, "pan": 2.50.
#3. Método total_carrito(): Calcula el precio total de todos los artículos.
#Primero crea total = 0 y luego utiliza un bucle for para recorrer los precios con .values().
#Cada precio se va sumando a total mediante total = total + precio.
#4. Método articulos_por_rango(precio_min, precio_max): Busca los artículos cuyo precio se encuentra dentro de un rango.
#Recorre el diccionario utilizando .items() para obtener el nombre y el precio.
#La condición precio_min <= precio <= precio_max comprueba si el precio está dentro del rango indicado. Si cumple, agrega el nombre a la lista resultado.
#5. Atributo articulos: Es un diccionario que almacena los artículos y sus precios.
#Por ejemplo: {"pan": 2.50, "leche": 3.00}.
#6. Atributo total: Es una variable acumuladora que comienza en 0.
#Se utiliza para ir sumando cada precio hasta obtener el total del carrito.
#7. Conceptos aplicados: diccionarios, claves y valores, listas, bucle for, 
#condiciones if, operadores de comparación (<=), .values(), .items(), variables acumuladoras, parámetros y métodos dentro de una clase.

class CarroCompras:

    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total = total + precio
        return total
    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


# --- Programa principal ---
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
c.agregar_articulo("Aceite", 4.50)
c.agregar_articulo("Queso", 6.00)
total = c.total_carrito()
articulos = c.articulos_por_rango(2.00, 3.00)
print(f"Los artículos del carrito son: {c.articulos}")
print(f"El total del carrito es: ${total:.2f}")
print(f"Los artículos entre $2.00 y $3.00 son: {articulos}")
print("-" * 50)

#Prueba de escritorio
#Paso	Artículo	Precio	Acción	Diccionario articulos
#1	      pan	    2.50	Se agrega	{"pan": 2.50}
#2	     leche	    3.00	Se agrega	{"pan": 2.50, "leche": 3.00}
#3	    Aceite	    4.50	Se agrega	{"pan": 2.50, "leche": 3.00,...}
#4	     Queso	    6.00	Se agrega	{"pan": 2.50, "leche": 3.00,...}

#___________________________________________________________________________________________

#EJERCICIO 4 — Inversor de secuencias
#Clase: InversorSecuencia
#Nivel: Medio

#Entrada
#Una lista, o varias listas.
#Proceso
#Invertir manualmente el orden de una lista (sin usar reversed()).
#Reutilizar esa inversión para varias listas a la vez y guardarlas en un diccionario {lista_original:lista_invertida}.
#Salida
#Lista invertida, o diccionario con varias inversiones.

#Bosquejo
#Entrada: [1, 2, 3]
#Recorremos desde el último índice (2) hasta el primero (0):
#índice 2 -> 3
#índice 1 -> 2
#índice 0 -> 1
#Resultado: [3, 2, 1]

#Descubrir el patrón
#1. Método invertir_lista(lista): Invierte el orden de los elementos de una lista.
#Primero crea una lista vacía llamada invertida. Después utiliza un bucle for con range() para recorrer la lista desde el último elemento hasta el primero.
#Cada elemento se agrega a invertida utilizando append().
#2. Método invertir_multiples(*listas): Permite invertir varias listas utilizando *args.
#Recorre cada lista recibida con un bucle for y utiliza el método invertir_lista() para invertirla.
#El resultado se guarda en un diccionario, donde la lista original convertida en tupla es la clave y la lista invertida es el valor.
#3. Variable invertida: Es una lista vacía que se utiliza para almacenar los elementos de la lista original en orden inverso.
#Se va llenando mediante append() mientras el for recorre los índices desde el último hasta el primero.
#4. Variable resultado: Es un diccionario que almacena las listas originales y sus respectivas listas invertidas.
#Se utiliza tuple(lista) porque una lista no puede utilizarse directamente como clave de un diccionario.
#5. Uso de range(len(lista) - 1, -1, -1): Permite recorrer los índices de la lista hacia atrás.
#len(lista) - 1 representa el último índice, -1 indica que se detiene antes de llegar a -1, y el último -1 indica que avanza de uno en uno hacia atrás.
#6. Uso de tuple(lista): Convierte temporalmente la lista en una tupla.
#Esto permite utilizarla como clave del diccionario, ya que las listas no pueden ser claves de un diccionario.
#7. Conceptos aplicados: listas, diccionarios, tuplas, for, range(), len(), append(), *args, índices, recorrido inverso, reutilización de métodos y retorno de resultados.

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

# --- Programa principal ---
inv = InversorSecuencia()
lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d"]
lista3 = [10, 20, 30]
invertida = inv.invertir_lista(lista1)
print(f"La lista original es: {lista1}")
print(f"La lista invertida es: {invertida}")
resultado = inv.invertir_multiples(lista1, lista2, lista3)
print(f"Las listas originales e invertidas son: {resultado}")
print("-" * 50)

#Prueba de escritorio
#Paso	Índice i	lista[i]	Acción	invertida
#1	      4	   5	Se agrega     5	       [5]
#2	      3	   4	Se agrega     4	     [5, 4]
#3	      2	   3	Se agrega     3	    [5, 4, 3]
#4	      1	   2	Se agrega     2	   [5, 4, 3, 2]
#5	      0	   1	Se agrega     1	  [5, 4, 3, 2, 1]

#_____________________________________________________________________________________________________

#EJERCICIO 5 — Detector de números pares e impares
#Clase: AnalizadorNumeros
#Nivel: Básico

#Entrada
#Números en lote (*numeros).
#Proceso
#Clasificar cada número en par o impar usando el operador %.
#Separar todos los números en un diccionario {'pares': [...], 'impares':[...]}.
#Contar cuántos pares e impares hay.
#Salida
#Diccionario con las dos listas.
#Tupla (cantidad_pares, cantidad_impares).

#Bosquejo
#Entrada: 1, 2, 3, 4, 5
#1 -> impar
#2 -> par
#3 -> impar
#4 -> par
#5 -> impar
#pares = [2, 4] ; impares = [1, 3, 5]
#cantidad_pares_impares() = (2, 3)

#Descubrir el patrón ====================
#1. Constructor __init__: Inicializa dos listas vacías.
#pares almacenará los números pares e impares almacenará los números impares.
#El constructor prepara el estado inicial del objeto.
#2. Método es_par(numero): Comprueba si un número es par.
#Utiliza el operador % para obtener el residuo de la división entre 2.
#Si numero % 2 == 0, significa que el número es divisible entre 2 y retorna True; de lo contrario, retorna False.
#3. Método separar(*numeros): Recibe varios números mediante *args y los separa en pares e impares.
#Primero reinicia las listas pares e impares para comenzar una nueva clasificación.
#Después utiliza un for para recorrer cada número y reutiliza el método es_par() para determinar dónde debe almacenarse.
#4. Atributos pares e impares: Son listas que almacenan los números clasificados según su tipo.
#pares guarda los números divisibles entre 2 e impares guarda los que no son divisibles entre 2.
#5. Método cantidad_pares_impares(): Cuenta cuántos números pares e impares fueron clasificados.
#Utiliza len() para conocer la cantidad de elementos de cada lista y retorna ambos valores dentro de una tupla.
#6. Reinicio de las listas: Dentro de separar() aparecen:
#self.pares = []
#self.impares = []
#Esto permite limpiar las clasificaciones anteriores antes de procesar nuevos números.
#7. Conceptos aplicados: clases, constructor __init__, listas, if/else, operador módulo %, for, *args, len(), tuplas, True y False, y reutilización de métodos.

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []
    def es_par(self, numero):
        return numero % 2 == 0
    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {'pares': self.pares,'impares': self.impares}
    def cantidad_pares_impares(self):
        return (len(self.pares),
len(self.impares))
    
# --- Programa principal ---
an = AnalizadorNumeros()
clasificados = an.separar(1, 2, 3, 4, 5)
print(f"Clasificados:, {clasificados}")
print(f"Cantidades (pares, impares): {an.cantidad_pares_impares()}")
print("-" * 50)

#Prueba de escritorio
#Paso	Número	numero % 2 == 0	     Acción	       Pares  Impares
#1	      1	      No → False	Se agrega a impares	[]	    [1]
#2	      2	      Sí → True	    Se agrega a pares	[2]	    [1]
#3	      3	      No → False	Se agrega a impares	[2]	    [1, 3]
#4	      4	      Sí → True	    Se agrega a pares	[2, 4]	[1, 3]
#5	      5	      No → False	Se agrega a impares	[2, 4]	[1, 3, 5]

#_______________________________________________________________________________________________

#EJERCICIO 6 — Estadísticas de temperatura
#Clase: GestorTemperatura
#Nivel: Medio

#Entrada
#Temperaturas individuales o en lote (*temps).
#Proceso
#Guardar cada temperatura en una lista.
#Calcular mínima, máxima y promedio de las temperaturas guardadas.
#Salida
#Valores estadísticos: mínima, máxima, promedio.

#Bosquejo
#Entrada: 20, 25, 18, 30
#Lista: [20, 25, 18, 30]
#Mínima: 18
#Máxima: 30
#Suma: 20 + 25 + 18 + 30 = 93
#Cantidad: 4
#Promedio: 93 / 4 = 23.25

#Descubrir el patrón
#1. Constructor __init__: Inicializa el atributo temperaturas como una lista vacía.
#Esta lista se utilizará para almacenar todas las temperaturas registradas.
#2. Método registrar_temperatura(temp): Agrega una temperatura a la lista.
#Utiliza append() para colocar el valor recibido al final de self.temperaturas.
#3. Método minima(): Obtiene la temperatura más baja de la lista.
#Utiliza la función min() para encontrar el menor valor almacenado.
#4. Método maxima(): Obtiene la temperatura más alta de la lista.
#Utiliza la función max() para encontrar el mayor valor almacenado.
#5. Método promedio(): Calcula el promedio de todas las temperaturas registradas.
#Utiliza sum() para sumar las temperaturas y len() para saber cuántas temperaturas existen. Después divide la suma para la cantidad.
#6. Método registrar_multiples(*temps): Permite registrar varias temperaturas al mismo tiempo.
#Recibe varios valores mediante *args y utiliza un for para recorrerlos. Por cada temperatura reutiliza el método registrar_temperatura() para agregarla a la lista.
#7. Atributo temperaturas: Es una lista que almacena todas las temperaturas registradas.
#Se inicializa vacía en el constructor y se va llenando mediante registrar_temperatura().
#8. Conceptos aplicados: clases, constructor __init__, listas, append(), min(), max(), sum(), len(), for, *args, reutilización de métodos y cálculo de promedio.

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)
    def minima(self):
        return min(self.temperaturas)
    def maxima(self):
        return max(self.temperaturas)
    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)
    def registrar_multiples(self, *temps):
        for temp in temps: 
            self.registrar_temperatura(temp)
        return self.temperaturas
    
# --- Programa principal ---
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(f"Temperaturas: {gt.temperaturas}°C")
print(f"Mínima: {gt.minima()}°C")
print(f"Máxima: {gt.maxima()}°C")
print(f"Promedio: {gt.promedio()}°C")
print("-" * 50)

#Prueba de escritorio
#Paso	Temperatura	  Acción	  Lista temperaturas
#1	       20 °C	Se registra	       [20]
#2	       25 °C	Se registra	     [20, 25]
#3	       18 °C	Se registra	    [20, 25, 18]
#4	       30 °C	Se registra	   [20, 25, 18, 30]

#_____________________________________________________________________________________________________________________

#EJERCICIO 7 — Mapeador de edades
#Clase: GestorPersonas
#Nivel: Básico

#Entrada
#Nombres y edades de personas.
#Proceso
#Guardar cada persona en un diccionario {nombre: edad}.
#Filtrar personas cuya edad sea mayor o igual a un mínimo.
#Calcular el promedio de todas las edades.
#Salida
#Lista de nombres filtrados.
#Promedio de edades.

#Bosquejo
#agregar_persona("Ana", 28) -> {"Ana": 28}
#agregar_persona("Bob", 17) -> {"Ana": 28, "Bob": 17}
#personas_mayores(18): 28 >= 18 (sí) ; 17 >= 18 (no)
#edad_promedio() = (28 + 17) / 2 = 22.5

#Descubrir el patrón 
#1. Constructor __init__: Inicializa el atributo personas como un diccionario vacío.
#El diccionario almacenará el nombre de cada persona como clave y su edad como valor.
#Por ejemplo: "Ana": 25.
#2. Método agregar_persona(nombre, edad): Agrega una persona al diccionario.
#Utiliza el nombre como clave y la edad como valor. Cada vez que se llama al método, se registra una nueva persona.
#3. Método personas_mayores(edad_minima): Busca las personas que tienen una edad mayor o igual al límite indicado.
#Primero crea una lista vacía llamada resultado. Después recorre el diccionario utilizando .items() para obtener el nombre y la edad.
#Con if edad >= edad_minima comprueba si cumple la condición y, si es así, agrega el nombre a la lista.
#4. Método edad_promedio(): Calcula el promedio de las edades registradas.
#Primero crea total = 0. Luego utiliza un for para recorrer las edades mediante .values().
#En cada vuelta, la edad se suma al total con total = total + edad. Finalmente, divide el total entre la cantidad de personas usando len().
#5. Atributo personas: Es un diccionario que almacena los nombres y edades de las personas.
#La clave es el nombre y el valor corresponde a la edad.
#6. Variable resultado: Es una lista que almacena los nombres de las personas que cumplen con la edad mínima solicitada.
#Comienza vacía y se llena mediante append().
#7. Variable total: Es una variable acumuladora.
#Comienza en 0 y va sumando una edad en cada repetición del for hasta obtener la suma total de las edades.
#8. Conceptos aplicados: diccionarios, claves y valores, listas, for, if, operador de comparación >=, .items(), .values(), append(), len(), variable acumuladora y cálculo de promedio.

class GestorPersonas:

    def __init__(self):
        self.personas = {}
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado
    def edad_promedio(self):
        total = 0
        for edad in self.personas.values():
            total = total + edad  #La edad la va sumando de uno en uno en el total
        return total / len(self.personas)

# --- Programa principal ---
gp = GestorPersonas()

gp.agregar_persona("Ana", 25)
gp.agregar_persona("Carlos", 17)
gp.agregar_persona("Pedro", 20)
mayores = gp.personas_mayores(18)
print(f"Las personas registradas son: {gp.personas}")
print(f"Las personas mayores o iguales a 18 años son: {mayores}")
print(f"La edad promedio es: {gp.edad_promedio():.2f} años")
print("-" * 50)

#Prueba de escritorio
#Paso	Nombre	Edad	Acción	          Diccionario personas
#1	     Ana	25	   Se agrega	{"Ana": 25}
#2	    Carlos	17	   Se agrega	{"Ana": 25, "Carlos": 17}
#3	   Pedro	20	   Se agrega	{"Ana": 25, "Carlos": 17, "Pedro": 20}

#_____________________________________________________________________________

#EJERCICIO 8 — Asignador de equipos
#Clase: Equipos
#Nivel: Medio
#Entrada
#Nombres de equipos y de jugadores.
#Proceso
#Crear la estructura equipo -> [jugadores] en un diccionario.
#Agregar jugadores a un equipo existente.
#Contar jugadores por equipo y comparar para encontrar el mayor.
#Salida
#Nombre del equipo con más integrantes.

#Bosquejo


#Descubrir el patrón
#1. Constructor __init__: Inicializa el atributo equipos como un diccionario vacío.
#Este diccionario almacenará el nombre de cada equipo como clave y una lista de jugadores como valor.
#2. Método crear_equipo(nombre_equipo): Crea un nuevo equipo dentro del diccionario.
#Utiliza nombre_equipo como clave y asigna una lista vacía [] como valor.
#Por ejemplo: "A": [].
#3. Método agregar_jugador(equipo, jugador): Agrega un jugador a un equipo existente.
#Busca el equipo dentro del diccionario y utiliza append() para añadir el jugador a la lista correspondiente.
#4. Método equipo_mayor_integrantes(): Determina qué equipo tiene la mayor cantidad de jugadores.
#Primero crea equipo_mayor = "" para guardar el nombre del equipo con más integrantes y mayor_cantidad = 0 para guardar la cantidad mayor encontrada.
#5. Recorrido de los equipos: Utiliza un for con .items() para obtener el nombre del equipo y su lista de jugadores.
#Después utiliza len(jugadores) para contar cuántos integrantes tiene cada equipo.
#6. Condición if len(jugadores) > mayor_cantidad: Compara la cantidad de jugadores del equipo actual con la mayor cantidad encontrada anteriormente.
#Si la cantidad actual es mayor, actualiza mayor_cantidad y guarda el nombre del equipo en equipo_mayor.
#7. Atributo equipos: Es un diccionario que almacena los equipos y sus jugadores.
#Cada equipo tiene como valor una lista donde se van agregando sus integrantes.
#8. Variables equipo_mayor y mayor_cantidad:
#equipo_mayor almacena el nombre del equipo con más jugadores.
#mayor_cantidad almacena la cantidad de integrantes del equipo que lleva la mayor cantidad hasta ese momento.
#9. Conceptos aplicados: diccionarios, listas, .items(), for, if, len(), append(), comparación >, variables acumuladoras y búsqueda del valor mayor.

class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        equipo_mayor = ""
        mayor_cantidad = 0
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo
        return equipo_mayor
    
# --- Programa principal ---
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Maria")
print(f"Equipos: {eq.equipos}")
print(f"Equipo con más integrantes: {eq.equipo_mayor_integrantes()}")
print("-" * 50)

#Prueba de escritorio
#Paso	Equipo	Acción	Diccionario equipos
#1	      A	   Se crea	{"A": []}
#2	      B	   Se crea	{"A": [], "B": []}

#_________________________________________________________________________________

#EJERCICIO 9 — Validador de caracteres
#Clase: AnalizadorString
#Nivel: Básico

#Entrada
#Textos para analizar.
#Proceso
#Recorrer el texto carácter a carácter.
#Clasificar cada carácter en vocal, consonante o dígito.
#Guardar el texto más largo analizado hasta el momento.
#Salida
#Diccionario con los conteos {'vocales':..., 'consonantes':..., 'digitos':...}.

#Bosquejo
#Entrada: "Hola123"
#H -> consonante
#o -> vocal
#l -> consonante
#a -> vocal
#1 -> dígito
#2 -> dígito
#3 -> dígito
#vocales = 2, consonantes = 2, digitos = 3

#Descubrir el patrón 
#1. Constructor __init__: Inicializa el atributo texto_mas_largo como una cadena vacía "".
#Este atributo se utiliza para guardar el texto que tenga mayor longitud de todos los textos analizados.
#2. Método solo_vocales(letra): Comprueba si una letra es una vocal.
#Utiliza lower() para convertir la letra a minúscula y después comprueba si pertenece a "aeiou".
#Retorna True si es una vocal y False si no lo es.
#3. Método contar_por_tipo(texto): Cuenta cuántas vocales, consonantes y dígitos existen en un texto.
#Primero crea tres contadores: vocales, consonantes y digitos, todos iniciados en 0.
#4. Bucle for letra in texto: Recorre el texto carácter por carácter.
#En cada repetición analiza si el carácter es una vocal, una consonante o un dígito.
#5. Condición if self.solo_vocales(letra): Utiliza el método solo_vocales() para comprobar si el carácter es una vocal.
#Si retorna True, aumenta el contador vocales en uno.
#6. Condición elif letra.isalpha(): Comprueba si el carácter es una letra.
#Si es una letra pero no fue identificada como vocal, se considera consonante y aumenta consonantes en uno.
#7. Condición elif letra.isdigit(): Comprueba si el carácter es un número.
#Si es un dígito, aumenta el contador digitos en uno.
#8. Comparación del texto más largo: Después de analizar el texto, utiliza len() para comparar su longitud con texto_mas_largo.
#Si el texto actual tiene más caracteres, se guarda en self.texto_mas_largo.
#9. Retorno del resultado: El método devuelve un diccionario con tres elementos: vocales, consonantes y digitos, junto con sus respectivas cantidades.
#10. Atributo texto_mas_largo: Guarda el texto con mayor cantidad de caracteres de todos los textos analizados.
#Se actualiza cada vez que se encuentra un texto más largo.
#11. Conceptos aplicados: clases, constructor __init__, cadenas de texto, for, if/elif, lower(), isalpha(), isdigit(), len(), diccionarios, contadores, True y False, y reutilización de métodos.

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""
    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"
    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0
        for letra in texto:
            if self.solo_vocales(letra):
                vocales = vocales + 1
            elif letra.isalpha():
                consonantes = consonantes + 1
            elif letra.isdigit():
                digitos = digitos + 1
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }

# --- Programa principal ---
astr = AnalizadorString()

resultado1 = astr.contar_por_tipo("Hola123")
resultado2 = astr.contar_por_tipo("Python2026")
print(f"Resultado del primer texto: {resultado1}")
print(f"Resultado del segundo texto: {resultado2}")
print(f"El texto más largo analizado es: {astr.texto_mas_largo}")
print("-" * 50)

#Prueba de escritorio
#Paso	Letra	¿Vocal?	¿Es letra?	¿Es dígito?	Acción	Vocales	Consonantes	Dígitos
#1	      H	      No	    Sí	         No	     Suma consonante	0	1	0
#2	      o	      Sí	    —	         —	     Suma vocal	        1	1	0
#3	      l	      No	    Sí	         No	     Suma consonante	1	2	0
#4	      a	      Sí	    —	         —	     Suma vocal	        2	2	0
#5	      1	      No	    No	         Sí	     Suma dígito    	2	2	1
#6	      2	      No	    No	         Sí	     Suma dígito	    2	2	2

#__________________________________________________________________________________

#EJERCICIO 10 — Gestor de tareas con prioridad
#Clase: Tareas
#Nivel: Medio

#Entrada
#Descripciones de tareas y su prioridad.
#Proceso
#Guardar cada tarea como una tupla (descripcion, prioridad) en una lista.
#Filtrar las tareas de prioridad "alta".
#Eliminar una tarea de la lista por su descripción.
#Salida
#Lista de tareas filtradas por prioridad.

#Bosquejo


#Describir el patrón
#1. Constructor __init__: Inicializa el atributo tareas como una lista vacía.
#Esta lista almacenará todas las tareas que se agreguen al programa.
#2. Método agregar_tarea(descripcion, prioridad): Permite agregar una nueva tarea.
#Primero crea una tupla llamada tarea que contiene la descripción y la prioridad. Después utiliza append() para agregar esa tupla a la lista tareas.
#3. Tupla tarea: Almacena dos datos de cada tarea: la descripción y la prioridad.
#La posición 0 corresponde a la descripción y la posición 1 corresponde a la prioridad.
#Por ejemplo:
#("Hacer tarea de Python", "alta")
#tarea[0] → "Hacer tarea de Python"
#tarea[1] → "alta"
#4. Método tareas_prioritarias(): Busca las tareas que tienen prioridad "alta".
#Crea una lista vacía llamada resultado, recorre todas las tareas con un for y utiliza tarea[1] para obtener la prioridad.
#lower() convierte la prioridad a minúsculas para poder compararla con "alta".
#5. Condición if tarea[1].lower() == "alta": Comprueba si la prioridad de la tarea es "alta".
#Si se cumple, la tarea completa se agrega a resultado mediante append().
#6. Método eliminar_completada(descripcion): Busca una tarea específica por su descripción y la elimina de la lista.
#Utiliza un for para recorrer las tareas y tarea[0] para obtener la descripción.
#7. Uso de remove(): Cuando encuentra la tarea indicada, utiliza self.tareas.remove(tarea) para eliminarla de la lista.
#8. Uso de break: Después de eliminar la tarea, utiliza break para detener el for.
#Esto evita continuar recorriendo la lista después de encontrar y eliminar la tarea.
#9. Atributo tareas: Es una lista que almacena todas las tareas registradas.
#Cada elemento de la lista es una tupla formada por descripción y prioridad.
#10. Conceptos aplicados: listas, tuplas, for, if, append(), remove(), break, posiciones de una tupla ([0] y [1]), lower(), comparación == y métodos dentro de una clase.

class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)
    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1].lower() == "alta":
                resultado.append(tarea)
        return resultado
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break

#Tarea 0 y 1 son las posiciones de los parametros

# --- Programa principal ---
t = Tareas()
t.agregar_tarea("Hacer tarea de Python", "alta")
t.agregar_tarea("Estudiar para el examen", "alta")
t.agregar_tarea("Ordenar el cuarto", "baja")
print(f"Todas las tareas son: {t.tareas}")
print(f"Las tareas de prioridad alta son: {t.tareas_prioritarias()}")
t.eliminar_completada("Ordenar el cuarto")
print(f"Las tareas después de eliminar son: {t.tareas}")
print("-" * 50)

#Prueba de escritorio
#Paso	Descripción	          Prioridad	 Acción	           Lista tareas
#1	    Hacer tarea de Python	alta	Se agrega	[("Hacer tarea de Python", "alta")]
#2	    Estudiar para el examen	alta	Se agrega	[("Hacer tarea de Python", "alta"), ("Estudiar para el examen", "alta")]
#3	    Ordenar el cuarto	    baja	Se agrega	[("Hacer tarea de Python", "alta"), ("Estudiar para el examen", "alta"), ("Ordenar el cuarto", "baja")]

#____________________________________________________________________

#EJERCICIO 11 — Contador de frecuencia
#Clase: ContadorFrecuencia
#Nivel: Básico

#Entrada
#Elementos individuales o en lote.
#Proceso
#Guardar cada elemento en un diccionario,contando sus repeticiones.
#Encontrar el elemento con mayor frecuencia.
#Consultar cuántas veces apareció un elemento específico.
#Salida
#Elemento más frecuente.
#Frecuencia (cantidad de apariciones) de un elemento.

#Bosquejo
#agregar_elemento("a") -> {"a": 1}
#agregar_elemento("b") -> {"a": 1, "b": 1}
#agregar_elemento("a") -> {"a": 2, "b": 1}
#elemento_mas_frecuente() -> "a" (2 apariciones contra 1)

#Descubrir el patrón
#1. Método agregar_elemento(elemento): Es un método que sirve para registrar un elemento y contar cuántas veces aparece.
#Usa self.frecuencias.get(elemento, 0) para obtener la cantidad actual del elemento. Si no existe, toma 0, y luego suma 1.
#Finalmente, guarda el elemento con su nueva frecuencia en el diccionario.
#2. Método elemento_mas_frecuente(): Busca el elemento que aparece más veces en el diccionario.
#Utiliza max() para encontrar la frecuencia más alta y key=self.frecuencias.get para comparar los elementos según su cantidad de apariciones.
#Retorna el elemento que tiene la mayor frecuencia.
#3. Método frecuencia_elemento(elemento): Sirve para consultar cuántas veces aparece un elemento específico.
#Utiliza .get(elemento, 0), por lo que si el elemento existe devuelve su frecuencia y si no existe devuelve 0.
#4. Atributo frecuencias: Es un diccionario que almacena los elementos y la cantidad de veces que aparecen.
#Se inicia vacío y se va llenando mediante el método agregar_elemento().
#Por ejemplo, al final tendrá {"a": 2, "b": 1}.
#5. Constructor __init__: Inicializa el atributo frecuencias como un diccionario vacío.
#Su función es preparar el estado inicial del objeto antes de comenzar a agregar elementos.
#6. Programa principal: Se crea el objeto cf y se agregan los elementos "a", "b" y nuevamente "a".
#Después se imprimen las frecuencias, el elemento más frecuente y la frecuencia específica de "a".
#7. Conceptos aplicados: Diccionarios, clases, objetos, constructor __init__, métodos, self, .get(), max(), key=, return, suma + 1 y f-strings.

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1
    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)
    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

# --- Programa principal ---
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(f"Frecuencias: {cf.frecuencias}")
print(f"Elemento más frecuente: {cf.elemento_mas_frecuente()}")
print(f"Frecuencia de 'a': {cf.frecuencia_elemento("a")}")
print("-" * 50)

#Prueba de escritorio
#Paso	Elemento	Frecuencia anterior	        Acción         	Diccionario
#1	      "a"        	0	            Se agrega y aumenta 1	{"a": 1}
#2	      "b"	        0	            Se agrega y aumenta 1	{"a": 1, "b": 1}
#3	      "a"	        1	            Se aumenta 1	        {"a": 2, "b": 1}

#_________________________________________________________________________________

#EJERCICIO 12 — Selector de rango con tuplas
#Clase: SelectorRango
#Nivel: Medio

#Entrada
#Pares (inicio, fin) para varios rangos.
#Proceso
#Crear un rango como tupla de números entre inicio y fin.
#Unir varios rangos en una sola lista, sin elementos duplicados.
#Salida
#Lista de elementos únicos combinando todos los rangos.

#Bosquejo
#crear_rango(1, 3) -> (1, 2, 3)
#crear_rango(2, 4) -> (2, 3, 4)
#Unión sin duplicados: {1, 2, 3, 4}
#elementos_en_multiples_rangos((1,3), (2,4)) -> [1, 2, 3, 4]

#Descubrir el patrón
#1. Método crear_rango(inicio, fin): Es un método que crea un rango de números desde inicio hasta fin.
#Utiliza range(inicio, fin + 1) para incluir también el número final.
#Después utiliza tuple() para convertir el rango en una tupla y finalmente retorna el resultado.
#2. Método elementos_en_multiples_rangos(*rangos): Recibe varios rangos mediante *rangos.
#Crea un conjunto vacío llamado conjunto para almacenar los números sin repetir.
#Recorre cada rango con un for, separando cada rango en inicio y fin.
#Luego llama al método crear_rango() y utiliza update() para agregar todos sus elementos al conjunto.
#3. Atributo conjunto: Es un set que almacena los números de los diferentes rangos.
#Se utiliza un conjunto porque automáticamente evita que se repitan los elementos.
#4. Método sorted(): Después de combinar los rangos, se utiliza sorted(conjunto).
#Su función es ordenar los elementos del conjunto de menor a mayor.
#Finalmente retorna la lista ordenada.
#5. Constructor: Esta clase no tiene un método __init__, porque no necesita inicializar ningún atributo.
#Los datos se crean directamente dentro de los métodos cuando son necesarios.
#6. Programa principal: Se crea el objeto sr.
#Primero se crea el rango (1, 3) y después se combinan los rangos (1, 3) y (2, 4).
#Los números repetidos se eliminan gracias al set.
#7. Conceptos aplicados: Clases, objetos, métodos, range(), tuplas, conjuntos set, *args, bucle for, update(), sorted(), return y eliminación automática de elementos repetidos.

class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))
    def elementos_en_multiples_rangos(self, *rangos):
        conjunto = set()
        for inicio, fin in rangos:     
            conjunto.update(self.crear_rango(inicio,fin))
        return sorted(conjunto)
    
# --- Programa principal ---
sr = SelectorRango()
print(f"Rango (1,3): {sr.crear_rango(1, 3)}")
print(f"Combinación de rangos: {sr.elementos_en_multiples_rangos((1, 3),(2, 4))}")
print("-" * 50)

#Prueba de escritorio
#Paso	Número	Acción	    Tupla
#1     	1	   Se agrega	(1,)
#2	    2	   Se agrega	(1, 2)
#3	    3	   Se agrega	(1, 2, 3)

#_____________________________________________________________________________________________________

#EJERCICIO 13 — Combinador de listas
#Clase: CombinadorListas
#Nivel: Básico

#Entrada
#Dos o más listas.
#Proceso
#Alternar los elementos de dos listas (intercalar).
#Reutilizar el intercalado para combinar varias listas a la vez.
#Salida
#Lista intercalada.

#Bosquejo
#intercalar([1,2], [3,4]):
#índice 0: 1 (de lista1), 3 (de lista2)
#índice 1: 2 (de lista1), 4 (de lista2)
#Resultado: [1, 3, 2, 4]
#intercalar_multiples([1,2], [3,4], [5,6]):
#paso 1: intercalar([1,2],[3,4]) = [1,3,2,4]
#paso 2: intercalar([1,3,2,4],[5,6]) = [1,5,3,6,2,4]

#Descubrir el patrón
#1. Método intercalar(lista1, lista2): Es un método que sirve para combinar dos listas alternando sus elementos.
#Primero crea una lista vacía llamada resultado. Después utiliza max() para obtener el tamaño de la lista más grande.
#Con un for recorre las posiciones y, mediante if, verifica si existe un elemento en cada lista antes de agregarlo.
#2. Variable resultado: Es una lista vacía que almacena los elementos de las listas que se van intercalando.
#Se utiliza append() para agregar cada elemento al final de la lista.
#3. Variable max_len: Guarda el tamaño de la lista más grande.
#Se obtiene utilizando max(len(lista1), len(lista2)). Esto permite que el método funcione aunque las listas tengan diferentes tamaños.
#4. Condiciones if i < len(lista1) e if i < len(lista2): Comprueban si la posición i existe dentro de cada lista.
#Esto evita intentar acceder a una posición que no existe cuando una lista es más corta que la otra.
#5. Método intercalar_multiples(*listas): Permite intercalar más de dos listas utilizando *listas.
#Primero busca cuál es la lista con mayor cantidad de elementos y guarda su tamaño en mayor.
#Después utiliza dos bucles for: uno para recorrer las posiciones y otro para recorrer cada lista.
#Si la posición existe, agrega el elemento a resultado.
#6. Variable mayor: Comienza en 0 y almacena la cantidad de elementos de la lista más grande.
#Se actualiza cuando encuentra una lista cuya longitud sea mayor.
#7. Constructor: Esta clase no tiene __init__ porque no necesita inicializar atributos.
#Las listas resultado y las variables necesarias se crean directamente dentro de los métodos.
#8. Programa principal: Se crea el objeto cl y se prueban los dos métodos.
#Primero se intercalan dos listas y después se intercalan tres listas.
#9. Conceptos aplicados: Clases, objetos, métodos, listas, *args, for, if, len(), max(), append(), range() y return.

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiples(self, *listas):
        resultado = []
        mayor = 0
        for lista in listas:
            if len(lista) > mayor:
                mayor = len(lista)
        for i in range(mayor):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        return resultado

# --- Programa principal ---

cl = CombinadorListas()
print(f"Intercalar [1,2] y [3,4]: {cl.intercalar([1, 2], [3, 4])}")
print(f"Intercalar múltiples: {cl.intercalar_multiples([1, 2], [5, 6], [3, 4])}")
print("-" * 50)

#Prueba de escritorio
#Paso	i Elemento de lista1	Elemento de lista2	       Acción	         Resultado
#1	    0	     1	                   3	         Agrega 1 y luego 3	      [1, 3]
#2	    1	     2	                   4	         Agrega 2 y luego 4	   [1, 3, 2, 4]

#_____________________________________________________________________________________________

#EJERCICIO 14 — Mapeo de estudiantes a notas
#Clase: RegistroNotas
#Nivel: Medio

#Entrada
#Nombre de estudiante y su nota.
#Proceso
#Guardar cada estudiante en un diccionario {estudiante: nota}.
#Filtrar los estudiantes que superan una nota mínima.
#Encontrar al estudiante con la mejor nota.
#Salida
#Lista de estudiantes aprobados.
#Tupla (nombre, nota) del mejor estudiante.

#Bosquejo
#registrar("Ana", 95) -> {"Ana": 95}
#registrar("Bob", 70) -> {"Ana": 95, "Bob": 70}
#estudiantes_aprobados(75): 95 >= 75 (sí) ; 70 >= 75 (no) -> ["Ana"]
#mejor_estudiante(): comparar 95 vs 70 -> ("Ana", 95)

#Descubrir el patrón
#1. Constructor __init__: Inicializa el atributo notas como un diccionario vacío.
#El diccionario va a almacenar el nombre de cada estudiante junto con su nota. Por ejemplo: {"Ana": 85}.
#2. Método registrar(estudiante, nota): Sirve para registrar la nota de un estudiante.
#Recibe el nombre del estudiante y su nota, y los guarda en el diccionario notas.
#El nombre del estudiante funciona como clave y la nota como valor.
#3. Atributo notas: Es un diccionario que almacena los estudiantes y sus respectivas notas.
#Se inicializa vacío en __init__ y se va llenando cada vez que se utiliza registrar().
#4. Método estudiantes_aprobados(nota_minima): Busca los estudiantes que tienen una nota mayor o igual a la nota mínima establecida.
#Crea una lista llamada aprobados y recorre el diccionario con for.
#Utiliza la condición nota >= nota_minima y, si se cumple, agrega el nombre del estudiante a la lista.
#5. Método mejor_estudiante(): Busca al estudiante que tiene la nota más alta.
#Inicializa mejor_nombre como una cadena vacía y mejor_nota en 0.
#Recorre todos los estudiantes y compara cada nota con mejor_nota.
#Si encuentra una nota mayor, actualiza el nombre y la nota del mejor estudiante.
#Finalmente retorna ambos valores: mejor_nombre y mejor_nota.
#6. Variable aprobados: Guarda la lista que retorna el método estudiantes_aprobados(70).
#En este caso contiene los estudiantes que obtuvieron una nota de 70 o más.
#7. Variable mejor: Guarda el resultado que retorna mejor_estudiante().
#Como el método retorna dos valores, se guardan juntos en una tupla: nombre y nota.
#8. mejor[0] y mejor[1]: Se utilizan para acceder a los elementos de la tupla.
#mejor[0] contiene el nombre del estudiante y mejor[1] contiene su nota.
#9. Programa principal: Se crea el objeto rn y se registran tres estudiantes: Ana, Pedro y Sofía.
#Luego se muestran las notas registradas, los estudiantes aprobados con mínimo 70 y finalmente el estudiante con la nota más alta.
#10. Conceptos aplicados: Diccionarios, listas, tuplas, clases, objetos, constructor __init__, métodos, for, if, operadores de comparación (>=, >), .items(), append(), return y f-strings.

class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = 0
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return mejor_nombre, mejor_nota
    
# --- Programa principal ---
rn = RegistroNotas()
rn.registrar("Ana", 85)
rn.registrar("Pedro", 60)
rn.registrar("Sofía", 90)
print(f"Las notas registradas son: {rn.notas}")
aprobados = rn.estudiantes_aprobados(70)
print(f"Los estudiantes aprobados son: {aprobados}")
mejor = rn.mejor_estudiante()
print(f"El mejor estudiante es: {mejor[0]} con una nota de {mejor[1]}")
print("-" * 50)

#Prueba de escritorio 
#Paso	Estudiante	Nota	Acción	            Diccionario
#1	       Ana	     85	  Se registra	{"Ana": 85}
#2	      Pedro	     60	  Se registra	{"Ana": 85, "Pedro": 60}
#3	      Sofía	     90	  Se registra	{"Ana": 85, "Pedro": 60, "Sofía": 90}

#______________________________________________________________________________________________

#EJERCICIO 15 — Divisores de un número
#Clase: DivisorFinder
#Nivel: Básico

#Entrada
#Uno o varios números.
#Proceso
#Encontrar todos los divisores de un número con un bucle.
#Verificar si un número es perfecto (la suma de sus divisores propios,sin contar el número mismo, es igual al número).
#Repetir el proceso de divisores para varios números.
#Salida
#Tupla con los divisores.
#True/False si es perfecto.
#Diccionario {número: tupla_divisores}.

#Bosquejo

#Descubrir el patrón
#1. Método encontrar_divisores(numero): Es un método que busca todos los números que dividen exactamente al número indicado.
#Crea una lista vacía llamada divisores y utiliza un for para recorrer los números desde 1 hasta numero.
#Con la condición numero % i == 0 comprueba si el residuo de la división es 0. Si es así, significa que i es un divisor y se agrega a la lista.
#Al final, convierte la lista en una tupla utilizando tuple() y la retorna.
#2. Método es_perfecto(numero): Comprueba si un número es un número perfecto.
#Primero llama al método encontrar_divisores() para obtener sus divisores.
#Después crea suma = 0 y recorre los divisores.
#La condición divisor != numero evita sumar el mismo número que estamos analizando.
#Va acumulando los divisores en suma. Finalmente, si la suma es igual al número original, retorna True; de lo contrario, retorna False.
#3. Variable divisores: Es una lista que almacena los divisores encontrados por el método encontrar_divisores().
#Después esta lista se convierte en una tupla antes de ser retornada.
#4. Variable suma: Es un acumulador que comienza en 0.
#Se utiliza para sumar los divisores propios del número, es decir, todos sus divisores excepto el mismo número.
#5. Método encontrar_multiples_divisores(*numeros): Permite encontrar los divisores de varios números utilizando *numeros.
#Crea un diccionario vacío llamado resultado.
#Recorre cada número con un for, llama al método encontrar_divisores() y guarda el número junto con sus divisores en el diccionario.
#6. Variable resultado: Es un diccionario que almacena cada número como clave y sus divisores como valor.
#Por ejemplo: {6: (1, 2, 3, 6)}.
#7. Condición numero % i == 0: El operador % obtiene el residuo de una división.
#Si el resultado es 0, significa que el número se puede dividir exactamente entre i, por lo que i es un divisor.
#8. Programa principal: Se crea el objeto df y se prueban los tres métodos.
#Primero se buscan los divisores de 12, después se comprueba si 6 y 12 son números perfectos y finalmente se buscan los divisores de 6 y 12.
#9. Conceptos aplicados: Clases, objetos, métodos, listas, tuplas, diccionarios, for, if, else, *args, operador módulo %, append(), tuple(), acumuladores, return y reutilización de métodos.

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma = suma + divisor
        if suma == numero:
            return True
        else:
            return False
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

# --- Programa principal ---
df = DivisorFinder()
print(f"Divisores de 12: {df.encontrar_divisores(12)}")
print(f"¿6 es perfecto?: {df.es_perfecto(6)}")
print(f"¿12 es perfecto?: {df.es_perfecto(12)}")
print(f"Divisores múltiples: {df.encontrar_multiples_divisores(6, 12)}")
print("-" * 50)

#Prueba de escritorio
#Paso	i	12 % i	¿Es divisor?	Acción	Lista de divisores
#1	    1	   0	     Sí	      Se agrega	       [1]
#2	    2	   0	     Sí	      Se agrega	      [1, 2]
#3	    3	   0	     Sí	      Se agrega	     [1, 2, 3]
#4	    4	   0	     Sí	      Se agrega	    [1, 2, 3, 4]
#5	    5	   2	     No	      Se descarta	[1, 2, 3, 4]
#6	    6	   0	     Sí	      Se agrega	    [1, 2, 3, 4, 6]
#7	    7	   5	     No	      Se descarta	[1, 2, 3, 4, 6]
#8	    8	   4	     No	      Se descarta	[1, 2, 3, 4, 6]
#9	    9	   3	     No	      Se descarta	[1, 2, 3, 4, 6]
#10	   10	   2	     No	      Se descarta	[1, 2, 3, 4, 6]
#11	   11	   1	     No	      Se descarta	[1, 2, 3, 4, 6]
#12	   12	   0	     Sí	      Se agrega	    [1, 2, 3, 4, 6, 12]

#________________________________________________________________________________

#EJERCICIO 16 — Codificador/Decodificador (Cifrado César)
#Clase: CodificadorCesar
#Nivel: Medio

#Entrada
#Letra o palabra, y un desplazamiento (1-25).
#Proceso
#Convertir la letra a su código ASCII, desplazarla con el operador % (para que el alfabeto "dé la vuelta" al llegar a la z), y volver a
#convertir a letra.
#Repetir letra por letra para codificar una palabra completa.
#Guardar cada codificación en un historial.
#Salida
#Palabra codificada.

#Bosquejo
#codificar_letra('h', 3):
#posición de 'h' en el alfabeto (a=0): 7
#(7 + 3) % 26 = 10 -> letra en posición 10 = 'k'
#codificar_palabra("hola", 3):
#h(7) -> k(10)
#o(14) -> r(17)
#l(11) -> o(14)
#a(0)  -> d(3)
#Resultado: "krod"

#Descubrir el patrón
#1. Constructor __init__: Inicializa el atributo historial como un diccionario vacío.
#Este diccionario sirve para guardar las palabras que se han codificado junto con su resultado.
#Por ejemplo: {"hola": "krod"}.
#2. Método codificar_letra(letra, desplazamiento): Sirve para codificar una sola letra utilizando el desplazamiento indicado.
#Primero crea la variable alfabeto con las 26 letras.
#Luego utiliza .lower() para convertir la letra a minúscula y .index() para encontrar su posición dentro del alfabeto.
#Después calcula nueva_posicion sumando el desplazamiento a la posición original.
#Finalmente utiliza % len(alfabeto) para regresar al inicio del alfabeto cuando se llega a la letra z y retorna la nueva letra.
#3. Variable posicion: Guarda la posición de la letra dentro del alfabeto.
#Por ejemplo, la letra "a" está en la posición 0, "b" en la posición 1, "c" en la posición 2, etc.
#4. Variable nueva_posicion: Guarda la nueva posición de la letra después de aplicar el desplazamiento.
#Se calcula con (posicion + desplazamiento) % len(alfabeto).
#El operador % permite que el desplazamiento vuelva al comienzo del alfabeto cuando es necesario.
#5. Método codificar_palabra(palabra, desplazamiento): Sirve para codificar una palabra completa.
#Primero crea una cadena vacía llamada resultado.
#Luego recorre cada letra de la palabra con un for.
#Para cada letra llama al método codificar_letra() y agrega la letra codificada al resultado.
#Finalmente guarda la palabra original y su resultado en historial y retorna la palabra codificada.
#6. Variable resultado: Es una cadena que comienza vacía "".
#En cada vuelta del for se le agrega la letra codificada correspondiente hasta formar toda la palabra.
#7. Atributo historial: Es un diccionario que almacena las palabras codificadas.
#La palabra original queda como clave y la palabra codificada queda como valor.
#8. Programa principal: Se crea el objeto cc.
#Primero se prueba la codificación de una sola letra, "a" con desplazamiento 3.
#Después se codifica la palabra "hola" con desplazamiento 3.
#Finalmente se muestra el historial de codificaciones.
#9. Conceptos aplicados: Clases, objetos, constructor __init__, diccionarios, cadenas de texto, for, .lower(), .index(), len(), operador %, return, concatenación con +, reutilización de métodos y f-strings.

class CodificadorCesar:
    def __init__(self):
        self.historial = {}
    def codificar_letra(self, letra, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        posicion = alfabeto.index(letra.lower())
        nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
        return alfabeto[nueva_posicion]
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado

# --- Programa principal ---
cc = CodificadorCesar()
print(f"Letra codificada: {cc.codificar_letra('a', 3)}")
print(f"Palabra codificada: {cc.codificar_palabra('hola', 3)}")
print(f"Historial de codificaciones: {cc.historial}")
print("-" * 50)

#Prueba de escritorio
#Paso	Letra	Posición	+3	Nueva letra	Resultado
#1	      h     	7	   10	k	           "k"
#2	      o	       14	   17	r	           "kr"
#3	      l	       11	   14	o	           "kro"
#4	      a	       0	   3	d	           "krod"

#______________________________________________________________________________________

#EJERCICIO 17 — Grupo de edades
#Clase: AgrupadorEdades
#Nivel: Básico

#Entrada
#Edades en lote (*edades).
#Proceso
#Clasificar cada edad en una categoría: "niño", "adolescente", "adulto"
# o "mayor", usando condicionales if/elif.
#Agrupar todas las edades recibidas en un diccionario {categoria: [edades]}.
#Calcular el promedio de edades de una categoría específica.
#Salida
#Diccionario agrupado por categoría.
#Promedio de edades de una categoría.

#Bosquejo
#Entrada: 5, 15, 30, 70
#5  -> niño (< 13)
#15 -> adolescente (13 <= edad < 18)
#30 -> adulto (18 <= edad < 65)
#70 -> mayor (>= 65)
#Resultado: {'niño':[5], 'adolescente': [15], 'adulto':[30], 'mayor':[70]}
#edad_promedio_categoria('niño') = 5 / 1 = 5

#Descubrir el patrón
#1. __init__
#Es el constructor de la clase. Crea self.ultimo_grupo como un diccionario vacío {} para guardar el último agrupamiento realizado.
#2. clasificar_edad(self, edad)
#Recibe una edad y determina a qué categoría pertenece:
#Menor de 13 → "niño"
#Menor de 18 → "adolescente"
#Menor de 65 → "adulto"
#65 o más → "mayor"
#3. Condiciones if, elif, else
#Permiten revisar la edad de arriba hacia abajo hasta encontrar la categoría correspondiente.
#4. agrupar_por_categoria(self, *edades)
#Recibe varias edades gracias a *edades.
##Primero crea el diccionario grupos con las cuatro categorías y listas vacías.
#5. for edad in edades
#Recorre una por una las edades recibidas.
#6. categoria = self.clasificar_edad(edad)
#Llama al método anterior para saber dónde colocar cada edad.
#7. grupos[categoria].append(edad)
#Agrega la edad a la lista de su categoría.
#8. self.ultimo_grupo = grupos
#Guarda los grupos obtenidos dentro del objeto para poder utilizarlos después.
#9. edad_promedio_categoria(self, categoria)
#Busca las edades que pertenecen a una categoría y calcula su promedio.
#10. self.ultimo_grupo.get(categoria, [])
#Busca la categoría en el diccionario. Si no existe, devuelve una lista vacía [].
#11. if not lista:
#Comprueba si la lista está vacía. Si no hay edades, devuelve 0.
#12. sum(lista) / len(lista)
#sum() suma las edades y len() cuenta cuántas hay. Al dividir obtenemos el promedio.

class AgrupadorEdades:
    def __init__(self):
        self.ultimo_grupo = {}
    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        grupos = {"niño": [],"adolescente": [], "adulto": [], "mayor":[]}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            grupos[categoria].append(edad)
        self.ultimo_grupo = grupos
        return grupos
    def edad_promedio_categoria(self, categoria):
        lista = self.ultimo_grupo.get(categoria, [])
        if not lista:
            return 0
        return sum(lista) / len(lista)
    
# --- Programa principal ---
ae = AgrupadorEdades()
grupos = ae.agrupar_por_categoria(5, 15,
30, 70)
print(f"Grupos: {grupos}")
print(f"Promedio categoría niño: {ae.edad_promedio_categoria("niño")}")
print("-" * 50)

#Prueba de escritorio
#Paso Edad	Condición	                               Categoría	Grupos después de agregar
#1     	5  	5 < 13 → Sí	                                 niño	{"niño": [5], "adolescente": [], "adulto": [], "mayor": []}
#2	    15	15 < 13 → No; 15 < 18 → Sí            	adolescente	{"niño": [5], "adolescente": [15], "adulto": [], "mayor": []}
#3	    30	30 < 13 → No; 30 < 18 → No; 30 < 65 → Sí	adulto	{"niño": [5], "adolescente": [15], "adulto": [30], "mayor": []}
#4	    70	No cumple las anteriores	                 mayor	{"niño": [5], "adolescente": [15], "adulto": [30], "mayor": [70]}

#__________________________________________________________________________________________

#EJERCICIO 18 — Matriz de distancias
#Clase: CalculadorDistancia
#Nivel: Medio

#Entrada
#Tuplas (x, y) como puntos en el plano.
#Proceso
#Calcular la distancia euclidiana entre dos puntos con la fórmula 
#sqrt((x2-x1)^2 + (y2-y1)^2).
#Comparar la distancia de un punto de referencia contra varios puntos para encontrar el más cercano.
#Guardar todas las distancias calculadas.
#Salida
#Distancia numérica.
#Punto más cercano a la referencia.

#Bosquejo
#distancia_euclidiana((0,0), (3,4)):
#dx = 3-0 = 3 ; dy = 4-0 = 4
#sqrt(3^2 + 4^2) = sqrt(9+16) = sqrt(25) = 5.0
#punto_mas_cercano((0,0), (3,4), (1,1)):
#distancia a (3,4) = 5.0
#distancia a (1,1) = sqrt(1^2+1^2) = sqrt(2) ≈ 1.41
#el más cercano es (1,1)

#Descubrir el patrón
#1. __init__
#Es el constructor. Crea self.distancias como una lista vacía para guardar todas las distancias que se calculen.
#distancia_euclidiana(self, p1, p2)
#2. Calcula la distancia entre dos puntos. Cada punto se representa como una tupla, por ejemplo (0, 0) o (3, 4).
#3. p1 y p2
#Representan los dos puntos:
#p1 → primer punto.
#p2 → segundo punto.
#4. dx = p2[0] - p1[0]
#Calcula la diferencia entre las coordenadas X de los dos puntos.
#5. dy = p2[1] - p1[1]
#Calcula la diferencia entre las coordenadas Y de los dos puntos.
#6. distancia = (dx ** 2 + dy ** 2) ** 0.5
#Calcula la distancia euclidiana usando las diferencias dx y dy.
#7. self.distancias.append(distancia)
#Guarda la distancia calculada dentro de la lista distancias.
#8. return distancia
#Devuelve la distancia calculada.
#9. punto_mas_cercano(self, referencia, *puntos)
#Recibe un punto de referencia y varios puntos para comparar cuál está más cerca.
#10. mas_cercano = None
#Al inicio todavía no conocemos cuál es el punto más cercano.
#11. menor_distancia = None
#Al inicio tampoco tenemos una distancia mínima.
#12. for punto in puntos
#Recorre todos los puntos que fueron enviados.
#13. distancia = self.distancia_euclidiana(referencia, punto)
#Calcula la distancia entre el punto de referencia y el punto actual.
#14. if menor_distancia is None or distancia < menor_distancia
#Comprueba dos cosas:
#Si todavía no existe una distancia mínima.
#O si la nueva distancia es menor que la que teníamos.
#15. menor_distancia = distancia
#Guarda la nueva distancia como la menor encontrada.
#16. mas_cercano = punto
#Guarda el punto que tiene esa menor distancia.
#17. return mas_cercano
#Al terminar el recorrido, devuelve el punto más cercano.

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        mas_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mas_cercano = punto
        return mas_cercano

# --- Programa principal ---
cd = CalculadorDistancia()
print(f"Distancia (0,0)-(3,4): {cd.distancia_euclidiana((0, 0), (3, 4))}")
print(f"Punto más cercano a (0,0): {cd.punto_mas_cercano((0, 0), (3, 4), (1, 1))}")
print(f"Todas las distancias calculadas: {cd.distancias}")
print("-" * 50)

#Prueba de escritorio
#Paso	Variable	Operación	Resultado
#1      	p1	     (0, 0)       (0, 0)
#2	        p2	     (3, 4)	      (3, 4)
#3	        dx	      3 - 0	         3
#4	        dy	      4 - 0	         4
#5	    distancia	(3² + 4²) ** 0.5 5.0
#6	   distancias	Se agrega 5.0	[5.0]

#_____________________________________________________________________________________

#EJERCICIO 19 — Inventario de productos
#Clase: Inventario
#Nivel: Básico

#Entrada
#Productos y cantidades.
#Proceso
#Guardar o aumentar el stock de un producto en un diccionario.
#Disminuir el stock si hay suficiente cantidad disponible.
#Filtrar los productos cuyo stock está por debajo de un mínimo.
#Salida
#True/False al restar stock (según si había suficiente).
#Lista de productos con stock bajo.

#Bosquejo
#agregar_stock("pan", 50)    -> {"pan": 50}
#agregar_stock("leche", 10)  -> {"pan": 50, "leche": 10}
#restar_stock("pan", 30): 50 >= 30 (sí) -> pan queda en 20, retorna True
#productos_bajo_stock(15): pan=20 (no < 15) ; leche=10 (sí < 15)
#-> ["leche"]

#Descubrir el patrón
#1. __init__
#Es el constructor de la clase. Crea self.stock como un diccionario vacío {} para guardar los productos y sus cantidades.
#2. agregar_stock(self, producto, cantidad)
#Sirve para agregar productos al inventario.
#3. if producto in self.stock
#Comprueba si el producto ya existe en el diccionario.
#4. Si el producto ya existe:
#self.stock[producto] = self.stock[producto] + cantidad
#5. Suma la nueva cantidad a la cantidad que ya tenía.
#else
#Si el producto todavía no existe, lo agrega directamente:
#self.stock[producto] = cantidad
#6. restar_stock(self, producto, cantidad)
#Sirve para retirar una cantidad de un producto del inventario.
# if producto in self.stock and self.stock[producto] >= cantidad
# Comprueba dos condiciones:
# Que el producto exista.
# Que haya suficiente stock para realizar la resta.
#8. self.stock[producto] = self.stock[producto] - cantidad
# Resta la cantidad solicitada del stock existente.
#9. return True
#Indica que la operación se realizó correctamente.
#10. return False
#Si el producto no existe o no hay suficiente stock, devuelve False.
#11. productos_bajo_stock(self, minimo)
#Busca qué productos tienen una cantidad menor al mínimo indicado.
#12. resultado = []
#Crea una lista vacía donde se guardarán los productos con poco stock.
#13. for producto, cantidad in self.stock.items()
#Recorre el diccionario obteniendo el nombre del producto y su cantidad.
#14. if cantidad < minimo
#Comprueba si la cantidad está por debajo del límite.
#15. resultado.append(producto)
#Si está por debajo del mínimo, agrega el nombre del producto a la lista.
#16. Programa principal
#Crea el objeto inv, agrega "pan" y "leche", resta 30 unidades de pan y finalmente muestra el resultado.

class Inventario:
    def __init__(self):
        self.stock = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] = self.stock[producto] + cantidad
        else:
            self.stock[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] = self.stock[producto] - cantidad
            return True
        else:
            return False
    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado
    
# --- Programa principal ---
inv = Inventario()
inv.agregar_stock("pan", 50)
inv.agregar_stock("leche", 10)
exito = inv.restar_stock("pan", 30)
print(f"¿Se pudo restar stock de pan?: {exito}")
print(f"Stock actual: {inv.stock}")
print(f"Productos con stock bajo 15: {inv.productos_bajo_stock(15)}")
print("-" * 50)

#Prueba de escritorio

#Paso	Producto	Cantidad	¿Ya existe?	   Acción	           Stock
#1	       pan	      50	         No  	Se agrega con 50	{"pan": 50}
#2        leche       10             No     Se agrega con 10    {"pan": 50, "leche": 10}

#__________________________________________________________________________

#EJERCICIO 20 — Analizador de patrones en textos
#Clase: AnalizadorPatrones
#Nivel: Avanzado

#Entrada
#Texto y un patrón de búsqueda.
#Proceso
#Separar el texto en palabras con split().
#Filtrar las palabras que empiezan con el patrón.
#Agrupar las palabras según su longitud en un diccionario.
#Obtener el conjunto de palabras únicas del último texto analizado.
#Salida
#Lista de palabras que coinciden con el patrón.
#Diccionario {longitud: [palabras]}.
#Conjunto de palabras únicas.

#Bosquejo

#Descubrir el patrón 
#1. __init__
#Es el constructor de la clase. Crea self.palabras como una lista vacía [], donde posteriormente se pueden guardar palabras.
#2. encontrar_palabras(self, texto, patron)
#Busca dentro de un texto las palabras que comienzan con un patrón determinado.
#3. resultado = []
#Crea una lista vacía donde se guardarán las palabras encontradas.
#4. palabras = texto.split()
#Divide el texto en palabras individuales.
#Por ejemplo:
#"el gato está aquí"
#se convierte en:
#["el", "gato", "está", "aquí"]
#5. for palabra in palabras
#Recorre cada palabra de la lista.
#6. palabra.lower()
#Convierte la palabra a minúsculas para que la comparación no dependa de mayúsculas o minúsculas.
#8. .startswith(patron.lower())
#Comprueba si la palabra comienza con el patrón indicado.
#9. En este caso:
#"aquí".startswith("a")
#da True.
#10. resultado.append(palabra)
#Si la palabra cumple la condición, se agrega a la lista resultado.
#11. agrupar_por_longitud(self, texto)
#Agrupa las palabras según la cantidad de letras que tienen.
#12. resultado = {}
#Crea un diccionario vacío. Las claves serán las longitudes y los valores serán listas de palabras.
#13. longitud = len(palabra)
#Obtiene la cantidad de caracteres de cada palabra.
#14. if longitud not in resultado
#Comprueba si esa longitud todavía no existe como clave en el diccionario.
#15. resultado[longitud] = []
#Si no existe, crea una lista vacía para esa longitud.
#16. resultado[longitud].append(palabra)
#Agrega la palabra a la lista correspondiente.
#17. palabras_unicas(self)
#Devuelve las palabras almacenadas en self.palabras como un conjunto (set).
#18. return set(self.palabras)
#Convierte la lista en un conjunto. Los conjuntos no permiten elementos repetidos.
#19. Programa principal
#ap = AnalizadorPatrones()
#Crea un objeto de la clase.
#ap.palabras = "el gato está aquí".split()
#Guarda las palabras del texto directamente en ap.palabras.

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []
    def encontrar_palabras(self, texto, patron):
        resultado = []
        palabras = texto.split()
        for palabra in palabras:
            if palabra.lower().startswith(patron.lower()):
                resultado.append(palabra)
        return resultado
    def agrupar_por_longitud(self, texto):
        resultado = {}
        palabras = texto.split()
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado
    def palabras_unicas(self):
        return set(self.palabras)

# --- Programa principal ---
ap = AnalizadorPatrones()
ap.palabras = "el gato está aquí".split()
print("Palabras que empiezan con 'a':", ap.encontrar_palabras("el gato está aquí", "a"))
print("Agrupadas por longitud:", ap.agrupar_por_longitud("el gato está aquí"))
print("Palabras únicas:", ap.palabras_unicas())
print("-" * 50)

#Prueba de escritorio


