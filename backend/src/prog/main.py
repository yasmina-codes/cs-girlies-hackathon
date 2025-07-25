from src.prog.config import app, db
from src.prog.route import *


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()  # Temprorary to reset the database on each restart
        db.create_all()

        # Temporary data for proof of concept
        db.session.add(Person("John Doe", "0123456789", "john@example.com"))
        db.session.add(Person("Jane Deer", "9876543210", "jane@example.com"))
        db.session.commit()

    app.run(debug=True)
