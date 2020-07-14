# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import re

class AccountMoveLineInherited(models.Model):
    _inherit = "account.invoice.line"

    project_id = fields.Many2one('project.project', string='Basic Items')
    task_id = fields.Many2one('project.task', string="Sub Item", domain="[('project_id','=',project_id)]")
    description = fields.Char(string="Description")
    previousely_worked = fields.Integer(string="Previousely Worked")
    current_work = fields.Integer(string="Current Work")
    contracting_rate = fields.Integer(string="Contracting Rate")
    completion_rate = fields.Integer(string="Completion Rate")

    #override required constraint
    name = fields.Text(string='Description', required=False)

    @api.onchange('previousely_worked','current_work')
    def _calculate_total_work(self):
        for rec in self:
            if rec.previousely_worked or rec.current_work:
                x = rec.previousely_worked + rec.current_work
                print(x)
                rec.quantity = x



    @api.onchange('task_id')
    def _onchange_task_id(self):
        for line in self:
            line._get_computed_description()

    def _get_computed_description(self):
        self.ensure_one()

        clean = re.compile('<.*?>')
        task = self.task_id
        if task.description:
            self.description = re.sub(clean, '', task.description)

    

    


    


 