# base image
FROM python:3.9 
# a small linux based os also gets installed along with python

# work dir
WORKDIR /app

# copy -> copy all files to WORKDIR
COPY . /app

# run 
RUN pip install -r requirements.txt

# port
EXPOSE 5000 
# flask applications generally use port 5000

# command to execute the file
CMD ["python", "./app.py"]