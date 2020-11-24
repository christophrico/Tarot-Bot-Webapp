import json
from google.cloud import automl


# params: file of photo to run inference on
# returns: response.payload from automl client
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictresponse
def request_prediction(file):
    #model path
    project_id = "241661365506"
    model_id = "IOD6459342741137522688"
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    prediction_client = automl.PredictionServiceClient.from_service_account_json('GCPkeys.json')

    #open image file and convert to base64
    image = automl.Image(image_bytes=file.read())
    payload = automl.ExamplePayload(image=image)
    params = {}
    request = automl.PredictRequest(
        name=name,
        payload=payload,
        params=params
    )

    #request a prediction
    try:
        response = prediction_client.predict(request=request)
    except:
        card = "The Eye is shut. Please try again later."
        score = 0

    #now translate the prediction to nicer looking text
    try:
        score = round(response.payload[0].image_object_detection.score, 4)
        if response.payload[0].display_name == "chariot":
            card = "The Chariot"
        elif response.payload[0].display_name == "death":
            card = "Death"
        elif response.payload[0].display_name == "devil":
            card = "The Devil"
        elif response.payload[0].display_name == "emperor":
            card = "The Emperor"
        elif response.payload[0].display_name == "empress":
            card = "The Empress"
        elif response.payload[0].display_name == "fool":
            card = "The Fool"
        elif response.payload[0].display_name == "Fortune":
            card = "Fortune"
        elif response.payload[0].display_name == "hanged":
            card = "The Hanged Man"
        elif response.payload[0].display_name == "hermit":
            card = "The Hermit"
        elif response.payload[0].display_name == "hierophant":
            card = "The Hierophant"
        elif response.payload[0].display_name == "judgment":
            card = "Judgment"
        elif response.payload[0].display_name == "justice":
            card = "Justice"
        elif response.payload[0].display_name == "lovers":
            card = "The Lovers"
        elif response.payload[0].display_name == "magician":
            card = "The Magician"
        elif response.payload[0].display_name == "moon":
            card = "The Moon"
        elif response.payload[0].display_name == "priestess":
            card = "The Priestess"
        elif response.payload[0].display_name == "star":
            card = "The Star"
        elif response.payload[0].display_name == "strength":
            card = "Strength"
        elif response.payload[0].display_name == "sun":
            card = "The Sun"
        elif response.payload[0].display_name == "temperance":
            card = "Temperance"
        elif response.payload[0].display_name == "tower":
            card = "The Tower"
        elif response.payload[0].display_name == "world":
            card = "The World"
        else:
            card = "Your future is murky. Try another card."
            score = 666
    except:
        card = "Your future is murky. Try another card."
        score = 666

    return card, score
