import os

from microhackaton import sd

if sd is not None:
    sd.register('github-topics-analyzer', os.environ.get('HOST', 'localhost'), os.environ.get('PORT', 8911))