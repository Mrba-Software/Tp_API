FROM postgres:12.11

RUN mkdir /sql
COPY ./docker/postgres/sql/plants.psql /sql/plants.psql
COPY ./docker/postgres/sql/seed.sh /docker-entrypoint-initdb.d/seed.sh