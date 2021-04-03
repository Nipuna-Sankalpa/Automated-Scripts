FROM centos/systemd
LABEL authors = "Yellow Flash"

# install pre-requisites

RUN yum -y update
RUN mkdir -p /var/lib/elasticdump
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum -y update && yum install -y gcc-c++ make nodejs python3 cronie
RUN npm install elasticdump -g
RUN pip3 install pyaml elasticsearch