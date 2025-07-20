# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelCustomer(models.Model):
    
    """Model that holds the Hotel Customer."""

    _name = "hotel.customer" 
    _description = "Customer(Partner)"
    

    name = fields.Char(string="Customer Name", help="Name of the Customer",required=True) 
    
    icon = fields.Image(string="Icon")

    nrc = fields.Char()
    phone = fields.Char()
    email  = fields.Char()
    address = fields.Char()