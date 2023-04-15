FROM wonghongtou/forkingdog:latest
COPY ./func/ ./app/func/
RUN pip install -r ./app/func/requirements.txt
ENV ARGS '["python", "./app/func/get-macau-weather.py"]'