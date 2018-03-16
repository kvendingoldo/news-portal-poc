FROM django

COPY ./python/ /news-portal
WORKDIR /news-portal
EXPOSE 8000
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "manage.py runserver 0.0.0.0:8000" ]
