FROM python:3

RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get -y install vim cron

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./get_category/script.sh /code/get_category/script.sh
COPY ./init.sh /code/init.sh
COPY ./python-cron /etc/cron.d/python-cron
RUN chmod 0644 /etc/cron.d/python-cron

RUN chmod +x /code/get_category/script.sh \
    /code/get_category/script.sh \
    /code/init.sh
CMD ["/usr/sbin/cron", "-f"]
