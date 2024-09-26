# import boto3
# import uvicorn
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
#
# # FastAPI app initialization
# app = FastAPI()
#
# # AWS credentials and Timestream client initialization
# aws_access_key_id = "AKIAST6S62UA2EXY7CN4"
# aws_secret_access_key = "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"
# aws_region = "ap-southeast-2"
#
# timestream_query = boto3.client(
#     'timestream-query',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )
#
# # Pydantic model for input validation
#
#
# class QueryParams(BaseModel):
#     database_name: str
#     table_name: str
#     query_string: str
#
# # FastAPI route for querying Timestream
#
#
# @app.post("/query-timestream/")
# async def query_timestream(params: QueryParams):
#     # Construct query from provided parameters
#     query_string = params.query_string
#
#     try:
#         # Execute the query
#         result = timestream_query.query(QueryString=query_string)
#
#         # Extract rows from the result
#         rows = result.get('Rows', [])
#         return {"rows": rows}
#
#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"Error executing query: {e}")
#
#
#
#
# # Main entry point
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

import boto3
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel

# FastAPI app initialization
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # Update this with the origin of your HTML page
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
    "*",  # Allow all origins (useful for development, but restrict in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# AWS credentials and Timestream client initialization
aws_access_key_id = "AKIAST6S62UA2EXY7CN4"
aws_secret_access_key = "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"
aws_region = "ap-southeast-2"

timestream_query = boto3.client(
    'timestream-query',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Pydantic model for input validation
class QueryParams(BaseModel):
    database_name: str
    table_name: str
    query_string: str

# FastAPI route for querying Timestream
@app.post("/query-timestream/")
async def query_timestream(params: QueryParams):
    # Construct query from provided parameters
    query_string = params.query_string

    try:
        # Execute the query
        result = timestream_query.query(QueryString=query_string)

        # Extract rows from the result
        rows = result.get('Rows', [])
        return {"rows": rows}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error executing query: {e}"
        )

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
