# Stage 1: build
FROM python:3.10-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: runtime
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY app/ .
EXPOSE 5001
CMD ["python", "app.py"]
