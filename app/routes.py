from flask import render_template, flash, redirect, url_for
from app import app
from app.users import users
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # select a random user
    user = users[0]

    posts = [
        {
            'title': 'Hello, World!',
            'body': 'This is a test post.'
        },
        {
            'title': 'How to train your dragon',
            'body': 'Ever wanted to be a hero? Now you can!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember me: {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/stocks')
def stocks():
    return "Stocks"

@app.route('/stocks/<ticker>')
def stock(ticker):
    return f"Stock {ticker}"

@app.route('/stocks/<ticker>/history')
def stock_history(ticker):
    return f"Stock {ticker} history"

@app.route('/stocks/<ticker>/history/<date>')
def stock_history_date(ticker, date):
    return f"Stock {ticker} history for {date}"

@app.route('/stocks/<ticker>/history/<date>/<time>')
def stock_history_time(ticker, date, time):
    return f"Stock {ticker} history for {date} at {time}"

@app.route('/stocks/<ticker>/news')
def stock_news(ticker):
    return f"Stock {ticker} news"

@app.route('/stocks/<ticker>/news/<date>')
def stock_news_date(ticker, date):
    return f"Stock {ticker} news for {date}"

@app.route('/stocks/<ticker>/news/<date>/<time>')
def stock_news_time(ticker, date, time):
    return f"Stock {ticker} news for {date} at {time}"  

@app.route('/stocks/<ticker>/quotes')
def stock_quotes(ticker):
    return f"Stock {ticker} quotes"

@app.route('/stocks/<ticker>/quotes/<date>')
def stock_quotes_date(ticker, date):
    return f"Stock {ticker} quotes for {date}"

@app.route('/stocks/<ticker>/quotes/<date>/<time>')
def stock_quotes_time(ticker, date, time):
    return f"Stock {ticker} quotes for {date} at {time}"