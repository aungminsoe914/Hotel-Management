# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelCustomer(models.Model):
    
    """Model that holds the Hotel Customer."""

    _name = "hotel.customer" 
    _inherit = ['mail.thread', 'mail.activity.mixin']  # multiple inherit
    _description = "Customer(Partner)"
    

    name = fields.Char(string="Customer Name", help="Name of the Customer",required=True, tracking = True) 
    
    icon = fields.Image(string="Icon")

    nrc = fields.Char(tracking = True)
    phone = fields.Char(tracking = True)
    email  = fields.Char(tracking = True)
    address = fields.Char()
    
    active=fields.Boolean(default=True)