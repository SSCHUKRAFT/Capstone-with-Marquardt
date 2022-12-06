FROM node:17-alpine 

WORKDIR /app

COPY package.json .

RUN apk update && apk add bash 

RUN npm install --force

COPY . .

EXPOSE 3001

CMD ["npm", "start"]