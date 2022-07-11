FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
COPY bot bot
COPY requirements.txt .
COPY data data
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bot.lambda_enter.handler"]