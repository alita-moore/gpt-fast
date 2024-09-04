# %%
# NOTE: THIS IS GOING TO FAIL AND THAT's OKAY
!./scripts/prepare.sh mistralai/Mistral-7B-v0.1
# %%
from generate import main
from pathlib import Path

main(
    "I'm a large language model",
    False,
    5,
    200,
    1,
    200,
    0.8,
    Path(
        "/workspaces/data-engine/temp/gpt-fast/checkpoints/mistralai/Mistral-7B-v0.1/model.pth"
    ),
    False,
    False,
    None,
    None,
    5,
    "cuda",
)

# %%
