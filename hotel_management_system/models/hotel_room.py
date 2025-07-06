# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelRoom(models.Model):
    
    """Model that holds the Hotel Rooms."""

    _name = "hotel.room" # postgresql Database  Table 
    _description = "Rooms"
    

    name = fields.Char(string="Room Name", help="Name of the Rooms") 
    floor_name =  fields.Char(string="Floor Name")
    access = fields.Char()
    num_person = fields.Integer()
    


