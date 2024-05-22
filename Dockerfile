# Stage 1: Build stage
FROM python:3.8-slim AS builder

# Set the working directory
WORKDIR /app

# Install Streamlit and other dependencies
RUN pip install --no-cache-dir streamlit

# Copy the application source code
COPY . .

# Stage 2: Run stage
FROM gcr.io/distroless/python3

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8

# Expose the port the app runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "todo_app.py"]
