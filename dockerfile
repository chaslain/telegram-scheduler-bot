FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot bot
COPY data data
CMD ["bot.lambda_enter.handler"]