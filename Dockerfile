FROM python:3

RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8889
CMD jupyter notebook --ip 0.0.0.0 --port 8889 --no-browser --allow-root