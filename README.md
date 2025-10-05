# Proyecto OS 2025-2: API de Items + Servicio HTTP

Este proyecto contiene dos servicios que se ejecutan con systemd y se exponen mediante ngrok:
1. **Items API**: API REST con FastAPI y SQLite
2. **Simple HTTP Service**: Servidor HTTP estático con Python

---

## 📁 Estructura del Proyecto

```
OS_2025_2/
├── items_api/                    # Servicio 1: API de Items
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py          # Configuración de base de datos
│   │   ├── models.py            # Modelos SQLAlchemy
│   │   ├── schemas.py           # Esquemas Pydantic
│   │   └── routes.py            # Endpoints de la API
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── requirements.txt         # Dependencias de Python
│   └── items-api.service        # Archivo systemd
│
├── simple_http_service/         # Servicio 2: HTTP Simple
│   ├── index.html              # Página de inicio
│   └── simple-http.service     # Archivo systemd
│
└── README.md                    # Este archivo
```

---

## 🚀 Instalación Rápida

### Prerequisitos
- Python 3.8 o superior
- pip
- ngrok account (gratuito en https://ngrok.com)

### Paso 1: Configurar Items API

```bash
# 1. Navegar al directorio del proyecto
cd items_api

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Probar localmente
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Abre tu navegador en:
- **API Docs**: http://localhost:8000/docs
- **Root**: http://localhost:8000

### Paso 2: Probar la API

**GET - Obtener todos los items:**
```bash
curl http://localhost:8000/items
```

**POST - Crear items:**
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Lapiz", "price": 1200.50},
    {"name": "Cuaderno", "price": 3500}
  ]'
```

---

## 🔧 Configurar Servicios Systemd

### Para Items API

```bash
# 1. Editar el archivo de servicio
nano items_api/items-api.service

# Reemplazar:
# - YOUR_USERNAME con tu usuario (ej: ubuntu, tu_usuario)
# - /path/to/items_api con la ruta absoluta (ej: /home/ubuntu/OS_2025_2/items_api)

# 2. Copiar a systemd
sudo cp items_api/items-api.service /etc/systemd/system/

# 3. Recargar systemd
sudo systemctl daemon-reload

# 4. Habilitar servicio (inicia automáticamente al boot)
sudo systemctl enable items-api

# 5. Iniciar servicio
sudo systemctl start items-api

# 6. Verificar estado
sudo systemctl status items-api

# Ver logs si hay problemas:
sudo journalctl -u items-api -f
```

### Para Simple HTTP Service

```bash
# 1. Editar el archivo de servicio
nano simple_http_service/simple-http.service

# Reemplazar:
# - YOUR_USERNAME con tu usuario
# - /path/to/simple_http_service con la ruta absoluta

# 2. Copiar a systemd
sudo cp simple_http_service/simple-http.service /etc/systemd/system/

# 3. Recargar systemd
sudo systemctl daemon-reload

# 4. Habilitar servicio
sudo systemctl enable simple-http

# 5. Iniciar servicio
sudo systemctl start simple-http

# 6. Verificar estado
sudo systemctl status simple-http
```

---

## 🌐 Exponer con ngrok

### Instalar ngrok

```bash
# Descargar e instalar
# Visita: https://ngrok.com/download

# En Linux/Mac:
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
  sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list && \
  sudo apt update && sudo apt install ngrok

# Autenticar (obtén tu token en https://dashboard.ngrok.com/get-started/your-authtoken)
ngrok config add-authtoken TU_TOKEN_AQUI
```

### Exponer Items API (Puerto 8000)

```bash
# En una terminal separada:
ngrok http 8000
```

Verás algo como:
```
Forwarding  https://abc123.ngrok.app -> http://localhost:8000
```

**URLs públicas:**
- API: `https://abc123.ngrok.app/items`
- Docs: `https://abc123.ngrok.app/docs`

### Exponer Simple HTTP Service (Puerto 9000)

```bash
# En otra terminal:
ngrok http 9000
```

Verás:
```
Forwarding  https://xyz789.ngrok.app -> http://localhost:9000
```

---

## 📝 Comandos Útiles

### Gestión de Servicios

```bash
# Ver estado
sudo systemctl status items-api
sudo systemctl status simple-http

# Reiniciar
sudo systemctl restart items-api
sudo systemctl restart simple-http

# Detener
sudo systemctl stop items-api
sudo systemctl stop simple-http

# Deshabilitar autoarranque
sudo systemctl disable items-api
sudo systemctl disable simple-http

# Ver logs en tiempo real
sudo journalctl -u items-api -f
sudo journalctl -u simple-http -f
```

### Items API

```bash
# Activar entorno virtual
cd items_api
source venv/bin/activate

# Ejecutar manualmente (modo desarrollo)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Ver base de datos SQLite
sqlite3 items.db "SELECT * FROM items;"
```

---

## 🧪 Ejemplos de Uso de la API

### Usando curl

```bash
# GET - Listar items
curl https://tu-url.ngrok.app/items

# POST - Crear un item
curl -X POST https://tu-url.ngrok.app/items \
  -H "Content-Type: application/json" \
  -d '[{"name": "Marcador", "price": 2500}]'

# POST - Crear múltiples items
curl -X POST https://tu-url.ngrok.app/items \
  -H "Content-Type: application/json" \
  -d '[
    {"name": "Borrador", "price": 800},
    {"name": "Regla", "price": 1500},
    {"name": "Compas", "price": 4200}
  ]'
```

### Usando Python

```python
import requests

# GET
response = requests.get("https://tu-url.ngrok.app/items")
print(response.json())

# POST
items = [
    {"name": "Calculadora", "price": 15000},
    {"name": "Mochila", "price": 35000}
]
response = requests.post("https://tu-url.ngrok.app/items", json=items)
print(response.json())
```

---

## 🏗️ Arquitectura del Proyecto

### Items API

- **Framework**: FastAPI
- **Base de datos**: SQLite (archivo `items.db`)
- **ORM**: SQLAlchemy
- **Validación**: Pydantic
- **Servidor**: Uvicorn

### Componentes:

1. **database.py**: Configuración de SQLAlchemy y sesiones
2. **models.py**: Modelo `Item` para la tabla `items`
3. **schemas.py**: Esquemas Pydantic para validación
4. **routes.py**: Endpoints GET y POST
5. **main.py**: Aplicación FastAPI principal

### Simple HTTP Service

- Servidor HTTP estático con Python `http.server`
- Sirve archivos desde el directorio actual
- Puerto 9000

---

## 📊 Esquema de Base de Datos

### Tabla: items

| Campo      | Tipo         | Descripción                    |
|------------|--------------|--------------------------------|
| id         | INTEGER      | Primary Key, Autoincrement     |
| name       | VARCHAR(200) | Nombre del item (requerido)    |
| price      | NUMERIC(10,2)| Precio del item (> 0)          |
| created_at | DATETIME     | Timestamp de creación          |

---

## 🔍 Validaciones

La API valida automáticamente:
- ✅ `name`: Mínimo 1 carácter, máximo 200
- ✅ `price`: Debe ser mayor a 0, máximo 10 dígitos, 2 decimales
- ✅ `created_at`: Opcional, formato datetime ISO

---

## 🛠️ Troubleshooting

### La API no inicia

```bash
# Verificar logs
sudo journalctl -u items-api -n 50

# Verificar que el puerto 8000 no esté en uso
sudo lsof -i :8000

# Probar manualmente
cd items_api
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Error de permisos

```bash
# Verificar propietario del directorio
ls -la items_api/

# Cambiar propietario si es necesario
sudo chown -R tu_usuario:tu_usuario items_api/
```

### ngrok no conecta

```bash
# Verificar que el servicio esté corriendo
curl http://localhost:8000
curl http://localhost:9000

# Verificar authtoken
ngrok config check
```

---

## 📦 Dependencias

Ver `requirements.txt` para versiones específicas:
- fastapi
- uvicorn
- sqlalchemy
- pydantic

---

## 👨‍💻 Desarrollo

### Agregar nuevos endpoints

Edita `app/routes.py` y agrega tus funciones.

### Modificar el modelo

1. Edita `app/models.py`
2. Elimina `items.db`
3. Reinicia el servicio (se recreará la base de datos)

### Tests

```bash
# Instalar pytest (opcional)
pip install pytest httpx

# Crear tests/test_api.py
# pytest tests/
```

---

## ✅ Checklist de Entrega

- [ ] Items API corriendo en systemd
- [ ] Items API expuesta con ngrok
- [ ] Simple HTTP Service corriendo en systemd
- [ ] Simple HTTP Service expuesto con ngrok
- [ ] Ambos servicios inician automáticamente con el sistema
- [ ] Documentación completa en README
- [ ] Servicios probados con curl/navegador

---

## 📝 Notas Adicionales

- El servicio `items-api` se reinicia automáticamente si falla
- La base de datos SQLite se crea automáticamente en el primer inicio
- Los logs están disponibles con `journalctl`
- ngrok en versión gratuita genera URLs aleatorias en cada inicio
- Para URLs permanentes, considera ngrok Pro o alternativas como serveo.net

---

## 🎓 Créditos

Proyecto desarrollado para OS 2025-2  
Universidad: [Tu Universidad]  
Estudiante: [Tu Nombre]

---

¡Listo para ejecutar! 🚀

