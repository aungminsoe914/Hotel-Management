# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelFloor(models.Model):
    
    """Model that holds the Hotel Floors."""

    _name = "hotel.floor" # postgresql Database  Table 
    _description = "Floor"
    

    name = fields.Char(string="Name", help="Name of the floor",required=True) 
    # manager_name = fields.Char()
    manager_name = fields.Many2one('res.users')


