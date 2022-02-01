"""
My code works as a monitor for a website called "https://wtb.kikikickz.com/" i scrap the site and stock every info i need in a list
here its shoe name plus its sizes (i've built a class object shoe which has name and size as attribute)
So i create a list of the object shoe, every 150s i scrap the website again and i compare the old list
to the new. When there is a shoe in the new list which wasn't in the old one i send a notification to a 
discord server with the name and the size of the shoe.

"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request
import time
from dhooks import Webhook, Embed
url = "https://wtb.kikikickz.com/"
hooknew = Webhook('https://discord.com/api/webhooks/916099032831656006/FozX_f_gQP2rNz_wAsNhCpMWaU3TsO4Z90D9-_UE3AUTlkoBC3XuSVP814ZyQK78Y39t')

embed = Embed(
    description='',
    color=0x5CDBF0,
    )
embed.set_footer(text="Lowkey x Kikikickz")

class Shoe:
    def __init__(self, name, size,image):
        self.name = name
        self.size = size
        self.image = image
    def show(self):
        print(self.name + " " + self.size)

        
    def new(self):
        for i in wtblist:
            same_name = i.name == self.name
            same_size = i.size == self.size   
            if same_name == True & same_size == True:
                return(1)           

        return(2)
        

def update():
    page = urllib.request.urlopen(url,timeout = 5)
    soup = bs(page, features="html.parser")
    wtb = soup.find_all('h5', {'class': 'heading'})
    size = soup.find_all('h5', {'class': 'heading-size'})
    images = soup.find_all('img')

    wtb_all= list()
    for e in wtb :
        e=e.text
        e=e.replace('\n','')
        wtb_all.append(e)

    size_all = list()
    for e in size :
        e = e.text
        e=e.replace('\n','')   
        size_all.append(e)

    image_all = list()
    for image in images:
        image_all.append(image['src'])

    update = []
    for i in range(len(wtb_all)):
        for j in range(len(size_all[i].split(","))):     
            S = Shoe(wtb_all[i],size_all[i].split(",")[j],image_all[i])
            update.append(S)
    return update

def clean():   
    new_wtb.clear()
    new_wtb_all.clear
    new_size.clear()
    new_size_all.clear()
    wtblist.clear()
    new_wtblist.clear()

wtblist = update()
a = 0 
new_wtblist = []
monitoring = True
image = ""
while  monitoring == True:
    page = urllib.request.urlopen(url,timeout = 5)
    soup = bs(page, features="html.parser")
    new_wtb = soup.find_all('h5', {'class': 'heading'})
    new_size = soup.find_all('h5', {'class': 'heading-size'})
    new_images = soup.find_all('img')
    new_wtb_all= []
    
    for e in new_wtb:
        e=e.text
        e=e.replace('\n','')
        new_wtb_all.append(e)
    new_size_all = []
    for e in new_size:
        e = e.text
        e=e.replace('\n','')
        new_size_all.append(e)

        new_image_all = list()
    for image in new_images:  
        new_image_all.append(image['src'])
    for i in range(len(new_wtb_all)):
        for j in range(len(new_size_all[i].split(","))):
            New_Shoe = Shoe(new_wtb_all[i],new_size_all[i].split(",")[j],new_image_all[i])
            isnew = New_Shoe.new()
            new_wtblist.append(New_Shoe)
           
            if isnew == 2:
                New_Shoe.show
                embed.set_author(New_Shoe.name)
                embed.set_title(New_Shoe.size)
                embed.set_thumbnail(New_Shoe.image)
                New_Shoe.show()
                print("is new")
                hooknew.send(embed=embed)
    
    print("Nombre de paires en recherche : ")
    print(len(new_wtblist))
    clean()    
    print("update :")
    print(a)
    a += 1
    wtblist = update() 
    print("Nouveau nombre de paires en recherche : ")
    print(len(wtblist))
    time.sleep(120)
    
    

    

    
