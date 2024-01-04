frappe.ui.form.on('Journal Entry Account', {
    party: function(frm, cdt, cdn) {
        var d = frappe.get_doc(cdt, cdn);
        if (d.party_type && d.party) {
            frappe.call({
                method: "mehta.mehta_group.doctype.journal_entery.journal_entery.get_party_name",
                child: d,
                args: {
                    // company: frm.doc.company,
                    party_type: d.party_type,
                    party: d.party
                },
                callback: function(r) {
                    console.log(r.message);
                    // debugger;
                    if (r.message) {
                        // row.cust_party_name = response.message;
                        // update_jv_details(frm.doc, doc.cust_party_name);
                        frappe.model.set_value(cdt, cdn, 'cust_party_name', r.message);
                    }
                }
            }); 
        }
    }
});



// frappe.ui.form.on('Journal Entry Account', {
//     party: function(frm, cdt, cdn) {
//         var d = frappe.get_doc(cdt, cdn);
//         if (d.party_type && d.party) {

//         }
//     }
// });


// // var update_jv_details = function(doc, r) {
// // 	$.each(r, function(i, d) {
// // 		var row = frappe.model.add_child(doc, "Journal Entry Account", "cust_party_name");
// // 		frappe.model.set_value(row.doctype, row.name, "cust_party_name", "hello")
// // 		// frappe.model.set_value(row.doctype, row.name, "balance", d.balance)
// // 	});
// // 	refresh_field("cust_party_name");
// }






// frappe.ui.form.on('Journal Entry Account', {
//     setup: function(frm, cdt, cdn) {
//         var d = frappe.get_doc(cdt, cdn);
//         if (d.party_type && d.party) {
//             frappe.call({
//                 method: "mehta.mehta_group.doctype.journal_entery.journal_entery.get_party_name",
//                 args: {
//                     company: frm.doc.company,
//                     party_type: d.party_type,
//                     party: d.party
//                 },
//                 callback: function(response) {
//                     console.log(response.message);
//                     // debugger;
//                     if (response.message) {
//                         frappe.model.set_value(cdt, cdn, 'cust_party_name', response.message);
//                     }
//                 }
//             });
//         }
//     }
// });

// frappe.ui.form.on('Journal Entry Account', {
//     party: function(frm, cdt, cdn) {
//         frm.events.party_add_message(frm, cdt, cdn);
//     },
// });
// frappe.ui.form.on('Journal Entry Account', {
//     party: function(frm, cdt, cdn) {
//         frm.events.party_add_message(frm, cdt, cdn);
//     },

//     party_add_message: function(frm, cdt, cdn) {
//         frappe.throw('A row has been added to the links table 🎉');
//     }
// });
