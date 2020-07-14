# -*- coding: utf-8 -*-
# from odoo import http


# class VendorBillChanges(http.Controller):
#     @http.route('/vendor_bill_changes/vendor_bill_changes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vendor_bill_changes/vendor_bill_changes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vendor_bill_changes.listing', {
#             'root': '/vendor_bill_changes/vendor_bill_changes',
#             'objects': http.request.env['vendor_bill_changes.vendor_bill_changes'].search([]),
#         })

#     @http.route('/vendor_bill_changes/vendor_bill_changes/objects/<model("vendor_bill_changes.vendor_bill_changes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vendor_bill_changes.object', {
#             'object': obj
#         })
