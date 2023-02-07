import time
from bs4 import BeautifulSoup
import requests

html_file=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=')
soup= BeautifulSoup(html_file.text,'lxml')
job_list=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
jobs={}
print("Jobs List :")
for job_card in job_list:
     job=job_card.find('ul',class_='list-job-dtl clearfix')
     job_description=" ".join(job.find_all('li')[0].text.split())
     job_skils="".join(job.find_all('li')[1].text.split())
     job_infos=job_card.header.h2.a['href']
     published_date=job_card.find('span',class_='sim-posted').span.text
     # you can acces attributs of an html element using the ['attribute name']
     if (job_description.count(':')>1):
          jobs[job_description.split(':')[2].replace(',',' ').replace('... More Details','')+'\n'+job_infos]=job_skils.strip().split(':')[1].split(',')
     else:
          jobs[job_description.split(':')[1].replace(',','').replace('... More Details','')+'\n'+job_infos] =job_skils.split(':')[1].split(',')
          print (f'''
     Company Name:{job_card.find('h3',class_='joblist-comp-name').text.replace('(More Jobs)','').strip()}
     Job Description :{job_description.split(':')[1]}
     Job Required Skills :{job_skils.replace('KeySkills:','')}   
     More Infos : {job_infos}
     Published date:{published_date}
     ''')
skils_list=[]
n=int(input(">"))
for i in range(n):
     s=input("skill that u are familiar with>")
     skils_list.append(s)


def find_jobs():
     job_desc_matched=[]
     print("searching for job opportunity \npending ...")
     for desc,skills in jobs.items():
          skill_nb = 0
          for skill in skills:
               if skill in skils_list :
                    skill_nb+=1
          if ((skill_nb>2) & (desc not in job_desc_matched)):
               job_desc_matched.append(desc)
     if len(job_desc_matched)>0:
          print('Congrats , you have big chance for those jobs  :\n')
          for j,i in enumerate(job_desc_matched) :
               print(i)
               print('*******************')
               with open(f'Jobs/{j}.txt','w') as file:
                    file.write(i)
                    file.write(jobs[i])

     else:
          print('Sorry ,you have no job description ...')



if __name__== '__main__':
     while True:
          find_jobs()
          time_wait = 10*60
          print(f'waiting {time_wait} minutes ... ')
          time.sleep(time_wait)
