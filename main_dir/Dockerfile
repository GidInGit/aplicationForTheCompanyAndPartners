FROM python:3.10-slim
COPY reqs.txt /temp/reqs.txt
COPY . /main_dir

WORKDIR main_dir

RUN pip install -r /temp/reqs.txt


CMD uvicorn main:app --host 0.0.0.0 --port 8000
