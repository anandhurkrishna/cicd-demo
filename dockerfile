FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt update && apt install -y curl &&
 pip install -r requirements.txt
EXPOSE 80
HEALTHCHECK --interval=305 --timeout=5s
--retries=3 \
  CMD curl -f http://localhost/ || exit 1

CMD ["python", "app.py"]
