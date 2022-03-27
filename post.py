class Post:
    def __init__(self, post_id, title, subtitle, body, by, _from):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.by = by
        self._from = _from