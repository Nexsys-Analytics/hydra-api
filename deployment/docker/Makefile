NAME	:= hydra-api
TAG	:= $$(git rev-parse --short=8 HEAD)
IMG	:= ${NAME}:${TAG}
LATEST	:= ${NAME}:${DIST_NAME}

build:
	@echo ${DIST_NAME}
	@docker build --build-arg DIST_NAME=${DIST_NAME} --no-cache -t ${IMG} .
	@docker tag ${IMG} ${LATEST}
