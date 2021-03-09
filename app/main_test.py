import main
import unittest
import image_handler as ih
import firestore_handler as fh
from google.cloud import firestore


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        response = self.app.get("/retrieve-predictions")
        self.assertEqual(response.status_code, 200)

    def test_AutoML(self):
        # run a test to see if the predictor returns the correct thing
        file = open("./assets/hermit_1.jpg", "rb")
        hermit, score = ih.request_prediction(file)
        self.assertEqual(hermit, "The Hermit")

    def test_firebase(self):
        # clears the db so we can have a clean slate for testing
        def clear_collection(collection):
            for doc in collection.stream():
                doc.reference.delete()

        # log into firestore
        db = firestore.Client.from_service_account_json("GCPkeys.json")
        # clear the collection
        predictions = db.collection("tarot_bot")
        clear_collection(predictions)
        # add in a test message
        fh.update_database("This is a test", 42)
        # then check it to see if it matches
        test_predicts = fh.get_predictions()
        self.assertEqual("This is a test", test_predicts[0]["display_name"])
        self.assertEqual(42, test_predicts[0]["score"])
        # then clear the collection again.
        clear_collection(predictions)


if __name__ == "__main__":
    unittest.main()
