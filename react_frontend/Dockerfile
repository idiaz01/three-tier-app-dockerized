#Node image
FROM node:latest as build

#Set working directory
WORKDIR /webapp
ADD . /webapp

#Add /webapp/node_modules/.bin to environment variables
ENV PATH /webapp/node_modules/.bin:$PATH

#Install dependencies
COPY package.json /webapp/package.json
RUN npm install

#Build application
RUN npm run build

#Nginx image and deploy build image.
FROM nginx:1.17-alpine

COPY --from=build /webapp/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]