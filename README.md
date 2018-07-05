# flask_demo
Sample flask project with docker and gunicorn


# Environment variables
# Make sure you create env_vars.sh from env_vars.sh.template for respective environment

    source env_vars.sh

# Deploying with docker
    docker network create mynet

1. Application

        docker build -t flask_demo:1 .
        docker run --net mynet --name flask_demo --env-file env_vars.sh -d -p 8000:8000 flask_demo:1

2. MS SQL Server

        docker build -t mssql -f Dockerfile-MSSQL .
        docker run --net mynet --name mssqldev -d -p 1433:1433 mssql
