FROM python:3.7-slim
WORKDIR /app
COPY . .
ADD ./Test/. /Test/
RUN pip install -r requirements.txt
CMD ["python", "./test/test_database_command_time.py"]
