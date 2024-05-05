import boto3

def list_lambda_functions_in_all_regions():
    # Create a boto3 client for Lambda
    lambda_client = boto3.client('lambda')

    # Get all AWS regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        print(f"Checking Lambda functions in region: {region}")
        lambda_client = boto3.client('lambda', region_name=region)
        response = lambda_client.list_functions()

        # Check if there are Lambda functions in this region
        if 'Functions' in response:
            for function in response['Functions']:
                print(f"  Function Name: {function['FunctionName']}")
        else:
            print("  No Lambda functions found in this region.")

if __name__ == "__main__":
    list_lambda_functions_in_all_regions()
