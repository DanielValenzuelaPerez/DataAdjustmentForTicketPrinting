"""
MAIN

ticket_formatter = TicketFormatter(width=40, size=12)
formatted_ticket = ticket_formatter.format(data)
return formatted_ticket

TICKET SPACE CONFIGURATION

Header & Footer
<80% of width>
Articles
<-6--><-remaining-width-><---10--->

FORMAT

"""


class TicketFormatter:

    def __init__(self, width, size):
        self.width=width
        self.size=size
    
    def header_footer_format(self, data):
        lines = list()
        business = data['ticket']['business']
        branch = data['ticket']['branch']
        # Business name
        lines.append(dict())
        # RFC
        # Branch name & ID
        # Branch Address

    def items_format(self):
        pass

    def payment_format(self):
        pass

    def _format_text(self, text_list, header):
        pass

def create_ticket_json(pos_order):
    ticket_formatter = TicketFormatter(40)
    header_lines = ticket_formatter.header_footer_format(pos_order)

def main():
    pos_order_1 = dict(
        id=1,
        items=[
            dict(
                id=1,
                presentation=dict(name='24 pack'),
                model=dict(
                    name='Modelo Ámbar',
                    product=dict(name='Cerveza Modelo')
                ),
                qty=1,
                price="480.00",
                total="480.00",
                date_created="2022-11-25T01:07:01.980359Z"
            )
        ],
        user=dict(
            first_name='Yosi',
            last_name='Dey'
        ),
        discount=None,
        pay_split=[
            dict(
                type=1,
                amount="480.00"
            )
        ],
        total="480.00",
        subtotal="480.00",
        iva="0.00",
        date_created="2022-11-25T01:07:01.915816Z",
        ticket=dict(
            branch=dict(
                id=1,
                name='Tecuala La Orgullosa',
                address=None
            ),
            business=dict(
                rfc=None,
                name='Panadería la Mejor'
            ),
            footnote=None
        )
    )
    create_ticket_json(pos_order_1)

if __name__ == '__main__':
    main()
