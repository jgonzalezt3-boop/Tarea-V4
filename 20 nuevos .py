#Como lo hice
#Utilice 4 metodos agregar color, agregar varios, buscar color y cantidad de colores
#Para varios utilice esto *args
#Len para recorrer y saber cuantos colores tenía

class GestorColores:
    def __init__(self):
        self.colores = []
    def agregar_color(self, colores):
        if colores not in self.colores:
            self.colores.append(colores)
    def agregar_varios(self, *colores):
        for color in colores:
            self.agregar_color(color)
        return self.colores
    def buscar_colores(self, color):
        if color in self.colores:
            return True
        else:
            return False
    def cantidad_colores(self):
        return len(self.colores)

c = GestorColores()
c.agregar_color("Azul")
c.agregar_color("Gris")
c.agregar_color("Amarillo")
c.agregar_color("Verde")
buscar = c.buscar_colores("Azul")
cantidad = c.cantidad_colores()
print(f"¿El color existe?: {buscar}")
print(f"Cantidad de colores: {cantidad}")
print("-" * 50)
#________________________________________________________

#Como lo hice
#Utilice 5 metodos para saber de los número positivos, agregar número, agregar varios números, cantidad de números y el promedio.
#Para varios utilice esto *args
#Len para recorrer y saber cantidad de números
#Para el promedio sumamos todo los números de la lista y dividimos para el total de números recorriendo la lista con len.
class GestorNumerosPositivos:
    def __init__(self):
        self.numeros = []
    def es_positivo(self, numero):
        if numero > 0:
            return True
        else:
            return False
    def agregar_numero(self, numero):
        if self.es_positivo(numero):
            self.numeros.append(numero)
    def agregar_varios(self, *numeros):
        for numero in numeros:
            self.agregar_numero(numero)
    def cantidad_numeros(self):
        return len(self.numeros)
    def promedio(self):
        if len(self.numeros) > 0:
            return sum(self.numeros) / len(self.numeros)
        else:
            return 0

n = GestorNumerosPositivos()
n.agregar_varios(33, -5, 16, 0, -8)
print(f"Números positivos: {n.numeros}")
print(f"Cantidad: {n.cantidad_numeros()}")
print(f"Promedio: {n.promedio():.2f}")
print("-" * 50)
#____________________________________________________________________

#Como lo hice
#Utilice 5 metodos registrar altura, registrar varias, alturas mayores de 1.60, altura maxima y promedio
#Para varios utilice esto *args
#max para saber el maximo y len nos ayudo a sacar el promedio de las alturas con sum
#append nos ayudar agregar datos
class ControlAlturas:
    def __init__(self):
        self.alturas = []
    def registrar_altura(self, altura):
        self.alturas.append(altura)
    def registrar_varias(self, *alturas):
        for altura in alturas:
            self.registrar_altura(altura)
    def alturas_mayores(self):
        resultado = []
        for altura in self.alturas:
            if altura > 1.60:
                resultado.append(altura)
        return resultado
    def altura_maxima(self):
        return max(self.alturas)
    def promedio(self):
        return sum(self.alturas) / len(self.alturas)

a = ControlAlturas()
a.registrar_varias(1.52, 1.70, 1.59, 1.80, 1.68)
print(f"Alturas: {a.alturas}")
print(f"Mayores a 1.60: {a.alturas_mayores()}")
print(f"Altura máxima: {a.altura_maxima()}")
print(f"Promedio: {a.promedio():.2f}")
print("-" * 50)
#___________________________________________________________________

#Como lo hice
#Utilice 5 metodos agregar distancia, agregar varias, total, promedio y la distancia mayor
#Para varios utilice esto *args
#max para saber el maximo y len nos ayudo a sacar el promedio de las distancias con sum
#append nos ayudar agregar datos
class GestorDistancias:
    def __init__(self):
        self.distancias = []
    def agregar_distancia(self, distancia):
        self.distancias.append(distancia)
    def agregar_varias(self, *distancias):
        for distancia in distancias:
            self.agregar_distancia(distancia)
    def total(self):
        return sum(self.distancias)
    def promedio(self):
        return sum(self.distancias) / len(self.distancias)
    def distancia_mayor(self):
        return max(self.distancias)

d = GestorDistancias()
d.agregar_varias(25, 20, 13, 30, 48)
print(f"Distancias: {d.distancias}")
print(f"Distancia total: {d.total()}")
print(f"Promedio: {d.promedio():.2f}")
print(f"Mayor distancia: {d.distancia_mayor()}")
print("-" * 50)
#_______________________________________________________________________

#Como lo hice
#En este ejerciccio tenemos clave y valor, nombre la clave y especie el valor
#Utilice 4 metodos registrar, buscar por especie, cantidad mascotass, mostrar mascotas
#Len para recorrer y saber cuantas mascotas tengo
#append nos ayudar agregar datos
class RegistroMascotas:
    def __init__(self):
        self.mascotas = {}
    def registrar(self, nombre, especie):
        self.mascotas[nombre] = especie
    def buscar_por_especie(self, especie):
        resultado = []
        for nombre in self.mascotas:
            if self.mascotas[nombre].lower() == especie.lower():
                resultado.append(nombre)
        return resultado
    def cantidad_mascotas(self):
        return len(self.mascotas)
    def mostrar_mascotas(self):
        return self.mascotas

m = RegistroMascotas()
m.registrar("Kiara", "Perro")
m.registrar("Jack", "Gato")
m.registrar("Tika", "Perro")
print(f"Mascotas: {m.mostrar_mascotas()}")
print(f"Perros: {m.buscar_por_especie('Perro')}")
print(f"Cantidad: {m.cantidad_mascotas()}")
print("-" * 50)
#_______________________________________________________________________

#Como lo hice
#Utilice 5 agregar precio, agregar varios, precios mayores de 50, precio mayor y promedio
#para el promedio usamos sum y len
#para el maximo usamos max
#append nos ayudar agregar datos
#Para varios utilice esto *args
class GestorDescuentos:
    def __init__(self):
        self.precios = []
    def agregar_precio(self, precio):
        self.precios.append(precio)
    def agregar_varios(self, *precios):
        for precio in precios:
            self.agregar_precio(precio)
    def precios_mayores_50(self):
        resultado = []
        for precio in self.precios:
            if precio > 50:
                resultado.append(precio)
        return resultado
    def precio_mayor(self):
        return max(self.precios)
    def promedio(self):
        return sum(self.precios) / len(self.precios)

p = GestorDescuentos()
p.agregar_varios(35, 80, 100, 24, 12)
print(f"Precios: {p.precios}")
print(f"Mayores a $50: {p.precios_mayores_50()}")
print(f"Precio mayor: {p.precio_mayor()}")
print(f"Promedio: {p.promedio():.2f}")
print("-" * 50)
#____________________________________________________________

#Como lo hice
#Utilice 5 ocupar, liberar, asientos disponibles, asiento ocupados y cantidad disponibles
#para saber la cantidad disponibles usamos len
#append nos ayudar agregar datos

class ControlAsientos:
    def __init__(self):
        self.asientos = {}
    def ocupar(self, asiento):
        self.asientos[asiento] = "Ocupado"
    def liberar(self, asiento):
        self.asientos[asiento] = "Disponible"
    def asientos_disponibles(self):
        resultado = []
        for asiento in self.asientos:
            if self.asientos[asiento] == "Disponible":
                resultado.append(asiento)
        return resultado
    def asientos_ocupados(self):
        resultado = []
        for asiento in self.asientos:
            if self.asientos[asiento] == "Ocupado":
                resultado.append(asiento)
        return resultado
    def cantidad_disponibles(self):
        return len(self.asientos_disponibles())

c = ControlAsientos()
c.asientos[6] = "Disponible"
c.asientos[15] = "Disponible"
c.asientos[3] = "Disponible"
c.ocupar(15)
print(f"Asientos disponibles: {c.asientos_disponibles()}")
print(f"Asientos ocupados: {c.asientos_ocupados()}")
print(f"Cantidad disponibles: {c.cantidad_disponibles()}")
print("-" * 50)
#____________________________________________________________________________

#Como lo hice
#Utilice 4 analizar, palabra mayor, palabra menor y cantidad de palabras
#para saber la cantidad palabras usamos len
#usamos .split para separar el texto ingresado en palabras
#en return mayor siempre se guardará la palabra más larga
#if len(palabra) > len(mayor) Esta es la parte que compara el tamaño de las palabras y len() sirve para saber cuántos caracteres tiene una palabra.

class AnalizadorPalabras:
    def __init__(self):
        self.palabras = []
    def analizar(self, texto):
        self.palabras = texto.split()
    def palabra_mayor(self):
        mayor = self.palabras[0]
        for palabra in self.palabras:
            if len(palabra) > len(mayor):
                mayor = palabra
        return mayor
    def palabra_menor(self):
        menor = self.palabras[0]
        for palabra in self.palabras:
            if len(palabra) < len(menor):
                menor = palabra
        return menor
    def cantidad_palabras(self):
        return len(self.palabras)

a = AnalizadorPalabras()
a.analizar("Soy una costeña que ama la Sierra")
print(f"Palabras: {a.palabras}")
print(f"Palabra más larga: {a.palabra_mayor()}")
print(f"Palabra más corta: {a.palabra_menor()}")
print(f"Cantidad: {a.cantidad_palabras()}")
print("-" * 50)
#_____________________________________________________________________

#Como lo hice
#Utilice 5 registrar consumo, registrar varios, total consumido, promedio y mayor consumo
#para el promedio usamos sum y len
#para el maximo usamos max
#append nos ayudar agregar datos
#Para varios utilice esto *args
class GestorCombustible:
    def __init__(self):
        self.consumos = []
    def registrar_consumo(self, cantidad):
        self.consumos.append(cantidad)
    def registrar_varios(self, *cantidades):
        for cantidad in cantidades:
            self.registrar_consumo(cantidad)
    def total_consumido(self):
        return sum(self.consumos)
    def promedio(self):
        return sum(self.consumos) / len(self.consumos)
    def mayor_consumo(self):
        return max(self.consumos)

c = GestorCombustible()
c.registrar_varios(20, 10, 5, 30, 8)
print(f"Consumos: {c.consumos}")
print(f"Total: {c.total_consumido()}")
print(f"Promedio: {c.promedio():.2f}")
print(f"Mayor consumo: {c.mayor_consumo()}")
print("-" * 50)
#________________________________________________________________________

#Como lo hice
#Utilice 4 registrar deportista, mayores de edad, edad mayor y promedio de edades
#para el promedio usamos sum y len
#para edad mayor usamos max
#en registrar deportista aplicamos lo de clave valor, donde la clave es nombre y el valor edad
class GestorDeportes:
    def __init__(self):
        self.deportistas = {}
    def registrar_deportista(self, nombre, edad):
        self.deportistas[nombre] = edad
    def mayores_de_edad(self):
        resultado = []
        for nombre in self.deportistas:
            if self.deportistas[nombre] >= 18:
                resultado.append(nombre)
        return resultado
    def edad_mayor(self):
        return max(self.deportistas.values())
    def promedio_edades(self):
        return sum(self.deportistas.values()) / len(self.deportistas)

d = GestorDeportes()
d.registrar_deportista("Alex", 25)
d.registrar_deportista("Aaron", 10)
d.registrar_deportista("Jenn", 25)
print(f"Mayores de edad: {d.mayores_de_edad()}")
print(f"Edad mayor: {d.edad_mayor()}")
print(f"Promedio: {d.promedio_edades():.2f}")
print("-" * 50)
#________________________________________________________________________________

#Como lo hice
#Utilice 4 registrar peso, registrar varios, pesos mayores, peso mayor
#para el peso mayor usamos max
#append nos ayudar agregar datos
#Para varios utilice esto *args
class ControlPesos:
    def __init__(self):
        self.pesos = []
    def registrar_peso(self, peso):
        self.pesos.append(peso)
    def registrar_varios(self, *pesos):
        for peso in pesos:
            self.registrar_peso(peso)
    def pesos_mayores_70(self):
        resultado = []
        for peso in self.pesos:
            if peso > 70:
                resultado.append(peso)
        return resultado
    def peso_mayor(self):
        return max(self.pesos)

cp = ControlPesos()
cp.registrar_varios(12.5, 70, 8, 80, 90, 24.6)
print(f"Los pesos mayores a 70 son: {cp.pesos_mayores_70()}")
print(f"El peso mayor es: {cp.peso_mayor()}")
print("-" * 50)
#_________________________________________________________________________

#Como lo hice
#Utilice 4 agregar fruta, agregar varias, buscar fruta, cantidad de frutas
#en buscar fruta usamos el if y else, junto al retorno False o True
#para saber la cantidad de frutas que había usamos len
#append nos ayudar agregar datos
#Para varios utilice esto *args
#not in evita que la fruta se repita
class GestorFrutas:
    def __init__(self):
        self.frutas = []
    def agregar_fruta(self, fruta):
        if fruta not in self.frutas:
            self.frutas.append(fruta)
    def agregar_varias(self, *frutas):
        for fruta in frutas:
            self.agregar_fruta(fruta)
    def buscar_fruta(self, fruta):
        if fruta in self.frutas:
            return True
        else:
            return False
    def cantidad_frutas(self):
        return len(self.frutas)

g = GestorFrutas()
g.agregar_varias("Frutilla", "Durazno", "Frutilla" "Mango", "Manzana", "Cereza")
print(f"Frutas: {g.frutas}")
print(f"¿Existe Mango?: {g.buscar_fruta('Mango')}")
print(f"Cantidad de frutas: {g.cantidad_frutas()}")
print("-" * 50)
#_____________________________________________________________________

#Como lo hice
#Utilice 5 agregar precio, agregar varios, precios mayores de 50, precio mayor y promedio
#para el promedio usamos sum y len
#para el maximo usamos max
#append nos ayudar agregar datos
#Para varios utilice esto *args
class ControlHoras:
    def __init__(self):
        self.horas = []
    def registrar_horas(self, hora):
        self.horas.append(hora)
    def registrar_varias(self, *horas):
        for hora in horas:
            self.registrar_horas(hora)
    def total_horas(self):
        return sum(self.horas)
    def promedio_horas(self):
        return sum(self.horas) / len(self.horas)
    def mayor_cantidad_horas(self):
        return max(self.horas)

c = ControlHoras()
c.registrar_varias(8, 7, 9, 6, 8)
print(f"Horas registradas: {c.horas}")
print(f"Total de horas: {c.total_horas()}")
print(f"Promedio de horas: {c.promedio_horas():.2f}")
print(f"Mayor cantidad de horas: {c.mayor_cantidad_horas()}")
print("-" * 50)
#___________________________________________________________________

#Como lo hice
#Utilice 4 agregar celular, celulares mayores de 300, celular más caro y el precio promedio
#para el promedio usamos sum y len
#para el verificar el celular más caro usamos max
#append nos ayudar agregar datos
#en registrar celular aplicamos lo de clave valor, donde la clave es marca y el valor precio
class GestorCelulares:
    def __init__(self):
        self.celulares = {}
    def agregar_celular(self, marca, precio):
        self.celulares[marca] = precio
    def celulares_mayores_300(self):
        resultado = []
        for marca in self.celulares:
            if self.celulares[marca] > 300:
                resultado.append(marca)
        return resultado
    def celular_mas_caro(self):
        return max(self.celulares.values())
    def precio_promedio(self):
        return sum(self.celulares.values()) / len(self.celulares)

g = GestorCelulares()
g.agregar_celular("Samsung", 500)
g.agregar_celular("Infinix", 250)
g.agregar_celular("Apple", 900)
g.agregar_celular("LG", 300)
print(f"Celulares mayores a $300: {g.celulares_mayores_300()}")
print(f"Precio más alto: ${g.celular_mas_caro()}")
print(f"Precio promedio: ${g.precio_promedio():.2f}")
print("-" * 50)

#_________________________________________________________________________

#Como lo hice
#Utilice 4 registrar estudiantes, buscar por curso, cantidad estudiantes y mostrar estudiantes
#para len para saber la cantidad de estudiantes
#para la cantidad de estudiantes usamos max
#append nos ayudar agregar datos
class GestorCursos:
    def __init__(self):
        self.estudiantes = {}
    def registrar_estudiante(self, nombre, curso):
        self.estudiantes[nombre] = curso
    def buscar_por_curso(self, curso):
        resultado = []
        for nombre in self.estudiantes:
            if self.estudiantes[nombre] == curso:
                resultado.append(nombre)
        return resultado
    def cantidad_estudiantes(self):
        return len(self.estudiantes)
    def mostrar_estudiantes(self):
        return self.estudiantes

g = GestorCursos()
g.registrar_estudiante("Miguel", "Inglés")
g.registrar_estudiante("Luis", "Natación")
g.registrar_estudiante("Annelise", "Basquet")
print(f"Estudiantes de Basquet: {g.buscar_por_curso('Basquet')}")
print(f"Cantidad de estudiantes: {g.cantidad_estudiantes()}")
print(f"Estudiantes registrados: {g.mostrar_estudiantes()}")
print("-" * 50)

#____________________________________________________________________

#Como lo hice
#Utilice 5 agregar producto, aumentar stock, disminuir stock, buscar producto y productos stock bajo
#en agregar producto aplicamos lo de clave valor, donde la clave es producto y el valor stock
#append nos ayudar agregar datos
#en buscar producto usamos el if y else, junto al retorno False o True
class ControlInventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, producto, stock):
        self.productos[producto] = stock
    def aumentar_stock(self, producto, cantidad):
        self.productos[producto] += cantidad
    def disminuir_stock(self, producto, cantidad):
        self.productos[producto] -= cantidad
    def buscar_producto(self, producto):
        if producto in self.productos:
            return True
        else:
            return False
    def productos_stock_bajo(self):
        resultado = []
        for producto in self.productos:
            if self.productos[producto] < 5:
                resultado.append(producto)
        return resultado

i = ControlInventario()
i.agregar_producto("Huevo", 35)
i.agregar_producto("Azucar", 3)
i.agregar_producto("Sal", 9)
i.aumentar_stock("Sal", 5)
i.disminuir_stock("Huevo", 4)
print(f"Inventario: {i.productos}")
print(f"¿Existe Aceite?: {i.buscar_producto('Aceite')}")
print(f"Productos con stock bajo: {i.productos_stock_bajo()}")
print("-" * 50)

#___________________________________________________________________

#Como lo hice
#Utilice 3 analizar, cantidad de palabras y palabra más larga
#para ver la palabra más larga usamos max
#usamos .split para separar el texto ingresado en palabras
class AnalizadorPalabras:
    def __init__(self):
        self.palabras = []
    def analizar(self, texto):
        self.palabras = texto.split()
    def cantidad_palabras(self):
        return len(self.palabras)
    def palabra_mas_larga(self):
        return max(self.palabras, key=len)

a = AnalizadorPalabras()
a.analizar("Todo lo que hace Dios es bueno, todo lo que Dios permite es necesario")
print(f"Palabras: {a.palabras}")
print(f"Cantidad de palabras: {a.cantidad_palabras()}")
print(f"Palabra más larga: {a.palabra_mas_larga()}")
print("-" * 50)

#__________________________________________________________________

#Como lo hice
#Utilice 6 registar pais, buscar capital, modificaar capital, eliminar pais, mostrar paises y cantidad de paises
#para eliminar la peliculas usamos .pop
#para mostrar la cantidad de paises usamos len
#append nos ayudar agregar datos
#en buscar capital usamos if y else
#en registrar pais aplicamos lo de clave valor, donde la clave es pais y el valor capital
class GestorDePaises:
    def __init__(self):
        self.paises = {}
    def registrar_pais(self, pais, capital):
        self.paises[pais] = capital
    def buscar_capital(self, pais):
        if pais in self.paises:
            return self.paises[pais]
        else:
            return "País no encontrado"
    def modificar_capital(self, pais, capital):
        if pais in self.paises:
            self.paises[pais] = capital
    def eliminar_pais(self, pais):
        if pais in self.paises:
            self.paises.pop(pais)
    def mostrar_paises(self):
        return self.paises
    def cantidad_paises(self):
        return len(self.paises)

g = GestorDePaises()
g.registrar_pais("Ecuador", "Quito")
g.registrar_pais("Perú", "Lima")
g.registrar_pais("Colombia", "Bogotá")
print(f"Capital de Colombia: {g.buscar_capital('Colombia')}")
print(f"Países: {g.mostrar_paises()}")
print(f"Cantidad de países: {g.cantidad_paises()}")
print("-" * 50)
#___________________________________________________________________________

#Como lo hice
#Utilice 6 agregar pelicula, buscar pelicula, peliculas por genero, eliminar pelicula, cantidad peliculas y mostrar peliculas
#para eliminar la peliculas usamos .pop
#para mostrar la cantidad de pelicula usamos len
#append nos ayudar agregar datos
#en buscar palabras usamos if y else, esto nos ayuda a ver si la pelicula que buscamos esta, si es así retorna el nombre y sino retorna que la pelicula no existe
#en agregar pelicula aplicamos lo de clave valor, donde la clave es nombre y el valor genero
class GestorDePeliculas:
    def __init__(self):
        self.peliculas = {}
    def agregar_pelicula(self, nombre, genero):
        self.peliculas[nombre] = genero
    def buscar_pelicula(self, nombre):
        if nombre in self.peliculas:
            return self.peliculas[nombre]
        else:
            return "Película no encontrada"
    def peliculas_por_genero(self, genero):
        resultado = []
        for pelicula in self.peliculas:
            if self.peliculas[pelicula] == genero:
                resultado.append(pelicula)
        return resultado
    def eliminar_pelicula(self, nombre):
        if nombre in self.peliculas:
            self.peliculas.pop(nombre)
    def cantidad_peliculas(self):
        return len(self.peliculas)
    def mostrar_peliculas(self):
        return self.peliculas


g = GestorDePeliculas()
g.agregar_pelicula("Titanic", "Romance")
g.agregar_pelicula("Avengers", "Accion")
g.agregar_pelicula("Avatar", "Ciencia Ficcion")
print(f"Género de Titanic: {g.buscar_pelicula('Titanic')}")
print(f"Películas de Acción: {g.peliculas_por_genero('Accion')}")
print(f"Cantidad: {g.cantidad_peliculas()}")
print(f"Películas: {g.mostrar_peliculas()}")
print("-" * 50)

#_____________________________________________________________

#Como lo hice
#Utilice 4 agregra numero, agregar varios, cantidad y mostrar
#para mostrar cuantos numero son usamos len
#append nos ayudar agregar datos
#Para varios utilice esto *args
#not in evita que la fruta se repita
class GestorDeNumerosUnicos:
    def __init__(self):
        self.numeros = []
    def agregar_numero(self, numero):
        if numero not in self.numeros:
            self.numeros.append(numero)
    def agregar_varios(self, *numeros):
        for numero in numeros:
            self.agregar_numero(numero)
    def cantidad(self):
        return len(self.numeros)
    def mostrar(self):
        return self.numeros

g = GestorDeNumerosUnicos()
g.agregar_varios(10, 10, 5, 16, 10, 45, 70, 26)
print(f"Números únicos: {g.mostrar()}")
print(f"Cantidad: {g.cantidad()}")
print("-" * 50)