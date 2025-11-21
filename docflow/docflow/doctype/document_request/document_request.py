from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class DocumentRequest(Document):

    def before_insert(self):
        if not self.requested_by:
            self.requested_by = frappe.session.user

    def validate(self):

        new_rows = [v for v in self.document_version if not v.version_no]        