from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, StreamingResponse, RedirectResponse
import pandas as pd
import io
import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector



app = FastAPI(title="Data Export Example")



# Dummy data source
data = [
    {"id": 1, "name": "Sebastian", "age": 27},
    {"id": 2, "name": "Joanna", "age": 22},
    {"id": 3, "name": "George", "age": 37}
]



def export_to_csv(df: pd.DataFrame):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=df.columns)
    writer.writeheader()
    writer.writerows(df.to_dict(orient="records"))
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=data.csv"})

def export_to_excel(df: pd.DataFrame):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    output.seek(0)
    return StreamingResponse(output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                             headers={"Content-Disposition": "attachment; filename=data.xlsx"})

def export_to_pdf(df: pd.DataFrame):
    output = io.BytesIO()
    pdf = canvas.Canvas(output, pagesize=letter)
    pdf.drawString(100, 750, "Exported Data")
    y = 730
    for row in df.to_dict(orient="records"):
        pdf.drawString(100, y, str(row))
        y -= 20
    pdf.save()
    output.seek(0)
    return StreamingResponse(output, media_type="application/pdf",
                             headers={"Content-Disposition": "attachment; filename=data.pdf"})

def export_to_parquet(df: pd.DataFrame):
    output = io.BytesIO()
    df.to_parquet(output, engine="pyarrow", index=False)
    output.seek(0)
    return StreamingResponse(output, media_type="application/octet-stream",
                             headers={"Content-Disposition": "attachment; filename=data.parquet"})

def export_to_mysql(df: pd.DataFrame):
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "testdb")
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS exported_data (id INT, name VARCHAR(255), age INT)")
    cursor.executemany("INSERT INTO exported_data (id, name, age) VALUES (%s, %s, %s)",
                       [(row["id"], row["name"], row["age"]) for row in df.to_dict(orient="records")])
    conn.commit()
    cursor.close()
    conn.close()
    return JSONResponse(content={"message": "Data successfully exported to MySQL."})




@app.get("/export")
async def export_data(format: str = Query("json", enum=["json", "csv", "excel", "pdf", "parquet", "mysql"])):
    df = pd.DataFrame(data)

    if format == "json":
        return JSONResponse(content=df.to_dict(orient="records"))
    elif format == "csv":
        return export_to_csv(df)
    elif format == "excel":
        return export_to_excel(df)
    elif format == "pdf":
        return export_to_pdf(df)
    elif format == "parquet":
        return export_to_parquet(df)
    elif format == "mysql":
        return export_to_mysql(df)

    return JSONResponse(content={"error": "Invalid format"}, status_code=400)



@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
