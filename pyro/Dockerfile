FROM python:3.7

RUN pip install --no-cache-dir Pyro4

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

EXPOSE 9090

CMD python -m Pyro4.naming -n 0.0.0.0
