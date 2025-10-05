# 📁 Project Structure

```
OS_2025_2/
│
├── 📖 README.md                      # Complete documentation
├── 📖 QUICK_START.md                 # 5-minute setup guide
├── 📖 PROJECT_STRUCTURE.md           # This file
├── 🧪 test_api.sh                    # Test script for API
├── 🚫 .gitignore                     # Git ignore rules
│
├── 📦 items_api/                     # SERVICE 1: Items REST API
│   ├── app/                          # Application package
│   │   ├── __init__.py              # Package initializer
│   │   ├── database.py              # 🗄️  SQLAlchemy config & session
│   │   ├── models.py                # 🗃️  Item model (ORM)
│   │   ├── schemas.py               # ✅ Pydantic validation schemas
│   │   └── routes.py                # 🛣️  API endpoints (GET/POST)
│   │
│   ├── main.py                       # 🚀 FastAPI app entry point
│   ├── requirements.txt              # 📦 Python dependencies
│   ├── setup.sh                      # ⚙️  Quick setup script
│   └── items-api.service             # 🔧 Systemd service file
│
└── 📦 simple_http_service/           # SERVICE 2: Simple HTTP Server
    ├── index.html                    # 🌐 Static HTML page
    └── simple-http.service           # 🔧 Systemd service file
```

---

## 🔍 File Descriptions

### Root Level

| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation with all commands |
| `QUICK_START.md` | 5-minute quick start guide |
| `PROJECT_STRUCTURE.md` | This file - project structure overview |
| `test_api.sh` | Automated test script for the API |
| `.gitignore` | Git ignore rules (venv, db files, etc.) |

### Items API (`items_api/`)

#### Core Application Files

| File | Purpose | Description |
|------|---------|-------------|
| `main.py` | Entry point | Creates FastAPI app, includes routes, initializes DB |
| `requirements.txt` | Dependencies | Python packages needed |
| `setup.sh` | Setup script | Automated setup (venv, pip install) |

#### Application Package (`app/`)

| File | Responsibility | Key Components |
|------|---------------|----------------|
| `database.py` | Database layer | SQLAlchemy engine, SessionLocal, Base, get_db() |
| `models.py` | Data models | Item ORM model (id, name, price, created_at) |
| `schemas.py` | Validation | ItemIn (request), ItemOut (response) Pydantic models |
| `routes.py` | API endpoints | GET /items, POST /items |

#### System Integration

| File | Purpose |
|------|---------|
| `items-api.service` | Systemd service definition for auto-start |

### Simple HTTP Service (`simple_http_service/`)

| File | Purpose |
|------|---------|
| `index.html` | Static webpage served by Python http.server |
| `simple-http.service` | Systemd service definition |

---

## 🔄 Data Flow

### POST /items Request

```
Client → FastAPI → routes.py → Pydantic Validation (schemas.py)
                             ↓
                    models.py (Item ORM)
                             ↓
                    database.py (SQLAlchemy)
                             ↓
                    SQLite (items.db)
                             ↓
                    Response (ItemOut)
```

### GET /items Request

```
Client → FastAPI → routes.py → database.py (query)
                             ↓
                    SQLite (items.db)
                             ↓
                    models.py (Item objects)
                             ↓
                    Pydantic serialize (ItemOut)
                             ↓
                    JSON Response
```

---

## 🗃️ Database Schema

### Table: `items`

```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    created_at DATETIME NOT NULL
);
```

---

## 🔌 API Endpoints

### GET /items
- **Purpose**: Retrieve all items
- **Response**: List of ItemOut objects
- **Handler**: `routes.py::read_items()`

### POST /items
- **Purpose**: Create one or more items
- **Request Body**: List of ItemIn objects
- **Response**: List of created ItemOut objects
- **Handler**: `routes.py::create_items()`

### GET /
- **Purpose**: Root endpoint with API info
- **Handler**: `main.py::root()`

### GET /docs
- **Purpose**: Interactive API documentation (auto-generated)
- **Framework**: Swagger UI

---

## 🔧 Technologies Used

### Items API Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Programming language |
| FastAPI | 0.104.1 | Web framework |
| Uvicorn | 0.24.0 | ASGI server |
| SQLAlchemy | 2.0.23 | ORM |
| Pydantic | 2.5.0 | Data validation |
| SQLite | 3 | Database |

### Simple HTTP Service

| Technology | Purpose |
|------------|---------|
| Python http.server | Built-in HTTP server |
| HTML5 | Static webpage |

### System Integration

| Technology | Purpose |
|------------|---------|
| systemd | Service management |
| ngrok | Public URL tunneling |

---

## 🚀 Execution Flow

### Development Mode
```
Terminal → setup.sh → venv → pip install
                           ↓
         uvicorn main:app (reload mode)
                           ↓
         FastAPI app starts → SQLite DB created
                           ↓
         API available at localhost:8000
```

### Production Mode (systemd)
```
System Boot → systemd → items-api.service
                     ↓
         Activate venv → uvicorn main:app
                     ↓
         API starts automatically
                     ↓
         Restart on failure
```

### Public Exposure
```
Local API (port 8000) → ngrok http 8000
                      ↓
         Public URL: https://xxx.ngrok.app
                      ↓
         Internet access to API
```

---

## 📋 Design Patterns Used

1. **Dependency Injection**: FastAPI's `Depends()` for database sessions
2. **Repository Pattern**: Database operations isolated in models
3. **DTO Pattern**: Separate Input/Output schemas
4. **Factory Pattern**: `get_db()` session factory
5. **Layered Architecture**:
   - Presentation Layer: `routes.py`
   - Business Logic Layer: `schemas.py` validation
   - Data Access Layer: `models.py` + `database.py`

---

## 🧪 Testing

Use the provided `test_api.sh` script:

```bash
# Test local API
./test_api.sh

# Test ngrok URL
./test_api.sh https://your-url.ngrok.app
```

---

## 📚 Additional Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org
- **Pydantic Docs**: https://docs.pydantic.dev
- **systemd Docs**: https://systemd.io
- **ngrok Docs**: https://ngrok.com/docs

---

Created for OS 2025-2 Project 🎓

