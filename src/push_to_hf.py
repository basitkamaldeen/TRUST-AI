from huggingface_hub import HfApi, HfFolder, Repository
HfFolder.save_token("HF_TOKEN")  # store as secret in CI
repo = Repository("tmp", clone_from="username/trustai-model")
# copy files, commit, push
