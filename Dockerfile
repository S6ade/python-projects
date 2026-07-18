FROM python:3.14-slim
WORKDIR /app
RUN apt-get update && apt-get upgrade -y
COPY api.py /app/
RUN pip install fastapi uvicorn
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000" ]