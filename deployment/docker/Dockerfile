# These lines are needed to use the Dockerfile with different dist names: dev, test, live, etc
ARG DIST_NAME
ARG AWS_IMAGES_REGISTRY_BASENAME
ARG FROM_IMAGE="umwrg/hwi-core:${DIST_NAME}"
FROM ${FROM_IMAGE}

LABEL mantainer="giovanni.basolu@manchester.ac.uk"

WORKDIR /app
COPY requirements.txt /app

run pip3 install --upgrade pip

#This gets ignored when in the requirements.txt for some reason.
RUN pip3 install packaging

RUN pip3 install -r requirements.txt

ENV HWI_SETTINGS='/root/.hydra/config/config.py'

CMD ["hydra-api"]
