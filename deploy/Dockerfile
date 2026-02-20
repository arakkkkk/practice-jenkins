FROM jenkins/jenkins:lts-jdk17

USER root
COPY scripts/install-docker-in-image.sh /usr/local/bin/install-docker-in-image.sh
RUN chmod +x /usr/local/bin/install-docker-in-image.sh \
    && /usr/local/bin/install-docker-in-image.sh \
    && rm -f /usr/local/bin/install-docker-in-image.sh

USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
