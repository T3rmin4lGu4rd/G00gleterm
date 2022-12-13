#libraries 
import requests
from bs4 import BeautifulSoup
import sys
import getopt
import re
#Class
class Google_Terminal_Engine():#https://www.google.com/support/enterprise/static/gsa/docs/admin/current/gsa_doc_set/xml_reference/request_format.html google search parametres 
    def __init__(self,search_qry,file_extensions,site,result_num):
        self.file_extensions = file_extensions 
        self.search_qry = search_qry
        self.url = "https://www.google.com/search?q="
        self.result_num = result_num
        self.site = site
        self.sort_A_to_D = ":A:D"
        self.sort_D_to_A = ":D:A"
        self.user_agent = {"user-agent" : "192.168.1.1"}
        self.query_num = "&num="
        self.query_fileype = "filetype%3A"
        self.query_date_sort = "&sort=date"
        self.query_site = "site%3A"
#Site Research 
    def Site_Research(self):
        try:
            r = requests.get(self.url+self.search_qry+"+"+self.query_site+self.site+self.query_num+self.result_num,headers=self.user_agent)
            print(r.url)
            if r.status_code != 200 and 301:
                print("404 Not found check the search_qry")
                sys.exit(1)
            page_source = r.content
        except ConnectionError:
            print("connection error")
            sys.exit(1)
        except requests.exceptions.InvalidURL:
            print("Invalid URL error")
            sys.exit(1)
        except requests.exceptions.ConnectTimeout:
            print("Connect Timeout Error!")  
            sys.exit(1)
        except requests.exceptions.ContentDecodingError:
            print("Content Decoding Error!")
            sys.exit(1)
        except requests.exceptions.MissingSchema:
            print("Missing Schema Error! and check the search_qry")
            sys.exit(1)   
        soup = BeautifulSoup(r.content, "html.parser")
        count = 1
        for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
                links = re.split(":(?=http)",link["href"].replace("/url?q=",""))
                print(f"{count}){links[0]}")
                count+=1
#Dorking specific files include word     
    def File(self):
        try:
            r = requests.get(self.url+self.search_qry+"+"+self.query_fileype+self.file_extensions+self.query_num+str(self.result_num),headers=self.user_agent)
            print(r.url)
            if r.status_code != 200 and 301:
                print("404 Not found check the search_qry")
                sys.exit(1)
            page_source = r.content
        except ConnectionError:
            print("connection error")
            sys.exit(1)
        except requests.exceptions.InvalidURL:
            print("Invalid URL error")
            sys.exit(1)
        except requests.exceptions.ConnectTimeout:
            print("Connect Timeout Error!")  
            sys.exit(1)
        except requests.exceptions.ContentDecodingError:
            print("Content Decoding Error!")
            sys.exit(1)
        except requests.exceptions.MissingSchema:
            print("Missing Schema Error! and check the search_qry")
            sys.exit(1)   
        soup = BeautifulSoup(r.content, "html.parser")
        count = 1
        for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
                links = re.split(":(?=https)",link["href"].replace("/url?q="," "))
                linkx = (re.split("&",links[0]))
                
                print(f"{count}){linkx[0]}")
                count+=1
# Dorking files of site
    
    def Site_File(self):
        try:
            r = requests.get(self.url+self.query_site+self.site+"&"+self.query_fileype+self.file_extensions+self.query_num+str(self.result_num),headers=self.user_agent)
            print(r.url)
            if r.status_code != 200 and 301:
                print("404 Not found check the search_qry")
                sys.exit(1)
            page_source = r.content
        except ConnectionError:
            print("connection error")
            sys.exit(1)
        except requests.exceptions.InvalidURL:
            print("Invalid URL error")
            sys.exit(1)
        except requests.exceptions.ConnectTimeout:
            print("Connect Timeout Error!")  
            sys.exit(1)
        except requests.exceptions.ContentDecodingError:
            print("Content Decoding Error!")
            sys.exit(1)
        except requests.exceptions.MissingSchema:
            print("Missing Schema Error! and check the search_qry")
            sys.exit(1)   
        soup = BeautifulSoup(r.content, "html.parser")
        count = 1
        for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
                links = re.split(":(?=https)",link["href"].replace("/url?q="," "))
                linkx = (re.split("&",links[0]))
                
                print(f"{count}){linkx[0]}")
                count+=1

# Argv 
search_qry = ""
file_extension = ""
site = ""
result_num =""
helpx =""
help_text = ("""
Google T3rminal Engine V.0.1 
-q,--query        *Adds the specified query terms to the query terms in parameter q.
-s,--site         *Limits search results to documents in the specified domain, host or web directory, or excludes results from the specified location   
-f,--file         *Specifies a file format to include or exclude in the search results.
-n,--num          *Maximum number of results to include in the search results. The maximum value of this parameter is 1000.
Example : python3 G00GTERM.py -q hello -f doc -n 10
Example : python3 G00GTERM.py -s airways -f pdf -n 10 """)


# Argv elements
argv = sys.argv[1:]
try:
    options,args = getopt.getopt(argv,"q:f:s:n:",["search_qry =","file_extension =","site =","result_num ="])
except:
    print("Error Message")
for name, value in options:
    if name in ["-q"]:
        search_qry = value
    elif name in ["-f"]:
        file_extension = value
    elif name in ["-s"]:
        site = value
    elif name in ["-n"]:
        result_num = value

if len(sys.argv) == 1:
    print(IndexError,"Please check the argv")
    print(help_text)
    sys.exit()
# argv elements 
argv_1 = options[0]
argv_2 = options[1]
argv_3 = options[2]

#conditions and execute the  class
if argv_1[0] == "-q" and argv_2[0] == "-s" and argv_3[0] =="-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-q" and argv_2[0] == "-n" and argv_3[0] == "-s":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-s" and argv_2[0] == "-q" and argv_3[0] == "-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-s" and argv_2[0] == "-n" and argv_3[0] == "-q":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-q" and argv_3[0] == "-s":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-s" and argv_3[0] == "-q":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_Research()
   sys.exit()
elif argv_1[0] == "-q" and argv_2[0] == "-f" and argv_3[0] == "-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-q" and argv_2[0] == "-n" and argv_3[0] == "-f":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-f" and argv_2[0] == "-q" and argv_3[0] == "-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-f" and argv_2[0] == "-n" and argv_3[0] == "-q":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-q" and argv_3[0] == "-f":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-f" and argv_3[0] == "-q":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.File()
   sys.exit()
elif argv_1[0] == "-s" and argv_2[0] == "-f" and argv_3[0] == "-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()
elif argv_1[0] == "-s" and argv_2[0] == "-n" and argv_3[0] == "-f":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()
elif argv_1[0] == "-f" and argv_2[0] == "-s" and argv_3[0] == "-n":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()
elif argv_1[0] == "-f" and argv_2[0] == "-n" and argv_3[0] == "-s":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-f" and argv_3[0] == "-s":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()
elif argv_1[0] == "-n" and argv_2[0] == "-s" and argv_3[0] == "-f":
   execute =  Google_Terminal_Engine(search_qry,file_extension,site,result_num)
   execute.Site_File()
   sys.exit()