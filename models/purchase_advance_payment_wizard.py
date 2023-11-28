from odoo import _, api, exceptions, fields, models


class AccountVoucherWizardPurchase(models.TransientModel):
    _inherit = "account.voucher.wizard.purchase"

    def _prepare_payment_vals(self, purchase):
        res = super(AccountVoucherWizardPurchase, self)._prepare_payment_vals(purchase)
        account_id = purchase.company_id.advance_payment_outgoing_account_id.id
        res.update({'is_advance_payment':True,
                    'advance_payment_account_id':account_id})
        return res
    
class AccountVoucherWizard(models.TransientModel):
    _inherit = "account.voucher.wizard"

    def _prepare_payment_vals(self, sale):
        res = super(AccountVoucherWizard, self)._prepare_payment_vals(sale)
        account_id = sale.company_id.advance_payment_account_id.id
        res.update({'is_advance_payment':True,
                    'advance_payment_account_id':account_id})
        return res

