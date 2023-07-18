FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 manage.py makemigrations

CMD bash -c "sleep 30 && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
