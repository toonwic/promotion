# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Rule(models.Model):
    _name = 'promotion.rule'
    name = fields.Char(string="Rule", required=True)

    # many Rule to one Product
    # product_id = fields.Many2one('product.product', string="Product")

    # product_ids = fields.One2many('product.product',
        # 'rule_id', string="Products")

    # one Rule to many Conditions
    condition_ids = fields.One2many(
        'promotion.condition', 'rule_id', string="Conditions")

    # one Rule to many Actions
    action_ids = fields.One2many(
        'promotion.action', 'rule_id', string="Actions")

class Condition(models.Model):
    _name = 'promotion.condition'
    condition = fields.Selection([
        ('x_quantity_of_product', 'X Quantity of Product'),
    ])
    operator = fields.Selection([
        ('is', 'Is'),
        ('not_is', 'Not Is'),
        ('is_less_than', 'Is Less Than'),
        ('is_less_than_or_equal_to', 'Is Less Than Or Equal To'),
        ('is_greater_than', 'Is Greater Than'),
        ('is_greater_than_or_equal_to', 'Is Greater Than Or Equal To'),
    ])
    quantity = fields.Integer(string="Quantity")
    price = fields.Integer(string="Price")

    # many Conditions to one Product
    product_id = fields.Many2one('product.product',
        ondelete='set null', string="Product", index=True)

    # many Conditions to one Rule
    rule_id = fields.Many2one('promotion.rule', ondelete='cascade')

class Action(models.Model):
    _name = 'promotion.action'
    apply = fields.Selection([
        ('gift_with_purchase', 'Gift with Purchase'),
        ('x_product_for_y_discount', 'X Product for Y Discount'),
        ('order_percent_discount', 'Order Percent Discount')
    ])

    discount = fields.Integer(string="Discount")
    quantity = fields.Integer(string="Quantity")
    price = fields.Integer(string="Price")
    amount = fields.Integer(string="Amount")

    # many Actions to many Products
    xproduct_ids = fields.Many2many('product.product', string="Products")

    # many Actions to one rule
    rule_id = fields.Many2one('promotion.rule', ondelete='cascade')

    #prod_id = fields.Many2one('res.users', ondelete='set null', string="Product", index=True)
    #rule_id = fields.Many2one('promotion.rule', ondelete='cascade', string="Rule", required=True)
