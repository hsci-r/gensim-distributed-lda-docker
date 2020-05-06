FROM python:3.7

RUN pip install --no-cache-dir gensim Pyro4

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

ENV NS_HOST=

COPY dispatcher.py /dispatcher.py

EXPOSE 9100

CMD python /dispatcher.py --ns-host $NS_HOST
