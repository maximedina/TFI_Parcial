# -*- coding: utf-8 -*-

from itertools import groupby
from datetime import datetime, timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang



class Evaluation(models.Model):
    _name = 'veterinary.evaluation'
    _inherit = ['mail.thread']

    @api.multi
    def default_stage(self):
        return self.env['veterinary.evaluation.stages'].search([('name','=','New')])
    
    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['veterinary.evaluation.stages'].search([])
        return stage_ids
    
    name =fields.Char('Name',compute='_compute_name')
    animal = fields.Many2one('veterinary.animal', required=True,string='Animal',readonly=True)
    appointment_id = fields.Many2one('veterinary.appointment',string='Appointment',required=True)
    stage_id = fields.Many2one('veterinary.evaluation.stages',string='Stage',required=True,default=default_stage,group_expand='_read_group_stage_ids')
    user_id = fields.Many2one('res.users', string='Doctor', index=True, track_visibility='onchange', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Owner',required=True,readonly=True)
    
    # Musculoskeletal System Page
    conformation = fields.Char('Conformation')
    feet_shoeing = fields.Char('Feet and Shoeing')
    le = fields.Char('LF')
    rf = fields.Char('RF')
    lh = fields.Char('LH')
    rh = fields.Char('RH')
    neck_back_pelvis = fields.Char('Neck Back Pelvis')
    flexion_tests = fields.Char('Flexion Tests')
    ridden = fields.Char('Ridden')
    diagnostic_imaging = fields.Char('Diagnostic Imaging')
    walk = fields.Char('Walk')
    trot = fields.Char('Trot')
    
    #Respiratory System
    res_general = fields.Char('General')
    lung_auscultation = fields.Char('Lung auscultation')
    upper_airway_endoscopy = fields.Char('Upper airway endoscopy')
    
    #Cardiovascular System
    cardi_general = fields.Char('General')
    auscultation = fields.Char('Auscultation')
    ecg = fields.Char('ECG')
    
    #Gastrointestinal System
    gest_general = fields.Char('General')
    worming_history = fields.Char('Worming Histroy')
    teeth = fields.Char('Teeth')

    #Nervous System
    nevr_general = fields.Char('General')
    mentation = fields.Char('Mentation')
    gait = fields.Char('Gait')
    eyes = fields.Char('Eyes')
    
    #Reproductive and Uniary System
    fig = fields.Char('Female / Intact Male / Gelding')
    testicles = fields.Char('Testicles')
    vulva = fields.Char('Vulva')
    
    #Skin
    scars = fields.Char('Scars - Traumatic / Surgical')
    melanomas = fields.Char('Tumours - Melanomas Sarcoids')
    Dermatitis = fields.Char('Dermatitis')
    Allergy = fields.Char('Allergy')
    skin_other = fields.Char('Other')
    
    other = fields.Text('Other')
    overall_assessment = fields.Text('Overall Assessment')
    recommendations = fields.Text('Recommendations')
    
    def _compute_name(self):
        self.name = self.appointment_id.name
        return True

class EvaluationStages(models.Model):
    _name = 'veterinary.evaluation.stages'
    name = fields.Char('Stage')