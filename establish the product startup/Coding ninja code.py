#!/usr/bin/env python
# coding: utf-8

# # # QUESTION 1

# # Your Friend has developed the Product and he wants to establish the product startup and he is searching for a perfect location where getting the investment has a high chance. But due to its financial restriction, he can choose only between three locations -  Bangalore, Mumbai, and NCR. As a friend, you want to help your friend deciding the location. NCR include Gurgaon, Noida and New Delhi. Find the location where the most number of funding is done. That means, find the location where startups has received funding maximum number of times. Plot the bar graph between location and number of funding. Take city name "Delhi" as "New Delhi". Check the case-sensitiveness of cities also. That means, at some place instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore". For few startups multiple locations are given, one Indian and one Foreign. Consider the startup if any one of the city lies in given locations.

# In[27]:


import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('startup_funding.csv',encoding='utf-8') #reading file
sf=data.copy()
city=sf.CityLocation
city=city.dropna() # dropping nan
f={}
for i in city:
    i=str(i)
    i=i.split('/')[0].strip()                 #spliting the city names 
    if i=='Delhi':                            #correcting the city names
        i='New Delhi'
    if i=='bangalore':
        i='Bangalore'
maincity=[]

for i in city:
    if i== 'Bangalore' or i=='Mumbai' or i=='New Delhi' or i=='Gurgaon' or i=='Noida':  #filtering the cities as per req.
        maincity.append(i)
        
for i in maincity:                            #creating dictionary
    if i in f:
        f[i]+=1
    else:
        f[i]=1
c=[]
count=[]
for i in f:                              #appending the city name and its count of funding received in lists
    c.append(i)
    count.append(f[i])
count.sort(reverse=True)
print("****Top5 cities according to number of investments received****")
print()
for i in range(5):                     #printing the city name and no. of funding received
    print(c[i],count[i])  
plt.bar(c,count,width=0.2)            #ploting the bar graph
plt.ylabel('no. of investments')
plt.xlabel('<------cities------>')
plt.title("Bar Graph for Top5 cities according to number of investments ")
plt.show()


# # #QUESTION 2

# # Even after trying for so many times, your friend’s startup could not find the investment. So you decided to take this matter in your hand and try to find the list of investors who probably can invest in your friend’s startup. Your list will increase the chance of your friend startup getting some initial investment by contacting these investors. Find the top 5 investors who have invested maximum number of times (consider repeat investments in one company also). In a startup, multiple investors might have invested. So consider each investor for that startup. Ignore undisclosed investors.

# In[28]:


df=data.copy()
df['InvestorsName'].dropna(inplace=True) # dropping nan
inv=df['InvestorsName']
inv
inv=inv.values
#print(len(inv))
li=[]
for i in inv:
        a=i.split(',')   #spliting the investors
        for j in a:
            li.append(j.strip())
#print(len(li))
f={}                    # creating dictionary of investors
for i in li:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
investor=[]
times=[]
investor=sorted(f, key=f.get, reverse=True)[:5]   #sorting the dictionary and finding the top 5 investors
for i in investor:
    for j in f:
        if i==j:
            times.append(f[i])
print("******Top5 investors according to number of investments made by them******* ")
print()
for i in range(5):
    print(investor[i],times[i])  
plt.bar(investor,times,width=0.2)        #printing the bar graph
plt.xticks(rotation=90)
plt.ylabel('np. of investments')
plt.xlabel('investors')
plt.title("Bar Graph for Top5 investors according to number of investments made ")
plt.show()


# # # QUESTION 3

# # After re-analysing the dataset you found out that some investors have invested in the same startup at different number of funding rounds. So before finalising the previous list, you want to improvise it by finding the top 5 investors who have invested in different number of startups. This list will be more helpful than your previous list in finding the investment for your friend startup. Find the top 5 investors who have invested maximum number of times in different companies. That means, if one investor has invested multiple times in one startup, count one for that company. There are many errors in startup names. Ignore correcting all, just handle the important ones - Ola, Flipkart, Oyo and Paytm.

# In[30]:


x=data.copy()
x['StartupName'].fillna("",inplace=True)             #nans filled for both startupname and investor name 
x['InvestorsName'].fillna("",inplace=True)
     
        
x['StartupName'].replace("Ola Cabs",'Ola',inplace=True)
x['StartupName'].replace("Olacabs",'Ola',inplace=True)
x['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)      #important names corrected for startup
x['StartupName'].replace("Oyo Rooms","Oyo",inplace=True)
x['StartupName'].replace("OyoRooms","Oyo",inplace=True)
x['StartupName'].replace("Oyorooms","Oyo",inplace=True)
x['StartupName'].replace("Paytm Marketplace","Paytm",inplace=True)

d={}
startups=x['StartupName']
investors=x['InvestorsName']
for i in range(len(x['StartupName'])):       #use of loop to create dict entries with key as investor name
    s=startups[i]
    r=investors[i]                             
    if "," in r:
        r=r.split(",")                          
        for j in r:
            t=j.strip()
            if t!="":                           #some startups funded by many so names are stripped and then added with comma in between
                if t in d:
                    d[t]=d[t]+","+s
                else:
                    d[t]=s
    else:
        if r!="":
            if r in d:
                d[r]=d[r]+","+s
            else:
                d[r]=s

for i in d:
    temp=d[i]
    #print(temp)
    temp=temp.split(",")
    #print(temp)
    temp=list(dict.fromkeys(temp))          #this looop is been used to sepeeate every funding done by investor and then remove duplicates that refer to same startup funded different times
    #print(temp)
    d[i]=len(temp)
    #print(d[i])

investor_count=[]
#print(d.values)
for i in sorted(d.values(),reverse=True):
    if len(investor_count)==5:               #only five values used as per question to hold the count top 5 from dict d
        break
    else:
        investor_count.append(i)
investor_name=[]
for i in investor_count:
    for j in d:                                             #investor name added to the investor_name list that hold value to respoding investor_count
        if d[j]==i:
            investor_name.append(j)
print("*****Top5 investors with investment in diff startups*****")
print()
for i in range(5):
    print(investor_name[i],investor_count[i])            #values printed
plt.bar(investor_name,investor_count,width=0.2)
plt.xticks(rotation=90)
plt.ylabel('np. of investments')
plt.xlabel('investors')
plt.title("Bar Graph for Top5 investors with investment in diff startups")
plt.show()


# # # QUESTION 4

# # Even after putting so much effort in finding the probable investors, it didn't turn out to be helpful for your friend. So you went to your investor friend to understand the situation better and your investor friend explained to you about the different Investment Types and their features. This new information will be helpful in finding the right investor. Since your friend startup is at an early stage startup, the best-suited investment type would be - Seed Funding and Crowdfunding. Find the top 5 investors who have invested in a different number of startups and their investment type is Crowdfunding or Seed Funding. Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. You can find this by printing unique values from this column. There are many errors in startup names. Ignore correcting all, just handle the important ones - Ola, Flipkart, Oyo and Paytm.

# In[32]:


from collections import Counter


df5= data.copy()

#removing undisclosed investors

df5["InvestorsName"].replace("Undisclosed Investors","",inplace=True)
df5["InvestorsName"].replace("Undisclosed investors","",inplace=True)
df5["InvestorsName"].replace("", np.nan, inplace = True)
df5.dropna(inplace=True, subset=["InvestorsName"])


#removing no broker from startups

df5["StartupName"].replace("NoBroker",np.nan,inplace=True)
df5["StartupName"].dropna(inplace=True)

# correcting startup names
df5["StartupName"].replace("Flipkart.com","Flipkart",inplace=True)
df5["StartupName"].replace("Ola Cabs","Ola",inplace=True)
df5["StartupName"].replace("Olacabs","Ola",inplace=True)
df5["StartupName"].replace("Oyo Rooms","Oyo",inplace=True)

df5["StartupName"].replace("OyoRooms","Oyo",inplace=True)

df5["StartupName"].replace("Oyorooms","Oyo",inplace=True)

df5["StartupName"].replace("OYO Rooms","Oyo",inplace=True)
df5["StartupName"].replace("Paytm Marketplace","Paytm",inplace=True)

#correctibg investment types

df5["InvestmentType"].replace("SeedFunding","Seed Funding",inplace=True)
df5["InvestmentType"].replace("PrivateEquity","Private Equity",inplace=True)
df5["InvestmentType"].replace("Crowd funding","Crowd Funding",inplace=True)
df5["InvestmentType"].dropna(inplace=True)

# reset index of df5 pandas


df5.reset_index(drop=True,inplace=True)       


#creating a dictionary with startup name as key and values of unique investors only no repeated investor



dict_startups={}
for i in range(len(df5["InvestorsName"])):
    
    if (df5["InvestmentType"][i]=="Crowd Funding") | (df5["InvestmentType"][i]=="Seed Funding"):
        
    
        if  df5["StartupName"][i] not in dict_startups:

            dict_startups[df5["StartupName"][i]]=[]

            if "," not in df5["InvestorsName"][i] :

                dict_startups[df5["StartupName"][i]].append(df5["InvestorsName"][i])

            else:
                inv_each= (df5["InvestorsName"][i]).strip().split(",")
                for j in inv_each:

                    dict_startups[df5["StartupName"][i]].append(j.strip())

        else:

            if "," not in df5["InvestorsName"][i] :
                if df5["InvestorsName"][i] in dict_startups[df5["StartupName"][i]]:
                    continue

                else:

                    dict_startups[df5["StartupName"][i]].append(df5["InvestorsName"][i])

            else:

                inv_each= (df5["InvestorsName"][i]).strip().split(",")
                for j in inv_each:
                    if j in dict_startups[df5["StartupName"][i]]:
                        continue
                    else:

                        dict_startups[df5["StartupName"][i]].append(j.strip())


# creating another dictionary with keys as investor name and values as their count of investment in diff startups

inv_count_dict={}

for values in dict_startups.values():
    
      
    for x  in range(len(values)):
        
        
        if values[x] == "":
            continue
        inv_count_dict[values[x]]=inv_count_dict.get(values[x],0)+1
        
#printing top 5 investors with their count
print("****Top 5 Investors with investment in diff startups and their Investment Type is Seed Funding or Crowd Funding are:****")  
print()
inv_arr=[]
count_arr=[]

for investor, count in dict(Counter(inv_count_dict).most_common(5)).items():
    print(investor,count)
    inv_arr.append(investor)
    count_arr.append(count)
    
plt.bar(inv_arr,count_arr,width=0.2)          #ploting the bar graph
plt.xticks(rotation="vertical")
plt.xlabel("Top 5 investors")
plt.ylabel("Number of Diff Startups Funded")
plt.title("Bar Graph for Top5 investors with investment in diff startups with Crowd Funding or Seed Funding")
plt.show()


# # # QUESTION 5

# # Due to your immense help, your friend startup successfully got seed funding and it is on the operational mode. Now your friend wants to expand his startup and he is looking for new investors for his startup. Now you again come as a saviour to help your friend and want to create a list of probable new new investors. Before moving forward you remember your investor friend advice that finding the investors by analysing the investment type. Since your friend startup is not in early phase it is in growth stage so the best-suited investment type is Private Equity. Find the top 5 investors who have invested in a different number of startups and their investment type is Private Equity. Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. You can find this by printing unique values from this column.There are many errors in startup names. Ignore correcting all, just handle the important ones - Ola, Flipkart, Oyo and Paytm.

# In[33]:


x=data.copy()
x['InvestmentType'].replace('SeedFunding','Seed Funding',inplace=True)
x['InvestmentType'].replace('PrivateEquity','Private Equity',inplace=True)
x['InvestmentType'].replace('Crowd funding','Crowd Funding',inplace=True)       
x['StartupName'].replace("Ola Cabs",'Ola',inplace=True)
x['StartupName'].replace("Olacabs",'Ola',inplace=True)
x['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)     
x['StartupName'].replace("Oyo Rooms","Oyo",inplace=True)                     #important names corrected for startup
x['StartupName'].replace("OyoRooms","Oyo",inplace=True)
x['StartupName'].replace("Oyorooms","Oyo",inplace=True)
x["StartupName"].replace("OYO Rooms","Oyo",inplace=True)
x['StartupName'].replace("Paytm Marketplace","Paytm",inplace=True)
x["InvestorsName"].replace("Undisclosed Investors","",inplace=True)
x["InvestorsName"].replace("Undisclosed investors","",inplace=True)

x['StartupName'].fillna("",inplace=True)             
x['InvestorsName'].fillna("",inplace=True)                         #nans filled for both startupname and investor name 
x=x[x['InvestmentType'] == 'Private Equity']                       #filtering for private equity
     

d={}
startups=x['StartupName'].values
investors=x['InvestorsName'].values
# print(startups)
# print(investors)
for i in range(len(x['StartupName'])):                        #use of loop to create dict entries with key as investor name
#     print(i)
    s=startups[i]
    r=investors[i]
    if not('Undisclosed' in investors[i] or 'undisclosed' in investors[i]):
        if "," in r:
            r=r.split(",")                  
            for j in r:
                t=j.strip()
                if t!="":                   #some startups funded by many so names are stripped and then added with comma        
                    if t in d:
                        d[t]=d[t]+","+s
                    else:
                        d[t]=s
        else:
            if r!="":
                if r in d:
                    d[r]=d[r]+","+s
                else:
                    d[r]=s

for i in d:
    temp=d[i]
    #print(temp)
    temp=temp.split(",")
    #print(temp)
    temp=list(dict.fromkeys(temp))          #this looop is been used to separate every funding done by investor and then remove duplicates that refer to same startup funded different times
    #print(temp)
    d[i]=len(temp)
    #print(d[i])

investor_count=[]
#print(d.values)
for i in sorted(d.values(),reverse=True):
    if len(investor_count)==5:             #only five values used as per question to hold the count top 5 from dict d  
        break
    else:
        investor_count.append(i)
investor_name=[]
for i in investor_count:
    for j in d:                            #investor name added to the investor_name list that hold value to respoding investor_count                 
        if d[j]==i:
            investor_name.append(j)
print("****Top5 investors with investment in diff startups with investment type private equity*****")
print()
for i in range(5):
    print(investor_name[i],investor_count[i])  #values printed
    
plt.bar(investor_name,investor_count,width=0.2)    #ploting bar graph
plt.xticks(rotation=90)
plt.ylabel('np. of investments')
plt.xlabel('investors')
plt.title("Bar Graph for Top5 investors with investment in diff startups with Investment Type Private Equity")

plt.show()




