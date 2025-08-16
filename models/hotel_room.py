# -*- coding: utf-8 -*-

from odoo import fields, models,api


class HotelRoom(models.Model):
    
    """Model that holds the Hotel Rooms."""

    _name = "hotel.room" # postgresql Database  Table 
    _description = "Rooms"
    

    name = fields.Char(string="Room Name", help="Name of the Rooms",required=True) 
    # floor_name =  fields.Char(string="Floor Name")  
    floor_name1 = fields.Many2one("hotel.floor" ,string = "Floor Name")
    # access = fields.Char(help = "This is Hotel Room Of Accessories")
    access = fields.Many2many("hotel.amenity")
    num_person = fields.Integer()

    status = fields.Selection(
                            [
                               ("available", "Available"),
                               ("reserved", "Reserved"),
                               ("occupied", "Occupied")
                            ],
                                default="available",
                                string="Status",
                                help="Status of The Room",
                                )


    
    free_amount = fields.Float(compute ="_compute_fee_amount")

    description = fields.Html()


    @api.depends('num_person')

    def _compute_fee_amount(self):
        for record in self:
                if record.num_person <= 1:
                    record.free_amount = 10000
                elif record.num_person > 1:
                    record.free_amount = 20000
      


