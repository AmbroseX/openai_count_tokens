FROM python:3.9-slim-buster

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update

# 设置工作目录
WORKDIR /app

# 将当前目录下代码复制到镜像内部
COPY requirements.txt /app/

# 安装依赖
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app/

# 设置工作目录和环境变量
WORKDIR /app
ENV PYTHONPATH=/app

EXPOSE 8001
# 启动命令
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8001"]