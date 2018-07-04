FROM python:3.6.5

# apt-get and system utilities
RUN apt-get update && apt-get install -y apt-utils apt-transport-https debconf-utils gcc build-essential

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev mssql-tools

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

RUN mkdir -p /appl/flask_demo/logs

COPY . /appl/flask_demo/
#RUN /bin/bash -c "source /appl/flask_demo/env_vars.sh.template"

WORKDIR /appl/flask_demo/project
RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
