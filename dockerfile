FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
RUN pip install --no-cache-dir -r requirements.txt

COPY bot .
CMD ["lambda_enter.handler"]