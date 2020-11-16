#FROM python:3.7-alpine3.9 as base
FROM alpine as base

FROM scratch as user
COPY --from=base . .

RUN apk update \
    && apk add pytest \
    && apk add nmap \
    && apk add tcpdump \
    && apk add openssh \
    && apk add openrc \
    && apk add py3-paramiko \
        bash
USER ${HOST_USER}
WORKDIR /home/${HOST_USER}






