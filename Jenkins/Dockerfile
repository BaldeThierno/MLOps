FROM jenkins/jenkins:2.332.3-jdk11 
USER root
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN apt-get update && apt-get install -y lsb-release && apt-get install sshpass && apt-get install sudo
RUN apt -y install software-properties-common
#RUN apt-add-repository -y ppa:ansible/ansible
RUN	apt-get -y install ansible 

RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \ 
  https://download.docker.com/linux/debian/gpg 
RUN echo "deb [arch=$(dpkg --print-architecture) \ 
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \ 
  https://download.docker.com/linux/debian \ 
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list 
RUN apt-get update && apt-get install -y docker-ce-cli 
USER jenkins 
RUN jenkins-plugin-cli --plugins "blueocean:1.25.3 docker-workflow:1.28"
