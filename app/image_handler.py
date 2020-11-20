from google.cloud import automl
from io import BufferedReader

# params: file of photo to run inference on
# returns: response.payload from automl client
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictresponse


def get_prediction(file):

    project_id = "241661365506"
    model_id = "IOD6459342741137522688"
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    prediction_client = automl.PredictionServiceClient()

    image = automl.Image(image_bytes=file.read())
    payload = automl.ExamplePayload(image=image)
    params = {}

    request = automl.PredictRequest(
        name=name,
        payload=payload,
        params=params
    )

    response = prediction_client.predict(request=request)

    return response.payload
