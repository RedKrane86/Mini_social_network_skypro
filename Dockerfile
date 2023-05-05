FROM python:3.10-slim

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]
