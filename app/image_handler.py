import json
from google.cloud import automl


# params: file of photo to run inference on
# returns: response.payload from automl client
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictresponse
def request_prediction(file):

    project_id = "241661365506"
    model_id = "IOD6459342741137522688"
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    prediction_client = automl.PredictionServiceClient.from_service_account_json('GCPkeys.json')

    image = automl.Image(image_bytes=file.read())
    payload = automl.ExamplePayload(image=image)
    params = {}

    request = automl.PredictRequest(
        name=name,
        payload=payload,
        params=params
    )
    response = prediction_client.predict(request=request)

    #now translate the prediction
    try:
        if response.payload[0].display_name == "chariot":
            card = "The Chariot"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "death":
            card = "Death"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "devil":
            card = "The Devil"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "emperor":
            card = "The Emperor"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "empress":
            card = "The Empress"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "fool":
            card = "The Fool"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "Fortune":
            card = "Fortune"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "hanged":
            card = "The Hanged Man"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "hermit":
            card = "The Hermit"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "hierophant":
            card = "The Hierophant"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "judgment":
            card = "Judgment"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "justice":
            card = "Justice"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "lovers":
            card = "The Lovers"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "magician":
            card = "The Magician"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "moon":
            card = "The Moon"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "priestess":
            card = "The Priestess"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "star":
            card = "The Star"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "strength":
            card = "Strength"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "sun":
            card = "The Sun"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "temperance":
            card = "Temperance"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "tower":
            card = "The Tower"
            score = round(response.payload[0].image_object_detection.score, 4)
        elif response.payload[0].display_name == "world":
            card = "The World"
            score = round(response.payload[0].image_object_detection.score, 4)
        else:
            card = "Your future is murky. Try another card."
            score = 666
    except:
        card = "Your future is murky. Try another card."
        score = 666

    return card, score
