FROM ubuntu:18.04

WORKDIR /usr/src/app

COPY requirements.txt ./




RUN apt update
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install -y python3-pip python3.8
#RUN pip3 install python3-nmap
RUN pip3 install --no-cache-dir --upgrade pip
#RUN pip install requests
RUN apt install -y nmap
RUN apt-get install -y python3-nmap
RUN apt install -y python3-tk

RUN python3 -m pip install requests
#ENV PATH "$PATH:/usr/local/lib/python3.10/site-packages/nmap/__init__.py"

#
COPY . .


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3.8", "Upkeepmonitoring.py"]
