FROM node:22-alpine AS builder

WORKDIR /app

# RUN npm install --frozen-lockfile

# Copy the rest of the application
COPY ../src/frontend .

# Install dependencies
# RUN npm install --frozen-lockfile

# Build the frontend
RUN npm run dev

# Use Nginx for serving static files
FROM nginx:stable-alpine

# Copy built frontend files to Nginx's serving directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 8888

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
