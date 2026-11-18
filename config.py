import os

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))


def _first_existing(*paths):
    for path in paths:
        if os.path.isdir(path):
            return path
    return paths[0]


# The GitHub repo keeps the texts beside the scripts, in "texts/open acess"
# (spelled that way). The original layout had them one level up, in
# "texts/open access". Use whichever exists.
TEXTS_DIR  = _first_existing(
    os.path.join(BASE_DIR, "texts", "open access"),
    os.path.join(BASE_DIR, "texts", "open acess"),
    os.path.join(BASE_DIR, "..", "texts", "open access"),
)

# Texts that must stay off GitHub (copyrighted transcripts, licensed translations)
# go in texts/local/, which Git ignores. A file named in PILOT_TEXTS is looked
# for in TEXTS_DIR first, then here.
LOCAL_TEXTS_DIR = os.path.join(BASE_DIR, "texts", "local")

# Each run writes to results/<RUN_NAME>/, so an earlier run is never overwritten.
# Change the name for every new run. Run folders are ignored by Git because the
# archive and labeled files contain the full text of the sources.
# Set to "" to write straight into results/, as the original pipeline did.
RUN_NAME    = "run2_four_texts"
RESULTS_DIR = os.path.join(BASE_DIR, "results", RUN_NAME) if RUN_NAME else os.path.join(BASE_DIR, "results")
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

# Pilot subset — comment out PILOT_TEXTS to run all texts in TEXTS_DIR
PILOT_TEXTS = [
    "Laozi_Tao_Te_Ching.txt",                                          # Legge translation, Project Gutenberg #216
    "Franz_Kafka_The_Metamorphosis.txt",                               # Wyllie translation, Project Gutenberg #5200
    "Brene_Brown_The_Power_of_Vulnerability.txt",                      # TEDxHouston 2010 transcript
    "Andrew_Solomon_Why_Is_It_So_Hard_To_Talk_About_Depression.txt",   # NPR TED Radio Hour transcript
    # "Dante_Alighieri_Inferno.txt",
]

CHUNK_WORDS   = 1000
OVERLAP_WORDS = 200

# ── API provider ─────────────────────────────────────────────────────────────
#   "openrouter"  OpenRouter. Needs OPENROUTER_API_KEY; no extra Python package.
#   "anthropic"   Anthropic's API directly. Needs ANTHROPIC_API_KEY and
#                 `pip install anthropic`.
PROVIDER = "openrouter"

# The same two models under each provider's naming.
MODELS = {
    "anthropic":  {"small": "claude-haiku-4-5-20251001",  "large": "claude-sonnet-4-6"},
    "openrouter": {"small": "anthropic/claude-haiku-4.5", "large": "anthropic/claude-sonnet-4.6"},
}
SCREEN_MODEL = MODELS[PROVIDER]["small"]
FILTER_MODEL = MODELS[PROVIDER]["small"]
TAG_MODEL    = MODELS[PROVIDER]["large"]
RATE_MODEL   = MODELS[PROVIDER]["large"]

# OpenRouter can pass a request to any of several companies that host the same
# model. These settings (sent with every request) keep that fixed:
#   only             : the request goes to Anthropic itself, not another host
#   allow_fallbacks  : if Anthropic is unavailable, fail; do not switch host
#   data_collection  : refuse hosts that keep or train on the text (protocol §2)
# The host and model that actually answered are recorded in run_log.json.
OPENROUTER_ROUTING = {
    "only": ["anthropic"],
    "allow_fallbacks": False,
    "data_collection": "deny",
}

# Prompt versions (files in prompts/). Never edit a prompt in place: add a new
# file and change the version here.
#   v3 layout: one shared system prompt + one task prompt per step. Task prompts
#              contain <<PASSAGE>> and are sent as the user message.
#   To re-run the original pilot set: screen_v1 / filter_v2 / tag_v2. Those files
#   are sent as the system message and SYSTEM_PROMPT_VERSION is not used.
#
# Tag step, two modes:
#   tag_open_v1  open coding. No code list; the tagger names each belief it finds
#                (label, definition, evidence). Output: results/open_codes.csv, one
#                row per belief. Use this first, to build the classification.
#   tag_v3       deductive coding against WORKING_CLASSIFICATION in pipeline.py.
#                Use once a classification has been built from the open codes.
SYSTEM_PROMPT_VERSION = "system_v1"
SCREEN_PROMPT_VERSION = "screen_v2"
FILTER_PROMPT_VERSION = "filter_v3"
TAG_PROMPT_VERSION    = "tag_open_v1"

# Step 5: place each open-coded belief in an area (BELIEF_AREAS in pipeline.py)
# and rate it on evaluation, inevitability and intertwinement (1-5, blank = no
# position). Runs only after tag_open_v1. Set to None to skip the step; areas
# and ratings are then left blank.
RATE_PROMPT_VERSION   = "rate_v1"
