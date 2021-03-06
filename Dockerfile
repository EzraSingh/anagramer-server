FROM python:3-alpine

ENV PORT 5001

RUN mkdir -p /src

ADD requirements.txt /
ADD src /src

# Pull raw english dictiornary and place in /src
RUN wget https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt -P /src/ -O en-us.dict

RUN pip install -r requirements.txt

WORKDIR /src

CMD [ "python", "server.py" ]