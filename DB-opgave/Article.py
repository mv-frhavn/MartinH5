class Article:
    def __init__(self, article_id, name, description, picture_path):
        self.article_id = article_id
        self.name = name
        self.description = description
        self.picture_path = picture_path


class NewArticle(Article):
    pass


class RemoveArticle(Article):
    pass

