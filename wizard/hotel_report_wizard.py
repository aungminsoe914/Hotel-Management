# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HotelReportWizard(models.TransientModel):
    _name = "hotel.report.wizard"
    _description = "Hotel Booking Report Wizard"

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    '''
      start date, end date ကို ရပြီး
      self.env['hotel.booking'] ထဲမှာရှိတဲ့ date_order ဆိုတဲ့   field  က user ထည့်လိုက်တဲ့
      data date နဲ့ စစ်တာ . search
    
    '''
    def action_print_report(self):
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'booking_ids': self._get_booking_data(),
        }
        print("data is ************************8",data['booking_ids'])
        for i in data['booking_ids']:
            print(i,'This is booking id *************8')
        # return self.env.ref('hotel_management_system.report_hotel_booking').report_action(self, data=data)

    def _get_booking_data(self):

        bookings = self.env['hotel.booking'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date),
        ])
        for i in bookings:
            print(i.name, i.id, i.customer_name,'*********************')
        return bookings.ids