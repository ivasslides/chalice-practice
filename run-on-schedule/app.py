from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')


instance_id = "xxxxyyyyzzzz" 


# cron is how to set the timing for it
@app.schedule('cron(0 8 * *)')
def daily_task():
    # your code to execute every day at 8am
    print("Turning off EC2 instance")
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(instance_id) 
