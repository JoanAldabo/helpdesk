from odoo import fields, models, api, _


class HelpdeskTicket (models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project')
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task')

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False

    @api.onchange('project_id')
    def _onchange_project_id(self):
        return {} \
            if not self.project_id \
            else \
            {'domain': {'task_id': [('project_id', '=', self.project_id.id)]}}
