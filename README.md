# ⚔️ Proyecto de Personajes en Batalla - Python POO

Este fue uno de mis **primeros proyectos con Python** y fue clave para comprender los fundamentos de la **Programación Orientada a Objetos (POO)**. Desarrollé una pequeña simulación de combate entre personajes, incluyendo clases personalizadas, herencia, métodos sobrescritos y lógica de ataque/defensa.

---

## 🧠 ¿Qué aprendí con este proyecto?

- Cómo definir **clases y atributos**.
- Uso de **herencia** para extender funcionalidades (como en `Guerrero` y `Mago`).
- Aplicación de **sobreescritura de métodos** (`__init__`, `imprimir_atributos`, `dañar`, etc.).
- Interacción entre objetos mediante **ataques y defensa**.
- Simulación de lógica condicional y entrada de usuario (`input`).
- Mejores prácticas básicas de estructuración de código.

---

## 🧱 Estructura del proyecto

El programa define una clase base `Personaje` y dos clases hijas:

- `Guerrero`: hace más daño basado en su fuerza y su espada.
- `Mago`: inflige daño usando su inteligencia y libro.

### 🔹 Clase `Personaje`
Métodos clave:
- `imprimir_atributos()`
- `atacar(enemigo)`
- `dañar(enemigo)`
- `morir()`
- `esta_vivo()`
- `subir_nivel()`

### 🔹 Clases hijas: `Guerrero` y `Mago`
Sobrescriben el cálculo de daño e impresión de atributos. También permiten escoger un arma o libro, lo que modifica el daño final.

---

## 🕹️ ¿Cómo se usa?

1. Se crean los objetos: un personaje genérico, un guerrero y un mago.
2. Se imprimen sus atributos iniciales.
3. Se ejecutan ataques entre ellos.
4. Se muestran los atributos después del combate.

---

## 💻 Ejemplo de salida

```plaintext
Arturo Suárez ha realizado 40 puntos de daño a Gandalf
vida de Gandalf es 60
