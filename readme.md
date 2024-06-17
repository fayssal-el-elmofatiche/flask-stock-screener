# Flask Stock Screener

A simple stock screener built with Flask. It's a work in progress. This is based on the Mega Flask tutorial from [Flask Mega Tutorial](https://github.com/miguelgrinberg/mega-flask-tutorial).

## Differences from the tutorial

- The stock screener adapts the tutorial from microblogging to stock screening.
- Instead of pip, we use poetry to manage dependencies.

## Installation

```
$ git clone https://github.com/jmcarp/flask-stock-screener.git
$ cd flask-stock-screener
$ poetry install    
```

## Usage

```
$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


# Hightlighted libraries used
- Flask - For web framework
- Flask-SQLAlchemy - For database access
- Flask-Migrate - For database migrations
- Flask-WTF (you read that right!) - For forms
- Werkzeug - For password hashing
- Flask-Login - For user authentication
- Email-validator - For email validation


# Useful tools used in this project
- [WWW SQL Designer](https://sql.toad.cz/)
- [DB Visualizer](https://dbvis.com/)
