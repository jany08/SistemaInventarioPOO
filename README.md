# 🛒 Sistema Avanzado de Gestión de Inventario

Este proyecto implementa un sistema de gestión de inventarios en **Python**, aplicando **Programación Orientada a Objetos (POO)**, **colecciones** (`dict`, `list`, `set`, `tuple`) y **almacenamiento en archivos** (`JSON`) para mantener los datos de manera persistente.

---

## 📌 Características

- **Clase Producto** con atributos:
  - `ID` (único)
  - `nombre`
  - `cantidad`
  - `precio`
- **Clase Inventario** con métodos para:
  - Añadir productos
  - Eliminar productos por ID
  - Actualizar cantidad o precio
  - Buscar productos por nombre
  - Mostrar todo el inventario
- **Colecciones utilizadas**:
  - `dict` → para almacenar productos con clave `ID` (búsqueda eficiente).
  - `list` → para mostrar todos los productos.
  - `set` → para obtener nombres únicos.
  - `tuple` → para devolver resultados de búsqueda como inmutables.
- **Persistencia**:
  - Guardado y carga del inventario en un archivo `inventario.json` usando formato **JSON**.

---

## 📂 Archivos principales

- `Sistema_Inventario.py` → código principal con menú interactivo.
- `inventario.json` → archivo de datos generado automáticamente para almacenar los productos.

---

## ▶️ Uso

1. Clona este repositorio o descarga el archivo.
2. Abre el proyecto en **PyCharm**.
3. Ejecuta el archivo:

```bash
python Sistema_Inventario.py
