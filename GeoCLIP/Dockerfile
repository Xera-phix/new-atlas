# Use an official NVIDIA CUDA runtime image as a parent image.
# This provides the necessary drivers and libraries for GPU access.
# Make sure the CUDA version is compatible with the PyTorch version you're using.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Set environment variables to ensure Python output is sent straight to the terminal
# without being buffered, which is useful for logging.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python, pip, and other system dependencies.
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
# We install torch separately to ensure we get a version compatible with the CUDA toolkit.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container.
COPY . .

# Create a non-privileged user to run the app
RUN useradd -m appuser
USER appuser

# Expose the port your app runs on.
EXPOSE 8000

# Define the command to run your app using uvicorn.
# This will start the FastAPI server and make it accessible.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
