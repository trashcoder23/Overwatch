import uuid
import datetime


class Incident:

    def __init__(self, source, metrics=None):

        self.id = str(uuid.uuid4())

        self.source = source
        self.metrics = metrics or {}

        self.classification = None
        self.recommended_action = None
        self.strategy = None

        self.confidence = None
        self.severity = None

        self.status = "open"

        self.created_at = datetime.datetime.utcnow().isoformat()

        self.history = []

        self.add_history("incident_created")

    def add_history(self, event):

        self.history.append({
            "event": event,
            "timestamp": datetime.datetime.utcnow().isoformat()
        })

    def update_classification(self, classification, action, confidence=None):

        self.classification = classification
        self.recommended_action = action
        self.confidence = confidence

        self.add_history("classified")

    def set_strategy(self, strategy):

        self.strategy = strategy
        self.add_history("strategy_generated")

    def resolve(self):

        self.status = "resolved"
        self.add_history("resolved")

    def to_dict(self):

        return {
            "incident_id": self.id,
            "source": self.source,
            "metrics": self.metrics,
            "classification": self.classification,
            "recommended_action": self.recommended_action,
            "strategy": self.strategy,
            "confidence": self.confidence,
            "status": self.status,
            "history": self.history
        }