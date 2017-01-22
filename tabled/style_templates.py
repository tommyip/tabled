"""
tabled.style_templates
~~~~~~~~~~~~~~~~~~~~~~

:synopsis: Contains table styles.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

from typing import Dict, Text

# Style: default
# +------------+-----------+--------------+
# | Heading 1  | Heading 2 | Last heading |
# +------------+-----------+--------------+
# | First cell | Cell 2    | Cell 3       |
# | Cell 4     | Cell 5    | Cell 6       |
# | Cell 7     | Cell 8    | Last cell    |
# +------------+-----------+--------------+
DEFAULT = {
    'vertical':     '|',
    'horizontal':   '-',
    'top_left':     '+',
    'top_right':    '+',
    'bottom_left':  '+',
    'bottom_right': '+',
    'down_joint':   '+',
    'up_joint':     '+',
    'left_joint':   '+',
    'right_joint':  '+',
    'cross_joint':  '+'
}

# Style: terminal
# ╔════════════╦═══════════╦══════════════╗
# ║ Heading 1  ║ Heading 2 ║ Last heading ║
# ╠════════════╬═══════════╬══════════════╣
# ║ First cell ║ Cell 2    ║ Cell 3       ║
# ║ Cell 4     ║ Cell 5    ║ Cell 6       ║
# ║ Cell 7     ║ Cell 8    ║ Last cell    ║
# ╚════════════╩═══════════╩══════════════╝
TERMINAL = {
    'vertical':     '║',
    'horizontal':   '═',
    'top_left':     '╔',
    'top_right':    '╗',
    'bottom_left':  '╚',
    'bottom_right': '╝',
    'down_joint':   '╦',
    'up_joint':     '╩',
    'left_joint':   '╠',
    'right_joint':  '╣',
    'cross_joint':  '╬'
}

STYLE_TEMPLATES = dict(
    default=DEFAULT,
    terminal=TERMINAL
)


def get_style(style: Text = 'default') -> Dict[str, Dict[str, Text]]:
    """ Construct and return a table style.

    Args:
        style: Style name.

    Returns:
        A dictionary of style separated by categories.
    """

    styling = STYLE_TEMPLATES[style]

    return {
        'raw': styling,  # The entire stylesheet.
        'row': {
            'left': styling['vertical'],
            'right': styling['vertical'],
            'connector': styling['vertical']
        },
        'top_border': {
            'left': styling['top_left'],
            'right': styling['top_right'],
            'connector': styling['down_joint']
        },
        'divider': {
            'left': styling['left_joint'],
            'right': styling['right_joint'],
            'connector': styling['cross_joint']
        },
        'bottom_border': {
            'left': styling['bottom_left'],
            'right': styling['bottom_right'],
            'connector': styling['up_joint']
        }
    }
