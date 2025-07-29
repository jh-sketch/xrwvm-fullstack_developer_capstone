# Use official Python base image
FROM python:3.12.0-slim-bookworm

# Environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Set the working directory
WORKDIR $APP

# Copy requirements file and install dependencies
COPY requirements.txt $APP
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . $APP

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port your app runs on
EXPOSE 8000

# Run the entrypoint script, then start Gunicorn server
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Use gunicorn as production WSGI server
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
