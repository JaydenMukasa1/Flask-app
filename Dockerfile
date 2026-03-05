FROM python:3.12.4
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]
