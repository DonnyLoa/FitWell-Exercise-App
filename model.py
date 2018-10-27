from google.appengine.ext import ndb

class easyAnimals(ndb.Model):
    animal_e_question = ndb.StringProperty(required=True)
    animal_e_correct = ndb.StringProperty(required=True)
    animal_e_wrong = ndb.StringProperty(repeated=True)
