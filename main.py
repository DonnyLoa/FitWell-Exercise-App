import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json
import random
import urlparse
from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SeedPage(BaseHandler):
    def get(self):
         animalsEasyEndPoint = "https://opentdb.com/api.php?amount=30&category=17&difficulty=easy&encode=url3986"



class Cover(BaseHandler):
    def get(self):
        start_template = jinja_env.get_template('templates/index.html')

        category = self.request.get("category")    # Category
        self.session['category'] = category

        difficulty = self.request.get("difficulty")     # Difficulty
        self.session['difficulty'] = difficulty

        self.response.write(start_template.render(difficulty=difficulty,category=category))

    def post(self):
        start_template = jinja_env.get_template('templates/index.html')

        category = self.request.get("category")    # Category
        self.session['category'] = category

        difficulty = self.request.get("difficulty")     # Difficulty
        self.session['difficulty'] = difficulty

        self.response.write(start_template.render(difficulty=difficulty,category=category))
        
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
    ('/', Cover),
    ('/seed-page', SeedPage),
], config=config,
   debug=True)

# Entity employee = new Entity("Employee", "asalieri");
# employee.setProperty("firstName", "Antonio");
# employee.setProperty("lastName", "Salieri");
# employee.setProperty("hireDate", new Date());
# employee.setProperty("attendedHrTraining", true);
#
# DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
# datastore.put(employee);
