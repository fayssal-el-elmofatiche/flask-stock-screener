from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(80), index=True, unique=True, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True, nullable=False)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    stocks: so.WriteOnlyMapped['StockScreener.stock'] = so.relationship(back_populates='screener')

    def __repr__(self):
        return f"<User('{self.username}')>"
    
class Stock(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    symbol: so.Mapped[str] = so.mapped_column(sa.String(10), index=True, unique=True, nullable=False)
    name: so.Mapped[str] = so.mapped_column(sa.String(100), index=True, nullable=False)

    screeners: so.WriteOnlyMapped['StockScreener.screener'] = so.relationship(back_populates='stock')

    def __repr__(self):
        return f"<Stock('{self.symbol}')>"

class StockScreener(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'), nullable=False)
    stock_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('stock.id'), nullable=False)
    date: so.Mapped[str] = so.mapped_column(sa.String(10), nullable=False)
    price: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    volume: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)

    screener: so.Mapped[User] = so.relationship(back_populates='stocks')
    stock: so.Mapped[Stock] = so.relationship(back_populates='screeners')

    def __repr__(self):
        return f"<StockScreener('{self.stock_id}', '{self.date}', '{self.price}', '{self.volume}')>"
    
    @classmethod
    def get_by_stock(cls, stock_id: int) -> Optional['StockScreener']:
        return cls.query.filter_by(stock_id=stock_id).first()
    
    @classmethod
    def get_by_user(cls, user_id: int) -> Optional['StockScreener']:
        return cls.query.filter_by(user_id=user_id).first()
    
    @classmethod
    def get_by_user_and_stock(cls, user_id: int, stock_id: int) -> Optional['StockScreener']:
        return cls.query.filter_by(user_id=user_id, stock_id=stock_id).first()
    
    @classmethod
    def get_by_user_and_date(cls, user_id: int, date: str) -> Optional['StockScreener']:
        return cls.query.filter_by(user_id=user_id, date=date).first()
    
    @classmethod
    def get_by_user_and_stock_and_date(cls, user_id: int, stock_id: int, date: str) -> Optional['StockScreener']:
        return cls.query.filter_by(user_id=user_id, stock_id=stock_id, date=date).first()
    
