FROM "amazon/aws-lambda-python"


WORKDIR "/var/task"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY data2 data2
COPY bot bot
CMD ["bot.lambda_enter.handler"]