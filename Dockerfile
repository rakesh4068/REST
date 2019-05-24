FROM python:2.7
ADD my_script.py /
RUN pip install requests
CMD [ "python", "./my_script.py" ]
