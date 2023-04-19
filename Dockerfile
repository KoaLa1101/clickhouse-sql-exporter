FROM python:3.9-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py
RUN mkdir app_config
COPY config/queries.json /app_config/queries.json
COPY config/config.json /app_config/config.json

EXPOSE 9439

CMD ["python", "main.py"]
