FROM python:latest
 
WORKDIR /MissRaya
COPY . /MissRaya
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "MissRaya"]