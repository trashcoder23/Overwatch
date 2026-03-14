FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements first (for caching)
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY mini_app ./mini_app

# set working dir to backend
WORKDIR /app/mini_app/backend

# expose API port
EXPOSE 8000

# run the service
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
