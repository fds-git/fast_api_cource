from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON, ForeignKey, Date, Computed

class Bookings(Base):
    __tablename__ = "bookings"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    fate_from: Mapped[Date] = mapped_column(nullable=False)
    fate_to: Mapped[Date] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))
