FROM python:3.7-slim

RUN pip install --no-cache-dir gensim Pyro4

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

EXPOSE 9090

EXPOSE 9091

EXPOSE 9100

CMD python -m Pyro4.naming -n 0.0.0.0 & python -m gensim.models.lda_dispatcher -p 9100 -v 
