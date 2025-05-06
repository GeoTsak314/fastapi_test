# Export Data Example with FastAPI

This example demonstrates how to build a FastAPI application that exports structured data to multiple formats, including:

- JSON
- CSV
- Excel
- PDF
- Parquet
- MySQL Database

## 🚀 How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Start the FastAPI server**:

```bash
uvicorn main:app --reload
```

3. **Open your browser** and navigate to:

```
http://127.0.0.1:8000/
```

You’ll be automatically redirected to the **interactive Swagger UI** at `/docs`.

---

## 🛠 Export Endpoint

**GET** `/export`

### Query Parameter:
| Name   | Type   | Description                                |
|--------|--------|--------------------------------------------|
| format | string | One of: `json`, `csv`, `excel`, `pdf`, `parquet`, `mysql` |

### Example:
```http
GET /export?format=excel
```

---

## 🗄 MySQL Export

To export to a MySQL database, set the following environment variables:

- `MYSQL_HOST`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_DATABASE`

Or edit them directly in `main.py` if running locally.

---

## 📦 Dependencies

See `requirements.txt` for all required packages:
- `fastapi`
- `uvicorn`
- `pandas`
- `xlsxwriter`
- `reportlab`
- `pyarrow`
- `mysql-connector-python`

---

## ✅ Features

- Modular export logic for clean and scalable code
- Real-time file generation for CSV, Excel, PDF, Parquet
- Database export with basic schema creation
- Swagger and ReDoc UI for exploration

---

## 📄 License

MIT - Provided as an example for educational and contribution purposes.
