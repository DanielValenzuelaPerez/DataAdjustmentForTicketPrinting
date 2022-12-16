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

    for i in range(len(lines_list)):
        lines_list[i] = ' '.join(lines_list[i])        
    return lines_list

def format_items(items, width, str_cant, str_total, str_articulo):
    # str_cant = 'Cant  '
    # str_total = 'Total   '
    # str_articulo = 'Artículo'
    # str_articulo += ''.join([' ' for _ in range(width - (len(str_articulo)+len(str_cant)+len(str_total)))])
    lines_list = list()
    # lines_list.append(str_cant + str_articulo + str_total)
    for item in items:
        line = str(item['qty']) + ''.join([' ' for _ in range(len(str_cant) - len(str(item['qty'])))])
        product = item['product']
        model = item['model']
        presentation = item['presentation']
        line += product[:width - 1 - (len(str_cant)+len(str_total))]
        line += ''.join([' ' for _ in range((len(str_cant) + len(str_articulo)) - len(line) + len(str_total) - len(item['price']))]) + item['price']
        lines_list.append(line)

        # Modelo / Presentación
        len_articulo =  width - (len(str_cant)+len(str_total))
        model_presentation = model[0:(len_articulo - 1)//2] + ' ' + presentation[0:(len_articulo - 1)//2]
        model_presentation_formatted = format_line(model_presentation, width, ''.join([' ' for _ in range(len(str_cant))]))
        lines_list.append(model_presentation_formatted[0])
    
    # for line in lines_list:
    #     print(line)
    return lines_list

def format_payment(payment, len_total):
    str_total = 'Total M.N '
    str_efectivo = 'Efectivo '
    str_cambio = 'Cambio '
    str_iva = '**Total de impuestos 16% '

    str_total = str_total + ''.join([' ' for _ in range(len_total - len(payment['total']))]) + payment['total']
    str_efectivo = str_efectivo + ''.join([' ' for _ in range(len_total - len(payment['efectivo']))]) + payment['efectivo']
    str_cambio =  str_cambio + ''.join([' ' for _ in range(len_total - len(payment['cambio']))]) + payment['cambio']
    str_iva = str_iva + ''.join([' ' for _ in range(len_total - len(payment['iva']))]) + payment['iva']
    return [str_total, str_efectivo, str_cambio, str_iva]

def main():
    order_data = dict(
        id=123,
        business_name='Cuca y Lupe',
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
    WIDTH = 48
    lines = list()
    # Adjust Header
    lines.append(format_line(order_data['business_name'], WIDTH))
    lines.append(format_line(order_data['business_rfc'], WIDTH, 'R.F.C '))
    lines.append(format_line(f"{order_data['branch_name']} ({order_data['branch_id']})", WIDTH, 'Suc. '))
    lines.append(format_line(f"{order_data['branch_address']['street']} {order_data['branch_address']['number']}", WIDTH))
    lines.append(format_line(f"{order_data['branch_address']['suburb']} C.P. {order_data['branch_address']['cp']}", WIDTH))
    lines.append([''.join(['-' for _ in range(WIDTH)])])
    # Adjust Articles
    str_cantidad = 'Cant  '
    str_total = 'Total   '
    str_articulo = 'Artículo'.ljust(WIDTH-len(str_cantidad)-len(str_total), ' ')
    lines.append([str_cantidad+str_articulo+str_total])
    lines.append(format_items(order_data['items'], WIDTH, str_cantidad, str_total, str_articulo))
    # Adjust Payment
    lines.append(format_payment(order_data['payment'], len(str_total)))
    # Adjust Footer
    lines.append(format_line(order_data['cashier_name'], WIDTH, 'Le atendió: '))
    lines.append([order_data['date_and_time'] + ' SUC. ' + str(order_data['branch_id'])])
    lines.append(format_line(str(order_data['id']), WIDTH, '***Folio: ' + ''.join(['0' for _ in range(8 - len(str(order_data['id'])))]), '***'))

    for line in lines:
        for l in line:
            print(l)

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
