// message.js

frappe.ui.form.on("Message", {
    validate(frm) {
        if (frm.doc.use_indicator) {
            frappe.msgprint({
                title: "Indicator Check",
                message: "The 'Use Indicator' field is checked.",
                indicator: frm.doc.indicator_color,
                primary_action: {
                    label: "Go to Google",
                    action() {
                        window.open("https://www.google.com", "_blank");
                    }
                }
            });

            frappe.validated = false; // stop form from saving
        }
    }
});
