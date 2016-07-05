# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from glitter import block_admin

from .models import RelatedPage, RelatedPagesBlock


class RelatedPageInline(block_admin.StackedInline):
    model = RelatedPage
    extra = 1


class RelatedPagesBlockAdmin(block_admin.BlockAdmin):
    inlines = [RelatedPageInline]


block_admin.site.register(RelatedPagesBlock, RelatedPagesBlockAdmin)
block_admin.site.register_block(RelatedPagesBlock, 'App Blocks')
