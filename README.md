# flask_demo
Sample flask project with docker and gunicorn


# Environment variables

    source env_vars.sh

# Deploying with docker

1. Application

        docker build -t flask_demo:1 .
        docker run -d -p 8000:8000 flask_demo:1

2. MS SQL Server

        docker build -t mssql -f DockerFile-MSSQL .
        docker run -d -p 1433:1433 mssql
