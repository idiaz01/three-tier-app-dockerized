FROM node:latest

EXPOSE 3000
EXPOSE 35729

WORKDIR /webapp

ENV PATH /webapp/node_modules/.bin:$PATH

COPY package.json /webapp/package.json


RUN npm install --silent
RUN npm install react-scripts -g --silent

ADD . /webapp

CMD ["npm", "start"]
