import logging

from odoo import models, fields

logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'kw.lib.author'  # kw_library_author
    _description = 'Author'

    name = fields.Char()

    active = fields.Boolean(
        default=True
    )
    book_ids = fields.Many2many(
        comodel_name='kw.lib.book',
        string='Boooks',
        relation='author_book_rel'
    )
