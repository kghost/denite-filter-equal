
# ============================================================================
# FILE: sorter/word.py
# AUTHOR: Tomohito OZAKI <ozaki at yuroyoro.com>
# DESCRIPTION: Simple filter to sort candidates by ascii order of word
# License: MIT license
# ============================================================================

from denite.base.filter import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/location'
        self.description = 'sort candidates by location (file:line)'

    def filter(self, context):
        return sorted(context['candidates'],
                      key=lambda x: (
                          x['word'],
                          x['action__path'],
                          x['action__line'],
                          x['action__col']))
