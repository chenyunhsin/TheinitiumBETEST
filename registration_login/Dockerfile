# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=registration_login.settings

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

