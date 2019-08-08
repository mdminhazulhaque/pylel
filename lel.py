#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__license__ = "GPLv3"

"""
Copyright (c) 2019 Md. Minhazul Haque (https://github.com/mdminhazulhaque)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import requests
from tabulate import tabulate as t

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def lel_info(trackingnumber):
    response = requests.get("https://tracker.lel.asia/tracker?trackingNumber="\
        + trackingnumber\
        + "&lang=en-US")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    trace__date_rows = soup.find_all('div', {'class': 'trace__date_row'})
    data = []
    
    for trace__date_row in trace__date_rows:
        elem = trace__date_row.find("div", {"class": "trace__date"}).text
        date = " ".join(elem.split())
        
        trace__items = trace__date_row.find_all('tr', {'class': 'trace__item'})
        
        for trace__item in trace__items:
            time = trace__item.find('span', {'class':'.trace__time'}).text
            value = trace__item.find('span', {'class':'trace__event-value'}).text
            
            data.append([date, time, value])
        
    t_headers = "Date Time Description".split(" ")
    print(t(data, headers=t_headers))

if __name__ == "__main__":
    import sys
    trackingnumber = sys.argv[1]
    lel_info(trackingnumber)
