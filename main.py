from flask import Flask, render_template, request
# import webapp2
# import jinja2
# import os
# from google.appengine.api import urlfetch
# import json
# import random
# import urlparse
# from webapp2_extras import sessions
#
# class BaseHandler(webapp2.RequestHandler):
#     def dispatch(self):
#         # Get a session store for this request.
#         self.session_store = sessions.get_store(request=self.request)
#
#         try:
#             # Dispatch the request.
#             webapp2.RequestHandler.dispatch(self)
#         finally:
#             # Save all sessions.
#             self.session_store.save_sessions(self.response)
#
#     @webapp2.cached_property
#     def session(self):
#         # Returns a session using the default cookie key.
#         return self.session_store.get_session()
#
# jinja_env = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True)
#
# class SeedPage(BaseHandler):
#     def get(self):
#          animalsEasyEndPoint = "https://opentdb.com/api.php?amount=30&category=17&difficulty=easy&encode=url3986"
#          # exerciseCategory =
#          # exerciseLength =
#
#          a_e_response = urlfetch.fetch(animalsEasyEndPoint).content
#          print a_e_response
#          json_a_e_response = json.loads(a_e_response)
#          a_e_results = json_a_e_response["results"]
#          for a in a_e_results:
#             aeqp = urlparse.unquote(a["question"])
#             aecp = urlparse.unquote(a["correct_answer"])
#             aewplist = []
#             # for x in a["incorrect_answers"]:
#             #    aewp = urlparse.unquote(x)
#             #    aewplist.append(aewp)
#             a_e_question = easyAnimals(
#                animal_e_question = aeqp,
#                animal_e_correct = aecp,
#                animal_e_wrong = aewplist)
#             a_e_question.put()
#
#
# class Cover(BaseHandler):
#     def get(self):
#         start_template = jinja_env.get_template('templates/index.html')
#
#         category = self.request.get("category")    # Category
#         self.session['category'] = category
#
#         difficulty = self.request.get("difficulty")     # Difficulty
#         self.session['difficulty'] = difficulty
#
#         self.response.write(start_template.render(difficulty=difficulty,category=category))
#
#     def post(self):
#         start_template = jinja_env.get_template('templates/index.html')
#
#         category = self.request.get("category")    # Category
#         self.session['category'] = category
#
#         difficulty = self.request.get("difficulty")     # Difficulty
#         self.session['difficulty'] = difficulty
#
#         self.response.write(start_template.render(difficulty=difficulty,category=category))
#
# config = {}
# config['webapp2_extras.sessions'] = {
#     'secret_key': 'my-super-secret-key',
# }
#
# app = webapp2.WSGIApplication([
#     ('/', Cover),
#     ('/seed-page', SeedPage),
# ], config=config,
#    debug=True)

app = Flask(__name__)
@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'index.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

@app.route('/submitted', methods=['GET'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'exercise_results.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

# Entity employee = new Entity("Employee", "asalieri");
# employee.setProperty("firstName", "Antonio");
# employee.setProperty("lastName", "Salieri");
# employee.setProperty("hireDate", new Date());
# employee.setProperty("attendedHrTraining", true);
#
# DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
# datastore.put(employee);
