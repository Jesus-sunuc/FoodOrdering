FROM node:20-alpine as builder
WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .
RUN npm install --save-dev typescript

RUN npm run build

# FROM nginx
# RUN apt update && apt install -y curl
# WORKDIR /usr/share/nginx/html
# COPY default.conf /etc/nginx/conf.d/default.conf
# COPY --from=builder /app/dist .
CMD ["nginx", "-g", "daemon off;"]