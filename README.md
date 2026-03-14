Flowly es una aplicación web de gestión de finanzas personales desarrollada con **Django**.  
Permite a los usuarios registrar ingresos y gastos y administrar sus transacciones de forma simple.

---

# Funcionalidades

- Registro de usuario
- Login de usuario
- Crear transacciones (ingresos y gastos)
- Editar transacciones
- Eliminar transacciones
- Visualizar últimas transacciones

Cada usuario solo puede ver y modificar **sus propias transacciones**.

---

# Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates

---

# Ejecutar el proyecto en local

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd flowly
```


### 2. Crear entorno virtual

```bash
python -m venv env
```

### 3. Activar entorno virtual

Windows:

```bash
env\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```bash
http://127.0.0.
```

## Orden recomendado para probar la aplicación

1. Registrarse como usuario  
2. Iniciar sesión  
3. Crear una transacción (ingreso o gasto)  
4. Visualizar las transacciones en el dashboard  
5. Editar una transacción  
6. Eliminar una transacción  

---

## Estructura del proyecto

El proyecto se divide en dos aplicaciones principales:

### Users

Encargada de:

- Registro de usuario
- Login
- Autenticación

### transactions

Encargada de:

- CRUD de transacciones
- Visualización de transacciones
- Dashboard principal