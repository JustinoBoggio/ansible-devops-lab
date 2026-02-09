FROM ubuntu:22.04

# Instalamos SSH y Python3
RUN apt update && apt install -y openssh-server python3 sudo && \
    mkdir /var/run/sshd

# Configuramos el usuario root para que acepte SSH
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
