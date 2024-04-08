FROM python:3.12-slim
WORKDIR /app
COPY app.py requirements.txt RFModel.pkl /app/
COPY templates/index.html /app/templates/
COPY static/css/style.css /app/static/css/
RUN pip install -r requirements.txt
EXPOSE 4000
CMD python ./app.py