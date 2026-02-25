from src.settings.extensions import db
import json

class Tool(db.Model):
    
    __tablename__ = "tools"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    link = db.Column(db.String(2048), nullable=False)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.Text, nullable=False)
    
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
    
    def set_tags(self, tags_list:list):
        self.tags = json.dumps(tags_list)
        
    def get_tags(self) -> list:
        return json.loads(self.tags)
    
    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "tags": self.get_tags(),
            "id": self.id
        }
        
    def __repr__(self):
        return f"ID: {self.id} - TITLE: {self.title}"