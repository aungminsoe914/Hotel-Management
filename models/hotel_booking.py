    # -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class RoomBooking(models.Model):
    _name = "hotel.booking"
    _description = "Hotel Room Reservation"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # multiple
    _order = 'id desc'



    name = fields.Char(string="Folio Number", 
                        help="Name of Folio",
                        required = True, copy=False,
                        default = 'New', readonly = True)
    customer_name = fields.Many2one('res.partner', string="Customer",
                                 help="Customers of hotel",
                                 required=True )
    date_order = fields.Datetime(string="Order Date",
                                 required=True, copy=False,
                                 help="Creation date of draft/sent orders,"
                                      " Confirmation date of confirmed orders",
                                 default=fields.Datetime.now)
    
    status = fields.Selection(
                            [
                                ('draft','Draft'),
                                ("check_in", "Check In"),
                                ("invoice", "Invoice"),
                                ("check_out", "Check Out"),
                               
                                ("cancel", "Cancel"),
                               
                                ("done", "Done")
                            ],
                                default="draft",
                                string="Status",
                                help="Status of The Room",
                                )

    room_line_ids = fields.One2many("hotel.booking.line",
                                    "booking_id", string="Room",
                                    help="Hotel room reservation detail.")
    
    amount_total = fields.Float(compute = "_compute_amount_total", store = True)

    @api.depends("room_line_ids.price") # id one or more
    def _compute_amount_total(self):
        for booking in self:
            booking.amount_total = sum(lines.price for  lines in booking.room_line_ids)

            # total = 0 # zero
            # for line in booking.room_line_ids:
            #     total += line.price # 0+ 300000 = 300000 + 100000 = 400000
            # booking.amount_total = total
            # total +=booking.room_line_ids.price
            # booking.amount_total = total

            

    @api.model
    def create(self, vals):
        print("values is *********************************************",vals)
        # outpuT******
        #values is ********************************************* 
        # {'name': 'New', 'customer_name': 3, 'date_order': '2025-07-27 07:44:48', 
        # 'room_line_ids': []}

        if vals.get('name', 'New') == 'New':# if New
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.booking') or 'New'
        return super(RoomBooking, self).create(vals)
    
    def action_checkin(self):

        
        for booking in self:
             # write
            # if booking.status == "check_in":

            booking.status = 'check_in'

            for line in booking.room_line_ids: # if 2 lines
                    if line.room_id:
                        # from odoo.exceptions import UserError, ValidationError
# 
                        if line.room_id.status == 'reserved':
                            print(line.room_id.status,'********************************')
                            raise UserError(_(
                                                            "Room is already Reserved",
                                                                    
                                                                ))
                        else:
                            print("Else Condition****************************************")
                            line.room_id.status = 'reserved'

                            #
    
    def action_draft(self):
        print("Clicked drat^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6")
        for booking in self:
            booking.status = 'draft'
            for line in booking.room_line_ids: # if 2 lines
                if line.room_id:
                    line.room_id.status = 'available'

    def action_invoice(self):
        print("****************action Invoice***************************")
        print(self.name,self.customer_name,self.date_order,'Name , customer name , date order')
        print(self.customer_name.id,'This is cus id')

        # insert into(account.move) where
        # self.env['account.move'].create
        #account.move model of field partner_id, move_type, invoice_date
        invoice = self.env['account.move'].create({
            'partner_id':self.customer_name.id, # hotel cus name
            'move_type': 'out_invoice', # customer invoice
            # if vendor bill
            # in_invoice
            'invoice_date': self.date_order, # choose Date
            'invoice_origin' : self.name  # Booking/00001
        })

        for rec in self:
            for booking_line in rec.room_line_ids:
                print("book line name", booking_line.room_id.name)
                print("Booking Room Line Price", booking_line.price)
                print("invoice.id",invoice.id,'***********&&&&&&^^^^^')
                invoice.invoice_line_ids.create([
                    {
                         'name': booking_line['room_id'].name, # line (A101)
                         'price_unit': booking_line['price'], # room price
                         'move_id': invoice.id, # upper assign invoice id
                    }
                ])
        #  for rec in booking_list:
        #         account_move.invoice_line_ids.create([{
        #             'name': rec['name'],
        #             'quantity': rec['quantity'],
        #             'price_unit': rec['price_unit'],
        #             'move_id': account_move.id,
        #             'price_subtotal': rec['quantity'] * rec['price_unit'],
        #             'product_type': rec['product_type'],
        #         }])

       
        
        if invoice:
            print("Success Create Invoice")
            self.status = 'invoice'
        else:
            print("Fail")

    def action_check_out(self):
        self.status = 'check_out'


    def action_print_pdf(self):
        print("**************************")
        #                       model name          . template id(name) 
        #                                               template  ရှိရမယ်
        #self.env.ref ()
        return self.env.ref('hotel_management_system.report_template_name').report_action(self)# docs
    

  
class RoomBookingLine(models.Model):
    
    _name = "hotel.booking.line"
    _description = "Hotel Folio Line"
    booking_id = fields.Many2one("hotel.booking", string="Booking",
                                 help="Indicates the Room",
                                 ondelete="cascade")
    
    room_id = fields.Many2one("hotel.room")
    amenity = fields.Many2one("hotel.amenity")
    price = fields.Float(related = "room_id.free_amount")
    