#
# FROM python:3-onbuild
#
# COPY start.sh /start.sh
#
# # EXPOSE port 8000 to allow communication to/from server
# EXPOSE 8000
#
# # CMD specifcies the command to execute to start the server running.
# CMD ["/start.sh"]
# # done!

######################33
# Starts from the Python image
FROM python:3.12

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# run this command to install all dependencies
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/
COPY start.sh /
# # CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]





