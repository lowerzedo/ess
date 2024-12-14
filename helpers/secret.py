import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()



def get_secret():
    if os.environ.get('DB_SECRET'):
        secret_name = os.environ.get('DB_SECRET')
        region_name = "ap-southeast-1"

        session = boto3.session.Session()
        
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

        # Parse the main JSON object
        secret = json.loads(get_secret_value_response['SecretString'])
        
        # Parse the nested JSON string within DB_URI
        db_uri = json.loads(secret['DB_URI'])

        gims_db = db_uri['GIMS_W']

        return gims_db
    else:
        mssql_db = os.environ.get('MSSQL_DB')
        api_key = os.environ.get('API_KEY')

        print(f"mssql_db: {mssql_db}")

        return mssql_db, api_key