from google.cloud import firestore
import os

db = firestore.Client.from_service_account_json('./GCPkeys.json')
my_collection = "tarot_bot"


"""
Retrieves all predictions from firestore
Returns a list of predictions names and scores
"""
def get_predictions():
    prediction_list = []
    predictions = db.collection(my_collection).stream()

    for card in predictions:
        prediction_list.append(card.to_dict())

    return prediction_list


"""
Adds the most recent prediction to firestore
args:
prediction: prediction object from google AutoML
"""
def update_database(prediction):
    data = {
        'display_name' : prediction.payload[0].display_name,
        'score': "{:.4f}".format(prediction.payload[0].image_object_detection.score)
    }
    print(data)
    db.collection(my_collection).add(data)
