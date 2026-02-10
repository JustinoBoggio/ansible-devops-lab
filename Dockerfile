# Use Ubuntu 22.04 as the base image for our managed nodes
FROM ubuntu:22.04

# Install SSH server, Python3 (required by Ansible), and sudo
RUN apt update && apt install -y openssh-server python3 sudo && \
    mkdir /var/run/sshd

# Set root password to 'root' for initial setup
RUN echo 'root:root' | chpasswd

# Permit root login via SSH for lab purposes
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Standard SSH port
EXPOSE 22

# Start SSH service in the foreground
CMD ["/usr/sbin/sshd", "-D"]