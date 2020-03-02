
# coding: utf-8

# In[7]:


import urllib
import json
import pandas as pd

# Retrieve the metadata for this dataset:

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
params = { "id": "78c88292-5375-4373-a687-788a5ff19077", "limit": "1000"}
response = urllib.request.urlopen(url, data=bytes(json.dumps(params), encoding="utf-8"))
package = json.loads(response.read())

#print(package["result"])



# In[8]:


#retrieve the data content for the first resource in the datastore:

for idx, resource in enumerate(package["result"]["resources"]):
    #if resource["datastore_active"]:
        url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
        p = { "id": resource["id"], "limit" : "1000"}
        r = urllib.request.urlopen(url, data=bytes(json.dumps(p), encoding="utf-8"))
        data = json.loads(r.read())
        df = pd.DataFrame(data["result"]["records"])
    
        break
        
#Here is the data        
#df


# In[9]:


df.info()
df.describe()


# In[10]:


#Changing the year to date time 
pd.to_datetime(df.Year, format='%Y')


# In[34]:


#let's look at the overall trend in the GTA
annual =df.groupby(["Year"]).agg({"# Positive":"sum", "Total BLTs": "sum"})



annual.plot(kind = "area", stacked = False, title = 'Black Legged Ticks (BLTs) in the GTA - Positive for Lyme vs Total')


# In[21]:


#Now lets zoom in to see what's up in each park

by_park= df.groupby(["Year","Park Location"]).agg({"# Positive":"sum", "Total BLTs": "sum"})
by_park


# In[35]:



#Looks like there are a lot of counts of less than 5 total BLTs in a park 
#This will make the per-park trend hard to visualize against the much higher counts in some parks. 
#Let's clean those out and only look at Park/Years with counts over five
df_nozero=df[df["Total BLTs"]>5]
df_nozero


# In[25]:


#Now it's going to be easier to visualize because it only inludes park-year pairs with over 5 ticks counted
df_nozero.groupby(["Park Location","Year"]).agg({"Total BLTs":"sum", "# Positive":"sum"})


# In[36]:


#Making a new df that only has the columns we need
df_clean = df_nozero[["Park Location","Year","# Positive", "Total BLTs"]]


# In[37]:


#Grouping by year and park location
df_cleangrouped = df_clean.groupby(["Year",'Park Location'])
totals = df_cleangrouped.sum()


# In[38]:


import pandas as pd

# Creating a pivot to make the results easier to plot

result_BLTs = pd.pivot_table(totals, values=[ 'Total BLTs'], index=['Year'],
                    columns=['Park Location'], aggfunc=sum)
result_positives = pd.pivot_table(totals, values=[ "# Positive"], index=['Year'],
                    columns=['Park Location'], aggfunc=sum)


# In[39]:




my_plot = result_positives.plot(kind='area', stacked = False, legend=True, title= "Lyme disease Carriers per park", sort_columns=True).legend(bbox_to_anchor=(1,1))
from matplotlib import pyplot as plt
plt.xticks([2015,2016,2017, 2018, 2019])


# In[40]:


my_plot = result_BLTs.plot(kind='area', stacked = False, legend=True, title= "Count of Black Leg Ticks per park", sort_columns=True).legend(bbox_to_anchor=(1,1))

from matplotlib import pyplot as plt
plt.xticks([2015,2016,2017, 2018, 2019])
plt.ylim([5, 125])
        

