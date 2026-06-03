frappe.ui.form.on('Customer', {
    refresh(frm) {
        frm.add_custom_button('Send SMS', () => {
            frappe.call({
                method: 'sms_integration.sms_integration.doctype.twilio_settings.twilio_settings.send_customer_sms',
                args: {
                    customer: frm.doc.name
                },
                callback(r) {
                    frappe.msgprint(__('SMS Sent'));
                }
            });
        });
    }
});