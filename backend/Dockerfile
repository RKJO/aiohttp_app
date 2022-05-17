FROM python:3.8.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
# CMD python -m aiohttp.web -H localhost -P 8080 main.py
CMD python main.py
