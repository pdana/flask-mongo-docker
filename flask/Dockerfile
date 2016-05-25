FROM centos:7
RUN yum install epel-release -y
RUN yum install python-pip -y
RUN pip install --upgrade pip
RUN pip install flask pymongo
EXPOSE 8080
COPY dr-app.py .
ENTRYPOINT ["/bin/python", "dr-app.py"]
LABEL app=flask version=1.0

