FROM python:3.7-slim

RUN pip install gensim Pyro4

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

CMD python -m gensim.models.lda_worker

