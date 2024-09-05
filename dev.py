# %%
# !./scripts/prepare.sh mistralai/Mistral-7B-v0.1

# %%
from generate import main
from pathlib import Path

main(
    prompt="The quick brown fox",
    interactive=False,
    num_samples=5,
    max_new_tokens=100,
    batch_size=1,
    top_k=1,
    temperature=0.5,
    checkpoint_path=Path("/workspaces/data-engine/temp/gpt-fast/checkpoints/mistralai/Mistral-7B-v0.1/model.pth"),
    #compile=True,
    compile_prefill=False,
    profile=None,
    #draft_checkpoint_path=Path("/workspaces/data-engine/temp/gpt-fast/checkpoints/mistralai/Mistral-7B-v0.1/model_int8.pth"),
    speculate_k=6,
    device="cuda",
)

# %%
