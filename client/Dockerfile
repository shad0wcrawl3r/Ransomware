FROM ubuntu:latest
RUN apt update
RUN apt install openssh-server -y
RUN /etc/init.d/ssh start
EXPOSE 22
CMD tail -f /var/log/dpkg.log

