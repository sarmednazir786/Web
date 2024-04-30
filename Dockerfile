# Use a lightweight image for the base
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Install Flask dependency
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the Flask script and template (if applicable)
COPY . .

# Expose the port where the Flask app runs
EXPOSE 5000

# Set the command to run the Flask app
CMD python3 server.py