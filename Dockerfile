FROM continuumio/miniconda3
MAINTAINER Jorman Copete
RUN apt-get update -y && \
    apt-get install python3-opencv -y
    
WORKDIR /
COPY . ./
RUN pip install -r requirements.txt
RUN conda create -n tf tensorflow
CMD ["UI_main.py"]
ENTRYPOINT ["python3"]
