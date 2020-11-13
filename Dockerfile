FROM alpine as base

FROM scratch as user
COPY --from=base . .
RUN apk update \
    && apk add python3 \
    && apk add pytest \
        bash
USER ${HOST_USER}
WORKDIR /home/${HOST_USER}
