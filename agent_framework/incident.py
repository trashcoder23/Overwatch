import uuid
from datetime import datetime


class Incident:

    def __init__(self, source, metrics=None):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()

        self.source = source
        self.metrics = metrics or {}

        self.classification = None
        self.recommended_action = None
        self.strategy = None
        self.status = "open"

    def update_classification(self, classification, action):
        self.classification = classification
        self.recommended_action = action

    def set_strategy(self, strategy):
        self.strategy = strategy

    def resolve(self):
        self.status = "resolved"

    def to_dict(self):

        return {
            "incident_id": self.id,
            "source": self.source,
            "metrics": self.metrics,
            "classification": self.classification,
            "recommended_action": self.recommended_action,
            "strategy": self.strategy,
            "status": self.status
        }