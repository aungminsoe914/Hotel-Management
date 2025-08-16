# -*- coding: utf-8 -*-
import logging
from odoo import models

_logger = logging.getLogger(__name__)

class RoomBookingInherit(models.Model):
    _inherit = "hotel.booking"

    def action_xls_pdf(self):
        print("****************************")
        """
        Return an action that opens the controller URL which streams the XLSX.
        Works with single record (form) or multiple records (selected in list if invoked by server action).
        """
        # Use comma-separated ids so the controller can generate one file for many bookings
        ids_str = ','.join(map(str, self.ids))
        print("IDS Str is---------------------******************* ",ids_str)
        return {
            'type': 'ir.actions.act_url',
            'url': f'/hotel/booking/xls?ids={ids_str}',
            'target': 'self',
        }
