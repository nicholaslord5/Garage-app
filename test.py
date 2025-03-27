from mech import create_app
from mech.models import Mechanic
from mech.blueprints.mechanics.schemas import mechanics_schema

print("Starting...")
app = create_app()
print("App created")
with app.app_context():
    print("In app context")
    mechanics = Mechanic.query.all()
    print("Mechanics queried:", mechanics)
    result = mechanics_schema.dump(mechanics)
    print("Result:", result)