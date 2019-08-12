#
# analyze.py
#  analyzes HTML-Entities.csv for basic errors and
#  creates out.html
#
# cmd.exe: set code page to 65001:
#   chcp 65001
#

html = open('out.html', 'w', encoding='utf-8')
html.write('<!DOCTYPE html>\n')
html.write('<html>');
html.write('<head>');
html.write('</head>');
html.write('<body>');
html.write('<html>');


with open('HTML-Entities.tsv', encoding='utf-8') as tsv:

   # Skip header:
     next(tsv)

     for line in tsv:

         line  = line.rstrip('\r\n')
         elems = line.split("\t")

         num   = int(elems[0])
         hex_  = elems[1]
         char  = elems[2]


         name_1= elems[3]
         name_2= elems[4]
         name_3= elems[5]
         name_4= elems[6]
         name_5= elems[7]
         name_6= elems[8]

#        s     = elems[9]
#        if 'HTML' not in s: 
#              print(s)

         if '{0:04X}'.format(num) != hex_:
            print('num {0} != hex_ {1} - {2:04X}'.format(num, hex_, num))

         if ',' in name_1:
            print(', in name_1')
         if ' ' in name_1:
            print('SP in name_1')

         html.write('{}: &#{}; &#x{}; &{};'.format(str(num), str(num), hex_, name_1));

         if name_2 != '':
            if ',' in name_2:
              print(', in name_2: ' + str(num))
            if ' ' in name_2:
               print('SP in name_2')

            html.write(' &{};'.format(name_2))

         if name_3 != '':
            if ',' in name_3:
              print(', in name_3: ' + str(num))
            if ' ' in name_3:
               print('SP in name_3: ' + str(num))
            html.write(' &{};'.format(name_3))

         if name_4 != '':
            if ',' in name_4:
              print(', in name_4: ' + str(num))
            if ' ' in name_4:
               print('SP in name_4')
            html.write(' &{};'.format(name_4))

         if name_5 != '':
            if ',' in name_5:
              print(', in name_5: ' + str(num))
            if ' ' in name_5:
               print('SP in name_5')
            html.write(' &{};'.format(name_5))

         if name_6 != '':
            if ',' in name_6:
              print(', in name_6: ' + str(num))
            if ' ' in name_6:
               print('SP in name_6: ' + str(num))
            html.write(' &{};'.format(name_6))


         html.write('<br>')

html.write('</body>');
html.write('</html>');
html.close()
