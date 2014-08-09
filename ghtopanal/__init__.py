import os

from microhackaton import sd

if sd is not None:
    sd.register('github-topics-analyzer', os.environ.get('PUBLIC_HOST', '0.0.0.0'), os.environ.get('PORT', 8911))