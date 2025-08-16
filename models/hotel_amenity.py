# -*- coding: utf-8 -*-

from odoo import fields, models


class HotelAmenity(models.Model):
    
    """Model that holds the Hotel Amenity."""

    _name = "hotel.amenity" # postgresql Database  Table 
    _description = "Amenity"
    

    name = fields.Char(string="Amenity Name", help="Name of the Amenity",required=True) 
    #wifi 
    description = fields.Char()
    # 5G Internet wifi


