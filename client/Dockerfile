FROM node:20
WORKDIR /app

COPY client/package.json client/package-lock.json ./
RUN npm install
RUN npm install --save-dev typescript

COPY client/ .
RUN npm run build