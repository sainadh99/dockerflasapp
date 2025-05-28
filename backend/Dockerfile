# Stage 1: dependencies install
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install

# Stage 2: production build
FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 5000
CMD ["node", "server.js"]
