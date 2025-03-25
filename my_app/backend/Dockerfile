FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

COPY . .
EXPOSE 8001

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5679", "app.py"]

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
