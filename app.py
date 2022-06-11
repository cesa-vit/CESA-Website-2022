# importing libraries
from flask import Flask,redirect,url_for,request,render_template,session
from flask_mail import Mail, Message
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from Flask-Ext import Mail
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class



app = Flask(__name__)
# english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
# Create a new instance of a ChatBot
english_bot = ChatBot(
    "Chatterbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.50
        }
    ]
)
trainer = ChatterBotCorpusTrainer(english_bot, show_training_progress=False)
trainer.train("chatterbot.corpus.english")
trainer.train("data/convo-data.yml")


# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'feedbackcesa@gmail.com'
app.config['MAIL_PASSWORD'] = 'feedbackcesa@321'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        if name=='' or email=='' or subject=='':
            return render_template('index.html',message='Please enter required fields')
        msg = Message(
                subject,
                sender ='yourId@gmail.com',
                recipients = ['cesa.vidyalankar@gmail.com']
               )
        msg.body = 'Name:'+ name + '\n' + 'Email: ' + email + '\n' 'Message:\n' + message
        # msg = Message(subject, sender = email, recipients = ['cesa.vidyalankar@gmail.com'])
        # msg.body = message
        mail.send(msg)
        return render_template('index.html')
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(english_bot.get_response(userText))

@app.route('/events')
def events():
	return render_template('event.html')

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/articles')
def articles():
	return render_template('articlespage.html')


@app.route('/article_1')
def article_1():
	return render_template('article__1.html')

@app.route('/article_2')
def article_2():
	return render_template('article__2.html')
@app.route('/article_3')
def article_3():
	return render_template('article__3.html')
@app.route('/article_4')
def article_4():
	return render_template('article__4.html')
@app.route('/article_5')
def article_5():
	return render_template('article__5.html')
@app.route('/article_6')
def article_6():
	return render_template('article__6.html')




if __name__ == '__main__':
	app.run(debug=True)
