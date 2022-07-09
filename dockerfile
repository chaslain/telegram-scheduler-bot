FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
COPY bot .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bot.lambda_enter.handler"]