from . import db
from sqlalchemy.orm import validates

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chrom1 = db.Column(db.String(100), nullable=False)
    start1 = db.Column(db.Integer, nullable=False)
    end1 = db.Column(db.Integer, nullable=False)
    chrom2 = db.Column(db.String(100), nullable=False)
    start2 = db.Column(db.Integer, nullable=False)
    end2 = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)    
    sample = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<Sample {self.sample}>'
    
    def serialize(self):
        return {
            'sample': self.sample,
            'chrom1': self.chrom1,
            'start1': self.start1,
            'end1': self.end1,
            'chrom2': self.chrom2,
            'start2': self.start2,
            'end2': self.end2,
            'score': self.score
        }
    
    @validates('score')
    def validate_score(self, sample, score):
        if score < 0 or score > 10:
            raise AssertionError('Score must be between 0 and 10: score {} at {}'.format(score, self))
        return score
    
    # AssertionError('Score must be between 0 and 10: score score at sample 11') == e