"""
Write functions that convert two input args into kebab-case sting output.

>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'
"""

def link(argoyle1, argoyle2):
    linker = str(argoyle1) + "-" + str(argoyle2)
    return linker