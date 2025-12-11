# Regression tests for gen.py
import gen

def main():
    test_num = 1

    desc = 'Test dialog and narrative string generators'
    print(f'TEST {test_num}: {desc}')
    dialog = gen.gen_dialog()
    print(dialog)
    narrative = gen.gen_narrative()
    print(narrative)
    print()

    desc = 'Test line string generators'
    test_num += 1
    print(f'TEST {test_num}: {desc}')
    for num_quotes in range(4):
        line, mode_f = gen.gen_line(gen.gen_narrative, num_quotes)
        print(num_quotes, line, gen.mode_str(mode_f))

        line, mode_f = gen.gen_line(gen.gen_dialog, num_quotes)
        print(num_quotes, line, gen.mode_str(mode_f))
    print()

    desc = 'Test paragraph string generator'
    test_num += 1
    print(f'TEST {test_num}: {desc}')
    qpl = [0, 1, 2]    # quotes per line as a list
    mode_f = gen.gen_narrative
    print(gen.mode_str(mode_f))
    text, mode_f = gen.gen_paragraph(mode_f, qpl)
    print(text.strip())
    print(gen.mode_str(mode_f))

if __name__ == '__main__':
    main()