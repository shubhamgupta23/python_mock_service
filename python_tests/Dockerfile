FROM python:3.12-slim

WORKDIR /app/tests

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh","-c","pytest test_mock.py -sv"]