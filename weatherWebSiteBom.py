#!C:\Users\sebas\AppData\Local\Programs\Python\Python310\python.exe


from datetime import date
import json
import requests

def main():
    press = []
    temp = []
    windSpeed = []
    raintrance = []
    dateW = []
    
    url = 'http://www.bom.gov.au/fwo/IDN60701/IDN60701.94799.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    x = requests.get(url, headers=headers)
    y = json.loads(x.text)
    for val in y['observations']['data']:
            press.append(val['press'])
            temp.append(val['air_temp'])
            windSpeed.append(val['wind_spd_kt'])
            raintrance.append(float(val['rain_trace']))
            dateW.append(val['local_date_time'])

    
    
    # web site
    print("Content-type: text/html\n")
    #print("hola")
    print("<html>") # open html website
    # code style 
    style = """
                
                <style>
                
                
                table {
                height: auto;
                left: auto;
                margin: 20px auto;
                overflow-y: scroll;
                position: static;
                width: auto;
                }

                thead th {
                background: #45B39D;
                color: #FFF;
                font-family: 'Lato', sans-serif;
                font-size: 16px;
                font-weight: 100;
                letter-spacing: 2px;
                text-transform: uppercase;
                }

                tr {
                background: #f4f7f8;
                border-bottom: 1px solid #FFF;
                margin-bottom: 5px;
                }

                th {
                font-family: 'Lato', sans-serif;
                font-weight: 400;
                padding: 20px;
                text-align: center;
                width: auto;
                }
                td {
                font-family: 'Lato', sans-serif;
                font-weight: 400;
                padding: 20px;
                text-align: center;
                width: auto;
                }
                </style>

               
                """
    print(style)


    website = ( 
            "<body>"
            "<h1 style='text-align:center;'> Port Macquarie Weather</h1>"
            

            

            "<table  align='center' style='margin: 0px auto';>"
            
            "<thead>"
            "<tr>"
                "<th> </th>"  
                "<th> Pressure MSLhPa</th>"
                "<th> Temperature °C</th>"
                "<th> Wind Speed kts</th>"
                "<th> Rain trance mm</th>"
            "</tr>"
            "<tr>"
            "</thead>"
            "<thead>"
            "<th>Max</th>"
            
            "<td>"+ str(format(max(press), '.2f')) + "</td>"
            "<td>"+ str(format(max(temp), '.2f')) + "</td>"
            "<td>"+ str(format(max(windSpeed), '.2f')) + "</td>"
            "<td>"+ str(format(max(raintrance), '.2f')) + "</td>"
            "</tr>"
            "<tr>"
               
            "<th>Min</th>"
            "<td>"+ str(format(min(press), '.2f')) + "</td>"
            "<td>"+ str(format(min(temp), '.2f')) + "</td>"
            "<td>"+ str(format(min(windSpeed), '.2f')) + "</td>"
            "<td>"+ str(format(min(raintrance), '.2f')) + "</td>"
            

            "</tr>"
            "<tr>"

            
            "<th>Avg</th>"
            "<td>"+ str(format(average(press), '.2f')) + "</td>"
            "<td>"+ str(format(average(temp), '.2f')) + "</td>"
            "<td>"+ str(format(average(windSpeed), '.2f')) + "</td>"
            "<td>"+ str(format(average(raintrance), '.2f')) + "</td>"


            "</tr>"
            "</thead>" 
            "</table>"
            "<h2 style='text-align:center;'> Current date: "+str(date.today())+"</h2>"
            "<table  align='center' style='margin: 0px auto';>"
            
            "<thead>"
            "<tr>"
                  
                "<th> Date </th>"
                "<th> Pressure MSLhPa</th>"
                "<th> Temperature °C</th>"
                "<th> Wind Speed kts</th>"
                "<th> Rain trance mm</th>"
                
                            
            "</tr>"
            
                            
            
            
            
            

        )
    print(website)

    for i in range(0,len(dateW)):
                    print("<tr>")
                    print("<td>" + str(dateW[i]) + "</td>")
                    print("<td>" + str(format(press[i], '.2f')) + "</td>")
                    print("<td>" + str(format(temp[i], '.2f')) + "</td>")
                    print("<td>" + str(format(windSpeed[i], '.2f')) + "</td>")
                    print("<td>" + str(format(raintrance[i], '.2f')) + "</td>")
                    print("</tr>")
    
    close = """

                </thead>
                </table>
                </body>
                </html>

    """
    print(close)


   

def average(listNum: list):
    return sum(listNum) / len(listNum)


main()
  