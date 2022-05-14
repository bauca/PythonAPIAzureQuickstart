# For the sake of simplicity, we are setting up a 'fat' image, no separation of dev/runtime images
FROM python:3.10.4-slim-bullseye

RUN mkdir backend
WORKDIR /backend
COPY . /backend
RUN pip install poetry
RUN poetry install 
EXPOSE 80
ENTRYPOINT ["poetry","run","uvicorn","api.main_api:app","--host","0.0.0.0", "--port", "80"]