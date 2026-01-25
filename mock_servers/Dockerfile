FROM python:3.12-slim

WORKDIR /app/tests

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["sh","-c","python3 mock_service.py && tail -f /dev/null"]