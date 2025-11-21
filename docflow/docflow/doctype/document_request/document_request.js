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

        // Load archived versions in popup
        frappe.call({
            method: "docflow.api.get_archived_versions",
            args: { parent: frm.doc.name },
            freeze: false,
            callback(r) {

                if (!r.message || r.message.length === 0) return;

                frm.add_custom_button("Show Archived Versions", () => {

                    let rows = r.message.map(v => `
                        <tr>
                            <td>${v.version_no}</td>
                            <td>${v.uploaded_on}</td>
                            <td><a href="${v.file}" target="_blank">View</a></td>
                    `).join("");
                    })}});
                }});