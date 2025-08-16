# -*- coding: utf-8 -*-
import io
import xlsxwriter
from odoo import http
from odoo.http import request, content_disposition


# class BookingReportControllerOne(http.Controller):

#     @http.route('/hotel/booking/one/xls', type='http', auth='user')
#     def booking_xls_one(self, ids=None, **kwargs):
#         return True

    # def my_function(**kwargs):
    # # def my_function(name,age,city):
    #     for key, value in kwargs.items():
    #         print(f"{key}: {value}")

    # my_function(name="Alice", age=30, city="New York")




















class BookingReportController(http.Controller):

    @http.route('/hotel/booking/xls', type='http', auth='user')
    def booking_xls(self, ids=None, **kwargs):
        # ** argument assign accept
        """
        /hotel/booking/xls?ids=1,2,3
        Generates an XLSX with:
          - Booking name
          - Customer name
          - Table of room_line_ids: Room, Amenity, Price
        """
        # print(self.id, **kwargs)
        # return True
        
        if not ids:
            return request.not_found()

        try:
            id_list = [
                            int(x) for x in ids.split(',') if x.strip()
                       ]
            print("********************",id_list) # [21]
            #  ORM 
            #  search
            #  browse  ==> 
        except Exception:
            return request.not_found()
        
        # return True

        bookings = request.env['hotel.booking'].browse(id_list).sudo()
        if not bookings:
            return request.not_found()
        # return bookings

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Bookings')

        # Formats
        fmt_bold = workbook.add_format({'bold': True,'color': "#168BB9"})
        fmt_header = workbook.add_format({'bold': True, 'bg_color': "#E60808"})
        fmt_money = workbook.add_format({'num_format': '#,##0.00'})

        row = 0
        for booking in bookings:
            # Booking name / Customer
            sheet.write(row, 0, 'Booking:', fmt_bold)
            #          0,0
            sheet.write(row, 1, booking.name or '')
            row += 1  # 1
            sheet.write(row, 0, 'Customer:', fmt_bold)
            cust_name = booking.customer_name.name if booking.customer_name else ''
            sheet.write(row, 1, cust_name)
            row += 1 # 2

            # Blank row
            row += 1 # 3

            # Room lines header
            headers = ['Room', 'Amenity', 'Price']
            #
            for col, h in enumerate(headers):
                #col,h
                # 0:Room
                # 1:Amenity
                # 2:Price
                #           3,0   h = ? Room
                #           3,1   h = ? Amenity
                #           3,2   h = ? Price   
                sheet.write(row, col, h, fmt_header)
            row += 1  # 4

            # Room lines
            if booking.room_line_ids:
                for line in booking.room_line_ids:
                    room_name = line.room_id.name if line.room_id else ''
                    amenity = line.amenity.name if line.amenity else ''
                    price = line.price or 0.0

                    #room_name = A101
                    #amenity = Aircon
                    # price = 100000
                    #           4,0  , A101
                    #           4,1 , Aircon
                    #write_number4,2 , 100000
                    sheet.write(row, 0, room_name)
                    sheet.write(row, 1, amenity)
                    sheet.write_number(row, 2, price, fmt_money)
                    row += 1
            else:
                sheet.write(row, 0, '--- No rooms ---')
                row += 1

            # Spacer between bookings
            row += 2

        workbook.close() # close and buffer
        output.seek(0) # buffer byte code 
        xls_data = output.read() # read 
        output.close() 

        filename = 'booking_report.xlsx' if len(id_list) > 1 else f'booking_{bookings[0].name or id_list[0]}.xlsx'
        return request.make_response(
            xls_data,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', content_disposition(filename))
            ]
        )
