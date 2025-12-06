# Generate test text file for pset2
import random

MIN_WORDS = 1

def gen_text(words, length, punct):
    '''
    words:   list of words to generate from
    length:  tuple of generated text length
    punct:   character set of allowed terminating
             punctuation marks
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
    return gen_text(['blah '],
                    (MIN_WORDS, 3),
                    '...?!')

def gen_narrative():
    return gen_text(['nar ', 'ra ', 'tive '],
                    (MIN_WORDS,4),
                    '.')

def gen_line(mode_f, num_quotes):
    line = mode_f()

    while num_quotes > 0:
        if mode_f == gen_dialog:
            mode_f = gen_narrative
            line += '" ' + mode_f()
        else:
            mode_f = gen_dialog
            line += ' "' + mode_f()
        num_quotes -= 1

    return line

def main():
    # Test dialog and narrative string generators
    dialog = gen_dialog()
    print(dialog)
    narrative = gen_narrative()
    print(narrative)

    # Test line string generators
    for num_quotes in range(4):
        print(num_quotes, gen_line(gen_narrative, num_quotes))
        print(num_quotes, gen_line(gen_dialog, num_quotes))

if __name__ == '__main__':
    main()