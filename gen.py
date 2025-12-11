# Generate test text file for pset2
import random

# Allow us to temporarily generate empty narrative
# and dialogue strings. Normally set to 1.
MIN_WORDS = 1

def mode_str(mode_f):
    '''
    Return a printable string for the current mode.
    '''
    if mode_f == gen_narrative:
        last_mode = '[n]'
    elif mode_f == gen_dialog:
        last_mode = '[d]'
    else:
        assert False, "Unexpected mode_f"
    return last_mode

def gen_text(words, length, punct):
    '''
    Return a string containing random string constrained by the
    input parameters. The string will start with a capital
    letter and not have any extra whitespace around it.

    words:   list of words to generate from.
    length:  tuple of generated text length.
    punct:   character set of allowed terminating
             punctuation marks.
    '''
    # Choose text length r from length range
    start, end = length
    r = random.randint(start, end)
    if r == 0:
        return ''
    
    # Generate text of r words
    if len(words) == 1:
        t = words[0] * r
    else:
        t = ''
        for i in range(r):
            t += random.choice(words)

    # Fix capitalization and add punctuation
    t = t.strip().capitalize()
    t += random.choice(punct)

    return t

def gen_dialog():
    ''' Return a string representing some dialog. '''
    return gen_text(['blah '],
                    (MIN_WORDS, 3),
                    '...?!')

def gen_narrative():
    ''' Return a string representing some narrative. '''
    return gen_text(['nar ', 'ra ', 'tive '],
                    (MIN_WORDS,4),
                    '.')

def gen_line(mode_f, num_quotes):
    '''
    Return a 2-tuple containing (1) a random line of text that
    meets the specified requirements and (2) the mode at the
    end of the line.

    mode_f:     function that starts the line.
    num_quotes: number of quotes on the line.
    '''
    assert num_quotes >= 0

    line = mode_f()

    while num_quotes > 0:
        if mode_f == gen_dialog:
            mode_f = gen_narrative
            line += '" ' + mode_f()
        else:
            mode_f = gen_dialog
            line += ' "' + mode_f()
        num_quotes -= 1

    return (line, mode_f)

def gen_paragraph(mode_f, quotes_per_line):
    '''
    Return a 2-tuple containing (1) a random paragraph of text
    that meets the specified requirements and (2) the mode at
    the end of the paragraph.

    mode_f: function that starts the paragraph's 1st line.
    quotes_per_line: list of quotes on each line.
    '''
    assert len(quotes_per_line) > 0
    text = ''

    for i in range(len(quotes_per_line)):
        line, mode_f = gen_line(mode_f, quotes_per_line[i])
        text += line + '\n'

    # Shave off the last (unnecessary) return
    return (text.strip(), mode_f)

def main():
    # Test paragraph string generator
    qpl = [0, 1, 2]
    mode_f = gen_narrative
    print(mode_str(mode_f))
    text, mode_f = gen_paragraph(mode_f, qpl)
    print(text)
    print(mode_str(mode_f))

if __name__ == '__main__':
    main()