FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
RUN pip install --no-cache-dir -r requirements.txt


CMD ["lambda_enter.handler"]