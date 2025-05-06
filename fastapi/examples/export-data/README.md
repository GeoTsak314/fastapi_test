# Export Data Example with FastAPI

This example demonstrates how to build a FastAPI application that exports structured data to various destinations, including:

## 📁 File Formats
- JSON
- CSV
- Excel
- PDF
- Parquet
- Avro
- Feather
- ORC

## 🗄 Databases & Storage
- MySQL
- SQLite
- AWS S3

## 🔄 Streaming Systems
- Kafka
- RabbitMQ
- Apache Pulsar

---

## 🚀 How to Run

1. **Install dependencies**:

```bash
pip install -r requirements_all_exports.txt
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
| Name   | Type   | Description |
|--------|--------|-------------|
| format | string | One of the supported formats listed above |

### Example:
```http
GET /export?format=excel
```

---

## 🔐 Environment Variables

### AWS S3:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_S3_BUCKET`
- `AWS_S3_OBJECT_KEY`

### MySQL:
- `MYSQL_HOST`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_DATABASE`

### Kafka:
- `KAFKA_BOOTSTRAP_SERVERS` (default: `localhost:9092`)
- `KAFKA_TOPIC` (default: `exported_data`)

### RabbitMQ:
- `RABBITMQ_HOST` (default: `localhost`)
- `RABBITMQ_QUEUE` (default: `export_queue`)

### Pulsar:
- `PULSAR_SERVICE_URL` (default: `pulsar://localhost:6650`)
- `PULSAR_TOPIC` (default: `exported_data`)

---

## ✅ Features

- Modular and extensible export logic
- Cloud- and stream-ready integrations
- Swagger UI for testing and documentation
- Easy setup with standard Python tools

---

## 📄 License

MIT - Provided as an open example for educational and development purposes.
