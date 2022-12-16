def format_line(text, max_width, prefix='', suffix=''):
    char_count = -1
    if prefix:
        char_count += len(prefix) + 1
    if suffix:
        char_count += len(suffix) + 1
    words_list = list()
    lines_list = list()
    for word in text.split(' '):
        char_count += len(word) + 1
        if char_count > max_width + 1:
            if prefix:
                words_list.insert(0, prefix)
            if suffix:
                words_list.insert(len(words_list), suffix)
            lines_list.append(words_list.copy())
            words_list.clear()
            char_count = len(word) + 1
            if prefix:
                char_count += len(prefix) + 1
            if suffix:
                char_count += len(suffix) + 1
        words_list.append(word)
    if words_list:
        if prefix:
            words_list.insert(0, prefix)
        if suffix:
            words_list.insert(len(words_list), suffix)
        lines_list.append(words_list.copy())

    for line in lines_list:
        print('(', len(' '.join(line)), ')', ' '.join(line))

def main():
    text = "Esta es una línea larga que debe dividirse en diferentes líneas, de las cuales cada una tiene un máximo de 40 caracteres."
    width = 40
    format_line(text, width, '*', '-')

if __name__ == '__main__':
    main()
