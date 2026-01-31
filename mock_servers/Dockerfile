FROM python:3.12-slim

# Install curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/tests

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# CMD ["sh","-c","python3 mock_service.py && tail -f /dev/null"]
CMD ["python3","mock_service.py"]