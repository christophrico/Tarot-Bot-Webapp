from google.cloud import automl

# params: file of photo to run inference on
# returns: response.payload from automl client
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictresponse


def getPrediction(file):
    #fill these in!!!
    project_id = ""
    model_id = ""

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(
                    project_id,
                    "us-central1", #this may need to change
                    model_id
    )
    content = file.read():

    image = automl.Image(image_bytes=content)
    payload = automl.ExamplePayload(image=image)

    # params is additional domain-specific parameters.
    # score_threshold is used to filter the result
    # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
    params = {"score_threshold" : "0.8"}

    request = automl.PredictRequest(
            name=model_full_id,
            payload=payload,
            params=params
    )

    response = predicton_client.predict(request=request)

    return response.payload
