FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Production image using serve
FROM node:20-alpine

WORKDIR /app
RUN npm install -g serve

COPY --from=builder /app/dist .

EXPOSE 4173
CMD ["serve", "-s", ".", "-l", "4173"]
