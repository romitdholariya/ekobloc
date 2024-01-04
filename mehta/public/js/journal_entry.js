frappe.ui.form.on('Journal Entry Account', {
    party: function(frm, cdt, cdn) {
        var d = frappe.get_doc(cdt, cdn);
        if (d.party_type && d.party) {
            frappe.call({
                method: "mehta.mehta_group.doc_events.journal_entry.get_party_name",
                args: {
                    company: frm.doc.company,
                    party_type: d.party_type,
                    party: d.party
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.model.set_value(cdt, cdn, 'cust_party_name', r.message);
                    }
                }
            }); 
        }
    }
});
