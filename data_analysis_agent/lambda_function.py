import json
import boto3
import pandas as pd
from io import StringIO

s3_client = boto3.client('s3')

def normalize_and_analyze_stock_data(bucket, input_key):
    # Get the stock data file from S3
    response = s3_client.get_object(Bucket=bucket, Key=input_key)
    file_content = response['Body'].read().decode('utf-8')
    
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(StringIO(file_content))
    
    # Normalize numerical columns (e.g., Open, Close, Volume) using Min-Max Scaling
    for column in ['Open', 'High', 'Low', 'Close', 'Volume']:
        if column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()
            df[column] = (df[column] - min_val) / (max_val - min_val)
    
    # Calculate percentage change in closing prices over 3 months
    df['Performance'] = df.groupby('ticker')['Close'].pct_change(periods=len(df) - 1).fillna(0)

    # Identify the best performer based on the maximum percentage change
    best_performer = df.loc[df['Performance'].idxmax()]['ticker']

    # Save the normalized DataFrame as a CSV back to S3
    output_key = 'normalized_stock_data.csv'
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())

    return {
        "best_performer": best_performer,
        "normalized_data_key": output_key
    }

def lambda_handler(event, context):
    # Extract bucket and key information from the event
    bucket = event['bucket']
    input_key = event['input_key']
    
    # Process the stock data and get the results
    result = normalize_and_analyze_stock_data(bucket, input_key)
    
    # Return the best performer and normalized data file key
    return {
        'statusCode': 200,
        'body': json.dumps({
            'best_performer': result['best_performer'],
            'normalized_data_key': result['normalized_data_key']
        })
    }
