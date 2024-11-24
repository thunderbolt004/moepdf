# moepdf
## DOC to PDF Conversion Service

This project provides a web-based service for converting `.docx` files to `.pdf` format. Built with **Flask** for the backend, **Gunicorn** as the WSGI server, and **LibreOffice** for document conversion, this service is containerized using **Docker** to ensure consistent and easy deployment across different environments.

---

## Features
- **File Upload**: Users can upload `.docx` files for conversion.
- **DOCX to PDF Conversion**: The uploaded `.docx` files are converted to `.pdf` using LibreOffice.
- **Dockerized**: The application is fully containerized, making it easy to deploy in any environment with Docker.
- **Flask and Gunicorn**: The backend is powered by Flask, with Gunicorn for serving the app in production.

---

## Getting Started

### Prerequisites

Before you can run this project locally, make sure you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop) (For building and running the container)

### Setting Up the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/thunderbolt004/moepdf.git
   cd moepdf
   ```

2. **Build and Run the Docker Container**

   Ensure Docker is running on your machine. You can build the container with the following command:

   ```bash
   docker build -t moepdf .
   ```

   Once the build is complete, run the container:

   ```bash
   docker run -p 5000:5000 moepdf
   ```

   This will start the application on port 5000.

### Running the Application Locally (Without Docker)

If you prefer to run the application without Docker, you can do so with the following steps:

1. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install LibreOffice**

   You need LibreOffice installed on your machine to handle the `.docx` to `.pdf` conversion. 

     ```bash
     sudo apt-get install libreoffice-writer
     ```

4. **Run the Flask Application**

   After setting up everything, you can run the Flask app locally with:

   ```bash
   python app.py
   ```

   The app will be available at `http://127.0.0.1:5000/`.

---


## Docker Setup

The Dockerfile is set up to create a Docker image containing the necessary dependencies. Here’s a breakdown:

### Dockerfile

```dockerfile
FROM python:3.9.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside container
WORKDIR /moepdf

# Install necessary packages and dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Install LibreOffice for DOCX to PDF conversion
RUN apk add libreoffice-writer

# Expose the port the app runs on
EXPOSE 5000

# Start the application with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
```

This Dockerfile does the following:
- Uses `python:3.9.13-alpine` as the base image.
- Installs Python dependencies from `requirements.txt`.
- Installs LibreOffice to convert `.docx` files to `.pdf`.
- Exposes port `5000` for the Flask app.
- Runs the Flask app using Gunicorn with 2 worker processes.

### Running the Docker Container

To build and run the Docker container, use the following commands:

1. **Build the Docker image:**

   ```bash
   docker build -t doc-to-pdf .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 doc-to-pdf
   ```

---

## Acknowledgments

- **Flask**: A lightweight Python web framework.
- **Gunicorn**: A WSGI HTTP server for Python.
- **LibreOffice**: Open-source office software for document conversion.
- **Docker**: Containerization platform for packaging and deploying applications.

