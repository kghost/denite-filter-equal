from denite.base.filter import Base


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'matcher/equal'
        self.description = 'simple equal matcher'

    def filter(self, context):
        candidates = context['candidates']
        if context['input'] == '':
            return candidates

        s = context['input']
        return [x for x in candidates if s == x['word']]
