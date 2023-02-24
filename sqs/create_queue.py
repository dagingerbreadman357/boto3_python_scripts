import boto3

sqs = boto3.client('sqs')           # creates sqs client variable

queue = sqs.create_queue(
    QueueName='KingSQS_Time'        # creates a queue and names it KingSQS_Time
)

print('Queue created', queue.url)   # print url of queue
