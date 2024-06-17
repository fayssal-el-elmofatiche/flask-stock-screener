from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.users import users
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    # select a random user
    user = users[0]

    stocks = [
        {
            'title': 'Hello, World!',
            'body': 'This is a test post.'
        },
        {
            'title': 'How to train your dragon',
            'body': 'Ever wanted to be a hero? Now you can!'
        }
    ]

    return render_template('index.html', title='Home Page', stocks=stocks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not urlsplit(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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