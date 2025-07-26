    # -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class RoomBooking(models.Model):
    _name = "hotel.booking"
    _description = "Hotel Room Reservation"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # multiple
    _order = 'id desc'
    name = fields.Char(string="Folio Number", 
                        help="Name of Folio")
    customer_name = fields.Many2one('res.partner', string="Customer",
                                 help="Customers of hotel",
                                 required=True )
    date_order = fields.Datetime(string="Order Date",
                                 required=True, copy=False,
                                 help="Creation date of draft/sent orders,"
                                      " Confirmation date of confirmed orders",
                                 default=fields.Datetime.now)
    room_line_ids = fields.One2many("hotel.booking.line",
                                    "booking_id", string="Room",
                                    help="Hotel room reservation detail.")
    
class RoomBookingLine(models.Model):
    
    _name = "hotel.booking.line"
    _description = "Hotel Folio Line"
    booking_id = fields.Many2one("hotel.booking", string="Booking",
                                 help="Indicates the Room",
                                 ondelete="cascade")
    
    room_id = fields.Many2one("hotel.room")
    amenity = fields.Many2one("hotel.amenity")
    