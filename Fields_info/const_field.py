from base_field import base_field

class loc_field(base_field):

    def __init__(self, loc=(None, None), content = None):
        super().__init__(content)
        self.loc = loc

    def get_content_count(self):
        return len(self.content)






