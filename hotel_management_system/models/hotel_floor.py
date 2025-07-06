# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelFloor(models.Model):
    
    """Model that holds the Hotel Floors."""

    _name = "hotel.floor" # postgresql Database  Table 
    _description = "Floor"
    

    name = fields.Char(string="Name", help="Name of the floor") 
    manager_name = fields.Char()


