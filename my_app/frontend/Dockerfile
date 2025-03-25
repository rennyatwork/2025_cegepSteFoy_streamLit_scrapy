FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

COPY . .
EXPOSE 8501
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "app.py"]

#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
