FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /src

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /src/app

COPY ./frontend /src/frontend

CMD ["streamlit", "run", "frontend/app.py"]