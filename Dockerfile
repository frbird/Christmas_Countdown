FROM nginx:alpine

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy website files to nginx html directory (excluding Docker files)
COPY countdown_website.html fonts/ images/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

