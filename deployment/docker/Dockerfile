# These lines are needed to use the Dockerfile with different dist names: dev, test, live, etc
ARG DIST_NAME
ARG AWS_IMAGES_REGISTRY_BASENAME
ARG FROM_IMAGE="${AWS_IMAGES_REGISTRY_BASENAME}hydra-hwi-step-1:${DIST_NAME}"
FROM ${FROM_IMAGE}

LABEL mantainer="stephen.knox@manchester.ac.uk"

WORKDIR /app

COPY install.sh /app
COPY Pipfile /app
COPY Pipfile.lock /app

#Tell docker to expect these arguments, and make them available to the install.sh script.
ARG SSH_PRIVATE_KEY
ARG SSH_KNOWN_HOSTS
ARG GITLAB_SERVER_IP

RUN chmod 755 install.sh
RUN ./install.sh

# Cleaning file system
#RUN rm ./install.sh
#RUN rm Pipfile
#RUN rm Pipfile.lock

CMD ["hydra-api"]
# Use the following command to hold the container for 3600 seconds instead of running the hydra-server command.
# In this way it is therefore possible to inspect the container
# CMD ["/bin/sleep", "3600"]
