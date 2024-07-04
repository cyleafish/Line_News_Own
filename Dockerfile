FROM python:3.9

# 將專案複製到容器中
COPY . /app
WORKDIR /app

ENV HOST 0.0.0.0

# 安裝必要的套件
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
npm install -g firebase-tools

EXPOSE 8080
CMD uvicorn main:app --host=0.0.0.0 --port=$PORT
