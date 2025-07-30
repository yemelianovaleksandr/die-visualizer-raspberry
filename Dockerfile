FROM python:3.10

# Install ffmpeg with libx264 support
RUN apt-get update && \
    apt-get install -y ffmpeg libx264-dev && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run Flask application
CMD ["python3", "app/app.py"]
