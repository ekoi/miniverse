FROM python:2.7
MAINTAINER Vyacheslav Tykhonov
COPY . /miniverse
WORKDIR /miniverse
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py", "migrate"]
CMD ["manage.py", "createsuperuser"]
CMD ["manage.py", "collectstatic"]
CMD ["manage.py", "runserver", "0.0.0.0:5000"]
EXPOSE 5000
