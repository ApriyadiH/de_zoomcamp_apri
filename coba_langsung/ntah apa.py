services:
    postgres:
        image: postgres:13
        environment:
            POSTGRES_USER: airflow
            POSTGRES_PASSWORD: airflow
            POSTGRES_DB: airflow
        volumes:
            - postgres-db-volume:/var/lib/postgresql/data 
        healthcheck:
            test: ["CMD", "pg_isready", "-U", "airflow"]
            interval: 5s
            retries: 5  
        restart: always

docker run -it \
    -e POSTGRES_USER="root" \ 
    -e POSTGRES_PASSWORD="unsin0104" \
    -e POSTGRES_DB="ny_taxi" \
    -v c:/Koding/siput/de_zoomcamp_apri/docker/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13