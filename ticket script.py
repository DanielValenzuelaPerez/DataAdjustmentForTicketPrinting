def format_line(text, max_width, prefix='', suffix=''):
    text = prefix + text + suffix
    char_count = -1
    words_list = list()
    lines_list = list()
    for word in text.split(' '):
        char_count += len(word) + 1
        if char_count > max_width + 1:
            lines_list.append(words_list.copy())
            words_list.clear()
            char_count = len(word) + 1
        words_list.append(word)
    if words_list:
        lines_list.append(words_list.copy())

    # for line in lines_list:
    #     print('(', len(' '.join(line)), ')', ' '.join(line))
    return lines_list

def format_items(items, width):
    str_cant = 'Cant  '
    str_total = 'Total     '
    str_articulo = 'Artículo'
    str_articulo += ''.join([' ' for _ in range(width - (len(str_articulo)+len(str_cant)+len(str_total)))])
    lines_list = list()
    lines_list.append(str_cant + str_articulo + str_total)
    for item in items:
        line = str(item['qty']) + ''.join([' ' for _ in range(len(str_cant) - len(str(item['qty'])))])
        product_description = '. '.join([item['product'], item['model'], item['presentation']])
        product_line_list = format_line(product_description, width - 2 - (len(str_cant)+len(str_total)))
        line += ' '.join(product_line_list[0])
        line += ''.join([' ' for _ in range((len(str_cant) + len(str_articulo)) - len(line))]) + '$ ' + item['price']
        lines_list.append(line)
        for product_line in product_line_list[1:]:
            lines_list.append(''.join([' ' for _ in range(len(str_cant))]) + ' '.join(product_line))
    
    for line in lines_list:
        print(line)

def main():
    text = "Esta es una línea larga que debe dividirse en diferentes líneas, de las cuales cada una tiene un máximo de 40 caracteres."
    width = 60
    # format_line(text, width, '*', '-')

    items = [
        dict(
            qty=3,
            product='El nombre del productoo iría aquí y puede ser un nombre largo',
            model='Este sería el nombre del modelo del producto',
            presentation='Este sería el nombre de la presentación del producto',
            price="100.00"
        ),
        dict(
            qty=2,
            product='El nombre del segundo producto iría aquí y puede ser un nombre largo',
            model='Este sería el nombre del modelo del segundo producto',
            presentation='Este sería el nombre de la presentación del segundo producto',
            price="200.00"
        ),
        dict(
            qty=6,
            product='Producto X',
            model='Modelo Y',
            presentation='Presentación Z',
            price="9000.00"
        )
    ]
    format_items(items, width)

    payment = dict(
        total="262.34",
        efectivo="500.00",
        cambio="237.10",
        iva="0.00"
    )
    len_total = 10
    str_total = 'Total M.N $'
    str_efectivo = 'Efectivo $'
    str_cambio = 'Cambio $'
    str_iva = '**Total de impuestos 16% $'

    t = format_line(str_total + ' ' + payment['total'], 40, ''.join([' ' for _ in range(width - len_total - len(str_total) + 1)]))
    print(' '.join(t[0]))

    str_total = ''.join([' ' for _ in range(width - len_total - len(str_total) + 1)]) + str_total + ' ' + payment['total']
    print(str_total)
    str_efectivo = ''.join([' ' for _ in range(width - len_total - len(str_efectivo) + 1)]) + str_efectivo + ' ' + payment['efectivo']
    print(str_efectivo)
    str_cambio = ''.join([' ' for _ in range(width - len_total - len(str_cambio) + 1)]) + str_cambio + ' ' + payment['cambio']
    print(str_cambio)
    str_iva = ''.join([' ' for _ in range(width - len_total - len(str_iva) + 1)]) + str_iva + ' ' + payment['iva']
    print(str_iva)

if __name__ == '__main__':
    main()
