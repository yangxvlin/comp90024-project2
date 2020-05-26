FROM node:14.3.0

EXPOSE 3000

WORKDIR /usr/frontend

COPY src src

COPY public public

COPY package.json package.json

RUN yarn

CMD ["npm", "start"]
