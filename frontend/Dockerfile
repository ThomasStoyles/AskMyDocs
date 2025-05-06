# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install deps
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Start the app
CMD ["npm", "start"]
