FROM python:3.9-slim

WORKDIR /user/src/app


COPY config_db.py .
COPY appartements_data_db.csv .
COPY requirements.txt .



RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python","config_db.py"]