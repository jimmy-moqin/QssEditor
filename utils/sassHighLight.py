"""
https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
"""

import json

from PyQt5 import QtCore, QtGui


def format(color, style=''):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = QtGui.QColor(color)  # default color is black "#000000

    _format = QtGui.QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QtGui.QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format



class SassHighlighter(QtGui.QSyntaxHighlighter):
    """
    Syntax highlighter for the Sass language.
    """
    # load json file
    with open('utils\sassHighLight.json') as f:
        data = json.load(f)
    
    styles = data['styles']
    keywords = data['keywords']
    operators = data['operators']
    braces = data['braces']
    units = data['units']
    attributes = data['attributes']
    attributes.sort(key=lambda x: len(x), reverse=True)
    pseudostates = data['pseudostates']
    subcontrols = data['subcontrols']
    
    STYLES = {}
    for sty in styles:
        if len(styles[sty]) == 2:
            STYLES[sty] = format(styles[sty][0], styles[sty][1])
        else:
            STYLES[sty] = format(styles[sty][0])

    def __init__(self, parent=None):
        super(SassHighlighter, self).__init__(parent)

        # Multi-line strings (expression, flag, style)
        self.tri_single = (QtCore.QRegularExpression("'''"), 1, self.STYLES['string2'])
        self.tri_double = (QtCore.QRegularExpression('"""'), 2, self.STYLES['string2'])

        rules = []

        # Keyword, operator, and brace rules
        rules += [(r'%s' % w, 0, self.STYLES['keyword']) for w in SassHighlighter.keywords]
        rules += [(r'%s' % o, 0, self.STYLES['operator']) for o in SassHighlighter.operators]
        rules += [(r'%s' % b, 0, self.STYLES['brace']) for b in SassHighlighter.braces]
        rules += [(r'\d+(%s)' % u, 1, self.STYLES['unit']) for u in SassHighlighter.units]
        
        exp = r"\b(" + "|".join(self.attributes) + r")\b"
        rules += [(exp, 0, self.STYLES['attribute'])]
        rules += [(r'\b(\d+)%s\b' % v, 1, self.STYLES['numbers']) for v in SassHighlighter.units]
        rules += [(r'(|&|\.|#).*(%s)' % p, 2, self.STYLES['pseudostate']) for p in SassHighlighter.pseudostates]
        rules += [(r'(|&|\.|#).*(%s)' % p, 2, self.STYLES['subcontrol']) for p in SassHighlighter.subcontrols]
       

        # All other rules
        rules += [

            # Numeric literals
            (r'\b\d+(?:\.\d+)?\b', 0, self.STYLES['numbers']),
            # hex
            (r'\#[0-9A-Fa-f]{6}', 0, self.STYLES['numbers']),
            

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, self.STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, self.STYLES['string']),

            # From '//' until a newline
            (r'\/\/[^\n]*', 0, self.STYLES['comment']),

            # selectores
            (r'\.([a-zA-Z_][a-zA-Z0-9_-]*)[^{:]*', 0, self.STYLES['selector']),
            (r'#.+(?=:{2})|#.+(?=:)|#.+(?={| {)', 0, self.STYLES['selector']),
            (r'^\w+(?=({| {))|^\w+(?=:{1})|^\w+(?=:{2})', 0, self.STYLES['selector']),
            # variable
            (r'\$[a-zA-Z0-9-_]+', 0, self.STYLES['variable']),

            (r"\b(\w+)\([^)]*\)", 1, self.STYLES['function']),
        ]

        # Build a QRegularExpression for each pattern
        self.rules = [(QtCore.QRegularExpression(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """
        Apply syntax highlighting to the given block of text.
        """

        # Do other syntax formatting
        for expression, nth, fmt in self.rules:
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                index = match.capturedStart(nth)
                length = match.capturedLength(nth)
                self.setFormat(index, length, fmt)

        self.setCurrentBlockState(0)

        # # Do multi-line strings
        # in_multiline = self.match_multiline(text, *self.tri_single)
        # if not in_multiline:
        #     in_multiline = self.match_multiline(text, *self.tri_double)

    # def match_multiline(self, text, delimiter, in_state, style):
    #     """
    #     Do highlighting of multi-line strings. ``delimiter`` should be a
    #     ``QRegularExpression`` for triple-single-quotes or triple-double-quotes, and
    #     ``in_state`` should be a unique integer to represent the corresponding
    #     state changes when inside those strings. Returns True if we're still
    #     inside a multi-line string when this function is finished.
    #     """
    #     # If inside triple-single quotes, start at 0
    #     if self.previousBlockState() == in_state:
    #         start = 0
    #         add = 0
    #     # Otherwise, look for the delimiter on this line
    #     else:
    #         start = delimiter.indexIn(text)
    #         # skipping triple quotes within strings
    #         if start in self.tripleQuoutesWithinStrings:
    #             return False
    #         # Move past this match
    #         add = delimiter.matchedLength()

    #     # As long as there's a delimiter match on this line...
    #     while start >= 0:
    #         # Look for the ending delimiter
    #         end = delimiter.indexIn(text, start + add)
    #         # Ending delimiter on this line?
    #         if end >= add:
    #             length = end - start + add + delimiter.matchedLength()
    #             self.setCurrentBlockState(0)
    #         # No; multi-line string
    #         else:
    #             self.setCurrentBlockState(in_state)
    #             length = len(text) - start + add
    #         # Apply formatting
    #         self.setFormat(start, length, style)
    #         # Look for the next match
    #         start = delimiter.indexIn(text, start + length)

    #     # Return True if still inside a multi-line string, False otherwise
    #     if self.currentBlockState() == in_state:
    #         return True
    #     else:
    #         return False
