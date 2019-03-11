#!python
import boto3
from botocore.exceptions import ClientError
from argparse import ArgumentParser


def stack_exists(client, stack_name):
    cfn_stacks = client.list_stacks()
    for cfn_stack in cfn_stacks["StackSummaries"]:
        if cfn_stack['StackName'] == stack_name and "COMPLETE" in cfn_stack['StackStatus'] and "DELETE" not in cfn_stack['StackStatus']:
            return True
    return False

def stack_operations(client, stack_name, template, ssh_key_name, operation):
    if operation == "create":
        with open(template, 'r') as cfn_template:
            return client.create_stack(StackName=stack_name,
                                       TemplateBody=cfn_template.read(),
                                       Parameters=[
                                           {
                                                'ParameterKey': 'keyName',
                                                'ParameterValue': ssh_key_name,
                                           }
                                        ])
    elif operation == "update":
        with open(template, 'r') as cfn_template:
            try:
                return client.update_stack(StackName=stack_name,
                                           TemplateBody=cfn_template.read(),
                                           Parameters=[
                                           {
                                                'ParameterKey': 'keyName',
                                                'ParameterValue': ssh_key_name,
                                           }
                                        ])
            except ClientError as e:
                print ("[Skipping stack update] {0}".format(e))
    else:
        print("Unknown operation {0}".format(operation))
        exit(1)

def get_arguments():
    parser = ArgumentParser(description='Check stack exists')
    parser.add_argument('--stack-name', help='CFn stack name', required=True)
    parser.add_argument('--template', help='CloudFormation template', required=True)
    parser.add_argument('--ssh-key-name', help='ECS Cluster SSH key name', required=True)
    return parser.parse_args()

def main():
    args = get_arguments()
    client = boto3.client('cloudformation')
    if stack_exists(client, args.stack_name):
        status = stack_operations(client, args.stack_name, args.template, args.ssh_key_name, operation="update")
    else:
        status = stack_operations(client, args.stack_name, args.template, args.ssh_key_name, operation="create")
    print (status)
        

if __name__ == "__main__":
    main()