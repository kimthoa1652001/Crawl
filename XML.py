import mysql.connector
#import xml.etree.ElementTree as ET
from lxml import etree

#Read xml file
def parseXML(xmlFile):
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(xmlFile, parser)
    root = tree.getroot()
    return root
root = parseXML("dblp.xml")

data = []
for item in root.findall("phdthesis"):
    data_dict = {}
    #print(etree.dump(item))
    for ele in item:
        data_dict[ele.tag] = ele.text
    data.append(data_dict)
#print(data[0])
#print(data[1])
#print(data[2])
#Connect mysql
db = mysql.connector.connect(user='root', password='kimthoa165', host='127.0.0.1', database='DBLP')
#Inser function
def insert_data(author,title,year,school,page,series,ee):
    sql = "INSERT INTO Bai_bao(Authors,Titles,Years,Schools,Pages,Series,Ee)" \
          "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (author,title,year,school,page,series,ee)
    cursor = db.cursor()
    cursor.execute(sql,val)
    db.commit()
#Creat database and table
code_1 = 'CREATE DATABASE `DBLP` '
code_2 = "CREATE TABLE `DBLP`.`Bai_bao` (`Authors` VARCHAR(500) NOT NULL, " \
         "`Titles` VARCHAR(10000) NULL, `Years` VARCHAR(5) NULL, `Schools` VARCHAR(500) NULL," \
         "`Pages` VARCHAR(100) NULL, `Series` VARCHAR(500) NULL, `Ee` VARCHAR(500) NULL);"
#code_3 = "DROP TABLE `DBLP`.`Bai_bao`;"
#Run
mycursor = db.cursor()
#mycursor.execute(code_3)
mycursor.execute(code_2)

#insert data

for item in data:
    if 'author' in item:
        au = item['author']
        ####
        if 'title' in item:
            ti = item['title']
        else:
            ti = 'None'
        ###
        if 'year' in item:
            ye = item['year']
        else:
            ye = 'None'
        ###
        if 'school' in item:
            sc = item['school']
        else:
            sc = 'None'
        ###
        if 'pages' in item:
            pa = item['pages']
        else:
            pa = 'None'
        ###
        if 'series' in item:
            se = item['series']
        else:
            se = 'None'
        ###
        if 'ee' in item:
            ee = item['ee']
        else:
            ee = 'None'
        ###
        insert_data(au,ti,ye,sc,pa,se,ee)

#End
mycursor.close()
db.close()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
