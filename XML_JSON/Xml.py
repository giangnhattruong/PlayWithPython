import xml.etree.ElementTree as ET

data = '''
<data>
    <people>
        <person>
            <name>James</name>
            <email isAgent="yes">james007@mig.com</email>
        </person>
        <person>
            <name>Wayne</name>
            <email isAgent="no">batman@gothem.com</email>
        </person>
    </people>
</data>
'''

tree = ET.fromstring(data)
personList = tree.findall('people/person')
print('Person count:', len(personList))

for person in personList:
    print('Name:', person.find('name').text)
    print('Attribute:', person.find('email').get('isAgent'))