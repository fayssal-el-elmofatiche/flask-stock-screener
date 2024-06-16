import sqlalchemy as sa
import sqlalchemy.orm as so 
from app import app, db
from app.models import User, Stock, StockScreener

@app.shell_context_processor
def make_shell_context():
    return {
        'sa': sa,
        'db': db,
        'so': so,
        'User': User,
        'Stock': Stock,
        'StockScreener': StockScreener
    }