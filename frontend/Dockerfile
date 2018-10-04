FROM node:8

# install simple http server for serving static content
RUN npm install -g @vue/cli-service

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
CMD ./run.sh
