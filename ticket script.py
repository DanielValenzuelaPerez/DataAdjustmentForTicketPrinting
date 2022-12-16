def format_line(text, max_width, font_size=12, alignment='left', font_type='normal', prefix='', suffix=''):
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

    for i in range(len(lines_list)):
        lines_list[i] = dict(text=' '.join(lines_list[i]), size=font_size, align=alignment, style=font_type)
    return lines_list

def format_items(items, width, str_cant, str_total, str_articulo, font_size=12, alignment='left', font_type='normal'):
    lines_list = list()
    for item in items:
        line = str(item['qty']) + ''.join([' ' for _ in range(len(str_cant) - len(str(item['qty'])))])
        product = item['product']
        model = item['model']
        presentation = item['presentation']
        line += product[:width - 1 - (len(str_cant)+len(str_total))]
        line += ''.join([' ' for _ in range((len(str_cant) + len(str_articulo)) - len(line) + len(str_total) - len(item['price']))]) + item['price']
        lines_list.extend(format_line(line, width, font_size, alignment, font_type))

        # Modelo / Presentación
        len_articulo =  width - (len(str_cant)+len(str_total))
        model_presentation = model[0:(len_articulo - 1)//2] + ' ' + presentation[0:(len_articulo - 1)//2]
        model_presentation_formatted = format_line(model_presentation, width, prefix=''.join([' ' for _ in range(len(str_cant))]))
        lines_list.extend(model_presentation_formatted)
    
    return lines_list

def format_payment(payment, len_total, width, font_size=12, alignment='right', font_type='normal'):
    str_total = 'Total M.N '
    str_efectivo = 'Efectivo '
    str_cambio = 'Cambio '
    str_iva = '**Total de impuestos 16% '

    str_total = str_total + ''.join([' ' for _ in range(len_total - len(payment['total']))]) + payment['total']
    str_efectivo = str_efectivo + ''.join([' ' for _ in range(len_total - len(payment['efectivo']))]) + payment['efectivo']
    str_cambio =  str_cambio + ''.join([' ' for _ in range(len_total - len(payment['cambio']))]) + payment['cambio']
    str_iva = str_iva + ''.join([' ' for _ in range(len_total - len(payment['iva']))]) + payment['iva']

    line_list = list()
    line_list.extend(format_line(str_total, width, alignment=alignment))
    line_list.extend(format_line(str_efectivo, width, alignment=alignment))
    line_list.extend(format_line(str_cambio, width, alignment=alignment))
    line_list.extend(format_line(str_iva, width, alignment=alignment))

    return line_list

def main():
    order_data = dict(
        id=123,
        business_name='Cuca y Lupe en colaboración con otra empresa',
        business_rfc='1234567890ABC',
        branch_name='Plaza Patria',
        branch_id=1,
        branch_address=dict(
            street='Avenida Patria',
            number='456',
            suburb='Colonia las Américas',
            cp=45234
        ),
        items=[
            dict(
                qty=3,
                product='Tenis Jordán Piratas',
                model='Negro',
                presentation='27 cm',
                price="1000.00"
            ),
            dict(
                qty=2,
                product='Pan de muertos',
                model='Chocolate',
                presentation='Grande',
                price="200.00"
            ),
            dict(
                qty=6,
                product='Producto X',
                model='Modelo Y',
                presentation='Presentación Z',
                price="10000.00"
            )
        ],
        payment=dict(
            total="262.34",
            efectivo="1000.00",
            cambio="737.10",
            iva="0.00"
        ),
        cashier_name='Victor Zamora',
        date_and_time='12/12/2022 20:23',
        footnote='¡Gracias por su compra!'
    )
    WIDTH = 32
    line_list = list()
    # Adjust Header
    line_list.extend(format_line(order_data['business_name'], WIDTH, alignment='center', font_type='bold'))
    line_list.extend(format_line(order_data['business_rfc'], WIDTH, prefix='R.F.C ', alignment='center'))
    line_list.extend(format_line(f"{order_data['branch_name']} ({order_data['branch_id']})", WIDTH, prefix='Suc. ', alignment='center'))
    line_list.extend(format_line(f"{order_data['branch_address']['street']} {order_data['branch_address']['number']}", WIDTH, alignment='center'))
    line_list.extend(format_line(f"{order_data['branch_address']['suburb']} C.P. {order_data['branch_address']['cp']}", WIDTH, alignment='center'))
    line_list.extend(format_line(''.join(['-' for _ in range(WIDTH)]), WIDTH))
    # Adjust Articles
    str_cantidad = 'Cant  '
    str_total = 'Total   '
    str_articulo = 'Artículo'.ljust(WIDTH-len(str_cantidad)-len(str_total), ' ')
    line_list.extend(format_line(str_cantidad+str_articulo+str_total, WIDTH))
    line_list.extend(format_items(order_data['items'], WIDTH, str_cantidad, str_total, str_articulo))
    # Adjust Payment
    line_list.extend(format_payment(order_data['payment'], len(str_total), WIDTH))
    # Adjust Footer
    line_list.extend(format_line(order_data['cashier_name'], WIDTH, prefix='Le atendió: ', alignment='center'))
    line_list.extend(format_line(order_data['date_and_time'] + ' SUC. ' + str(order_data['branch_id']), WIDTH, alignment='center'))
    line_list.extend(format_line(str(order_data['id']), WIDTH, prefix='***Folio: ' + ''.join(['0' for _ in range(8 - len(str(order_data['id'])))]), suffix='***', alignment='center'))

    for line in line_list:
        print(line)

if __name__ == '__main__':
    main()


"""
Cuca y Lupe
R.F.C. Meid345m3454
Suc. Plaza Patria (01)
Av.Patria 456
Col las Américas C.P 45234
--------------------------------
Cant  Artículo          Total   
1     Tenis Jordán Pira  1002.00
      Negro, 27 cm
1     Tenis Jordán Pira  1002.00
      Negro, 27 cm 

             Total M.N    262.34
              Efectivo    500.00
                Cambio    237.10

**Total de impuestos 16%    0.00

Le atendió: Victor Zamora
28/07/2022 20:23 SUC. 01
***Folio: 00000123***
"""