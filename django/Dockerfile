FROM django:onbuild
MAINTAINER Vyacheslav Tykhonov
RUN apt-get install -y wget patch git
RUN git clone https://github.com/DANS-KNAW/miniverse 
RUN cd miniverse
#RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["python manage.py runserver"]
