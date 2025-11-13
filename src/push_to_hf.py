from huggingface_hub import Repository
from pathlib import Path

def push_model_to_hf(model_path="models/exp1", repo_id="your-username/trustai-model"):
    Path(model_path).mkdir(parents=True, exist_ok=True)
    repo = Repository(local_dir="repo_clone", clone_from=repo_id, use_auth_token=True)
    repo.git_pull()
    repo.lfs_track("*.bin")
    repo.copy_from_local(model_path)
    repo.push_to_hub(commit_message="Auto push trained model")
    print("✅ Model pushed to Hugging Face Hub!")

if __name__ == "__main__":
    push_model_to_hf()
