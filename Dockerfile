# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8008
CMD ["python", "daily_crawl.py"]
