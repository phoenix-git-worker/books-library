import logging

from odoo import models, fields

logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'kw.lib.book'  # kw_library_book
    _description = 'Book'

    name = fields.Char()

    active = fields.Boolean(
        default=True
    )
    isbn = fields.Char()

    author_ids = fields.Many2many(
        comodel_name='kw.lib.author',
        string='Authors'
    )
