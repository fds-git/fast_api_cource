from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

class Hotels(Base):
    __tablename__ = "hotels"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]