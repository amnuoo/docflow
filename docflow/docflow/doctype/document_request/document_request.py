from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class DocumentRequest(Document):

    def before_insert(self):
        if not self.requested_by:
            self.requested_by = frappe.session.user