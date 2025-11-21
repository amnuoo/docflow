frappe.ui.form.on("Document Request", {
    refresh(frm) {

        if (!frm.doc.name) return;

        // Hide archived rows in the child table
        if (frm.fields_dict.document_version?.grid?.grid_rows) {
            frm.fields_dict.document_version.grid.grid_rows.forEach(row => {
                if (row.doc.archived == 1) {
                    row.wrapper.hide();
                } else {
                    row.wrapper.show();
                }
            });
        }
    }});