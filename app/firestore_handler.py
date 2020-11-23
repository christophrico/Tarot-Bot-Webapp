from google.cloud import firestore
import os

db = firestore.Client.from_service_account_json('GCPkeys.json')
my_collection = "tarot_bot"


"""
Retrieves all predictions from firestore
Returns a list of predictions names and scores
"""
def get_predictions():
    predictions = db.collection(my_collection) \
                     .order_by('createdAt',direction=firestore.Query.DESCENDING) \
                     .stream()

    prediction_list = []
    for card in predictions:
        prediction_list.append(card.to_dict())

    return prediction_list



"""
Adds the most recent prediction to firestore
args:
prediction: prediction object from google AutoML
"""
def update_database(card, score):
    data = {
        'display_name' : card,
        'score': score,
        'createdAt' : firestore.SERVER_TIMESTAMP
    }
    print(data)
    db.collection(my_collection).add(data)
