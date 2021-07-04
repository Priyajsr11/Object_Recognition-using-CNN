#!/usr/bin/python3 

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")



if plate_no == "KA 05 NB 1786":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : ANKIT SINGH 
    License No : 12345677889
    Make / Model : BABA HYUNDAI / Kia
    Registration Date : 1/12/2011
    Registering Authority : DELHI , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : NANDINI LUDBE
    License No : 098363357292
    Make / Model : Audi / A4
    Registration Date : 1/12/2014
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH:01.CT.5470":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : ROHIT CHOUHAN
    License No : 647384576526
    Make / Model : Honda / City
    Registration Date : 08/05/2019
    Registering Authority : MANDSAUR, INDIA
    Vehicle Class : MCWG
    Fuel Type : Diesel
    Engine No : RMJZC12348
    Chassis No : MAHINM2RMIJ2E85058
    Insurance Upto : 2/10/2025
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")

