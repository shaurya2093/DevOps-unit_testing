# Use Node.js version 16 or higher
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json into the container's working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of your application files into the container
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]
