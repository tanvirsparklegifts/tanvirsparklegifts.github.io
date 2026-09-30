# config/cloud_state.py
import os
import json
from google.cloud import storage, datastore

class CloudStateVault:
    def __init__(self, project_id="project-449e9aa7-9f7e-4f91-951", bucket_name="tanvirsparklegifts-vault-bucket"):
        self.project_id = project_id
        self.bucket_name = bucket_name
        self.datastore_client = datastore.Client(project=self.project_id)
        
    def save_agent_state_to_cloud(self, agent_id, state_payload):
        print(f"[*] Connecting to GCP Project: {self.project_id}...")
        
        # Saving state to Google Cloud Datastore for secure persistence
        kind = "AgentState"
        key = self.datastore_client.key(kind, agent_id)
        entity = datastore.Entity(key=key)
        entity.update(state_payload)
        
        self.datastore_client.put(entity)
        print(f"[+] Agent state for {agent_id} securely stored in GCP Datastore.")
        return True

    def fetch_agent_state(self, agent_id):
        key = self.datastore_client.key("AgentState", agent_id)
        entity = self.datastore_client.get(key)
        if entity:
            print(f"[+] Retrieved state for {agent_id} from cloud.")
            return dict(entity)
        print(f"[-] No state found for {agent_id} in cloud.")
        return None

if __name__ == "__main__":
    # Test execution snippet
    manager = CloudStateVault()
    sample_state = {"status": "ACTIVE", "risk_score": 0.0, "protocol": "T.M.T-Protocol"}
    # manager.save_agent_state_to_cloud("architect_core_01", sample_state)
