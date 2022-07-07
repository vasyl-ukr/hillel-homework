FROM ubuntu
RUN apt-get update; apt-get install -y python3 python3-pip; rm -rf /var/cache/apt

WORKDIR /flask_app
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]


