# -*- coding: utf-8 -*-
"""Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WVx2Oy3etSxpANk8yS6hvLMYlyQytnj6
"""

def add(x,y):
  return x+y
result=add(3,4)
print(result)

result=lambda x,y:x+y
print(result(3,4))

result=lambda x,y:x*y
print(result(5,6))

#iterablel
lst=[1,2,3,4,5,6,7,8,9]
var_iter=iter(lst)
print(var_iter)

type(var_iter)

for i in var_iter:
  if i % 2==0:
    print(i)

#by using iter keyword check for number is <5 then add the 1 value and print the number

for i in var_iter:
  if i < 5:
    i+=1
    print(i)

ls=[1,2,3,4,56,]
var_iter=iter(ls)

for i in var_iter:
  if i < 5:
    i+=1
    print(i)

#generator
def square(i):
  for i in range(i):
    i = i+1
    return i
res = square(2)
print(res)

from google.colab import files
import pandas as pd

uploaded = files.upload()

aaa=list(uploaded.keys())[0]
df=pd.read_csv(aaa)
df

df.iloc[1:3,2:4]

df.iloc[20:23,2:4]

df.iloc[[7,5,25,38],10]

df.iloc[[7,5,25,38],2:12:8]

df.describe()

df.head(10)
df.iloc[1:50,1:5]
data = df['First Name'] == 'Preston'
ff = df['Company'] == 'Vega-Gentry'
ff,data

df.drop('Phone 2',axis=1)

df.drop('Phone 2',axis=1)

df.isnull()

import lyricsgenius

def get_song_lyrics(song_title):
    # Replace 'your_access_token' with your actual Genius API access token
    genius = lyricsgenius.Genius(CVM70mRkcZei5720__blKHQNrW_GvAK_2H6zcChnuR-NdvXAo9cjwJjtvN99Zz9O)

    # Search for the song
    song = genius.search_song(song_title)

    if song:
        return song.lyrics
    else:
        return "Sorry, I couldn't find the lyrics for that song."

def main():
    print("Welcome to the Song Lyrics Finder!")

    while True:
        song_title = input("Please enter the title of the song (or type 'exit' to quit): ")
        if song_title.lower() == 'exit':
            print("Thank you for using the Song Lyrics Finder!")
            break

        lyrics = get_song_lyrics(song_title)
        print("\nLyrics:\n")
        print(lyrics)

if _name_ == "_main_":
    main()

dict1 ={ 'Customer_id':[1,2,3,4,5,6],'Product':['Television','er','evision','Televi','Tesion','Teln']}
dict2 ={'Customer_id':[2,4,6,8],'State':['California','California','Texas','Texas']}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
df1,df2

inner_join=pd.merge(df1,df2,on='Customer_id',how='inner')
outter_join=pd.merge(df1,df2,on='Customer_id',how='outer')
outter_join,inner_join

#left_join=pd.merge(df1,df2,on='Customer_id',how='left')
right_join=pd.merge(df1,df2,on='Customer_id',how='right')
#left_join
right_join

