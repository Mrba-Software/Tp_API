FROM python:3.10.6-slim as deps
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --user -r requirements.txt

# using a minimal image to optimize build
FROM python:3.10.6-slim
WORKDIR /usr/src/app
COPY . .
COPY --from=deps /root/.local /root/.local
ENV PATH="${PATH}:/root/.local/bin"
ENV FLASK_APP=flaskr
# watch app' files
ENV FLASK_DEBUG=True
ENV FLASK_ENV=development

# running Flask as a module
CMD ["sh", "-c", "sleep 5 \ 
    && python -m flask run --host=0.0.0.0"]