"""
tabled.style_templates
~~~~~~~~~~~~~~~~~~~~~~

:synopsis: Contains table styles.
:copyright: (c) 2017, Tommy Ip.
:license: MIT
"""

# Style: default
# +------------+-----------+--------------+
# | Heading 1  | Heading 2 | Last heading |
# +------------+-----------+--------------+
# | First cell | Cell 2    | Cell 3       |
# | Cell 4     | Cell 5    | Cell 6       |
# | Cell 7     | Cell 8    | Last cell    |
# +------------+-----------+--------------+
default = {
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
terminal = {
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

style_templates = dict(
    default=default,
    terminal=terminal
)
