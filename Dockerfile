FROM alpine:3.20

WORKDIR /workdir

COPY ./ ./

RUN apk add python3 py3-pip \
  && pip3 install --break-system-packages -r requirements.txt
CMD [ "run.sh" ]