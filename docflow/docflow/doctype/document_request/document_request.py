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

        if new_rows:
             new_row = new_rows[0]

        last_version = max([v.version_no for v in self.document_version if v.version_no], default=0)
        new_row.version_no = last_version + 1

        new_row.uploaded_on = now_datetime()
        new_row.uploaded_by = frappe.session.user

        new_row.is_latest = 1
        new_row.archived = 0
