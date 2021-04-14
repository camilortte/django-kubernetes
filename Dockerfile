FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
ENV APP_HOME=/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY app-dummy/ $APP_HOME/app-dummy/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r app-dummy/requirements.txt

COPY app-dummy/docker-entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 777 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /
ENTRYPOINT ["bash","entrypoint.sh"]