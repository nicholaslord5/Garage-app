from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from mech.models import Customer
from mech.extensions import ma

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        fields = ('id', 'email', 'phone')
        load_instance = False
        include_fk = True

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)