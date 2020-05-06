FROM python:3.7-slim

RUN pip install --no-cache-dir gensim Pyro4

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

EXPOSE 9100

CMD python -m gensim.models.lda_worker -p 9100 -v
