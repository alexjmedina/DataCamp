Example of RegEx
\w+     word                'Magic'
\d      digit               9
\s      space               ''
.*      wildcard            'username74'
+ or *  greedy match        'aaaaaa'
\S      not space           'no_spaces'
[a-z]   lowercase group     'abcdefg'

re Module

split
findall
search
match

Example:
re.split('\s+', 'Split on spaces')
Out: ['Split', 'on', 'spaces.']

