import hashlib
import json

class SelfHealingVault:
    def __init__(self, risk_threshold: float = 0.50):
        self.risk_threshold = risk_threshold

    def calculate_state_hash(self, payload: dict) -> str:
        serialized = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(serialized).hexdigest()

    def validate_and_heal(self, payload: dict, risk_score: float) -> dict:
        state_hash = self.calculate_state_hash(payload)
        
        if risk_score > self.risk_threshold:
            # Self-healing trigger logic
            return {
                "status": "HEALED",
                "original_hash": state_hash,
                "sanitized_payload": {"status": "reset", "risk": "mitigated"},
                "action": "State payload auto-remediated due to high risk score."
            }
        
        return {
            "status": "VALID",
            "state_hash": state_hash,
            "payload": payload
        }
