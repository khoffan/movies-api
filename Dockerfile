FROM python:3.8

ENV API_KEY=onVF1xD53e3zL4x68NIJIYytCe4
ENV BASE_DATABASE_URL=mysql+pymysql://naru:546326@192.168.74.207:3312/movies

WORKDIR /app

COPY requirements.txt  /app/

RUN python3 -m pip install --no-cache-dir -r requirements.txt


COPY app /app/

EXPOSE 5001


CMD ["python", "app.py"]
