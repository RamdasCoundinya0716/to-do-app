# Stage 1: Build stage
FROM python:3.8-slim as builder

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Stage 2: Runtime stage
FROM gcr.io/distroless/python3

# Set the working directory
WORKDIR /app

# Copy the dependencies from the build stage
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "todo_app.py"]