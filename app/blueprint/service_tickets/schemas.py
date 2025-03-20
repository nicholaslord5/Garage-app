from app.models import ServiceTicket
from app.extensions import ma

class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        fields = ('id', 'vin', 'service_date', 'service_desc', 'customer_id')

ticket_schema = ServiceTicketSchema()
tickets_schema = ServiceTicketSchema(many=True)