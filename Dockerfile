FROM python:3.7-slim
WORKDIR /app
COPY . .
ADD test/. /test/
RUN pip install -r requirements.txt
CMD ["python", "./test/test_database_command_time.py"]
