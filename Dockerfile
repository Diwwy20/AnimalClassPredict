#
FROM python:3.9

#
WORKDIR /animalclass
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

#
COPY ./requirements.txt /animalclass/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /animalclass/requirements.txt

#
COPY ./app /animalclass/app
COPY ./model /animalclass/model

ENV PYTHONPATH "${PYTHONPATH}:/animalclass"

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]