import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl"> +1 734 303 4456 </phone>
    <email hide="yes"/>
    <a href="http://www.hello.com">This web</a>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
print('Refe:',tree.find('a').text,'goes to', tree.find('a').get('href'))
