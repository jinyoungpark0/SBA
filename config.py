import os

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
TEXTS_DIR  = os.path.join(BASE_DIR, "..", "texts", "open access")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

# Pilot subset — comment out PILOT_TEXTS to run all texts in TEXTS_DIR
PILOT_TEXTS = [
    "Dante_Alighieri_Inferno.txt",
]

CHUNK_WORDS   = 1000
OVERLAP_WORDS = 200

SCREEN_MODEL = "claude-haiku-4-5-20251001"
FILTER_MODEL = "claude-haiku-4-5-20251001"
TAG_MODEL    = "claude-sonnet-4-6"

# Prompt versions (files in prompts/). Never edit a prompt in place: add a new
# file and change the version here.
#   v3 layout: one shared system prompt + one task prompt per step. Task prompts
#              contain <<PASSAGE>> and are sent as the user message.
#   To re-run the original pilot set: screen_v1 / filter_v2 / tag_v2. Those files
#   are sent as the system message and SYSTEM_PROMPT_VERSION is not used.
SYSTEM_PROMPT_VERSION = "system_v1"
SCREEN_PROMPT_VERSION = "screen_v2"
FILTER_PROMPT_VERSION = "filter_v3"
TAG_PROMPT_VERSION    = "tag_v3"
