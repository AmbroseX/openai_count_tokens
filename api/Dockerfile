FROM python:3.9-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录下代码复制到镜像内部
COPY ./app/requirements.txt /app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# 启动命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]