# from tkinter import *
# root=Tk()
# Mybutton=Button(root,text='click me')
# Mybutton.pack()
# root.mainloop()
#
from bs4 import BeautifulSoup
import requests
URL="https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.contents)
result = soup.find(id="ResultsContainer")
#print(result.prettify())
element_class = result.find_all("div", class_="card-content")
#print(element_class)
for elements_class in element_class:
    #print(elements_class, end="\n"*2)
    title_name= elements_class.find("h2",class_="title")
    company_name= elements_class.find("h3", class_="company")
    location_name= elements_class.find("p", class_="location")
    # print(title_name.text.strip())
    # print(company_name.text.strip())
    # print(location_name.text.strip())
    # print()

list_job=result.find_all('h2',string=lambda text:"python" in text.lower())
print(list_job)
print(len(list_job))
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in list_job
]
#print(python_job_elements)
for job_element in python_job_elements:
    print(job_element)

    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())

