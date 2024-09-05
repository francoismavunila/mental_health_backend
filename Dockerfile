# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV SECRET_KEY "django-insecure-k5g_ru9*r5)vc))l-0+bczur8z1@y6kq=2zk4yf20^2w+53!n5"
ENV PIPELINE production

# Run the application
CMD ["gunicorn", "stress_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]