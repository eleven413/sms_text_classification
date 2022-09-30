FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /src

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /src/app

COPY ./frontend /src/frontend

RUN mkdir -p ~/.streamlit/

ENV PORT=80

# RUN echo "\
# [server]\n\
# headless = true\n\
# port = $PORT\n\
# enableCORS = false\n\
# \n\
# " > ~/.streamlit/config.toml

COPY ./config.toml ~/.streamlit/

CMD ["streamlit", "run", "frontend/app.py"]