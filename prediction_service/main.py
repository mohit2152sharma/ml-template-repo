import logging
from typing import Dict

from fastapi import FastAPI

app = FastAPI()
logging.basicConfig(level=logging.INFO)


@app.get("/predictions")
async def read_sentence(
    clientid: int,
) -> Dict:
    """Takes the clientid and returns the prediction

    Args:
        clientid: user information required for authentication
    Returns:
        A Dictionary with user information and prediction
    """

    # At the moment it is returning a static value
    # but ideally it would call the machine learning model to generate
    # real time predictions or fetch the predictions from database
    response = {
        "user": {
            "username": "monte",
            "display_name": "Mohit Sharma",
            "emailid": "mohitlakshya@gmail.com",
        },
        "prediction": 0.1,
    }
    return response
