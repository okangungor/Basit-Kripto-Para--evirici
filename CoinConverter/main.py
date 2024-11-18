import streamlit as st
import requests

adet = st.number_input("")
adet = int(adet)
liste=[]

response=requests.get('https://api.coinlore.net/api/tickers/')
veri=response.json()

coinler=veri.get("data")
coins = len(coinler)

options = []
for i in range(0, coins):
    options.append((coinler[i])["name"])
secim = st.selectbox('', options)

secilen = None
for x in coinler:
    if x["name"] == secim:
        secilen = dict(x)

fiyat1=(float(secilen["price_usd"]))

for i in range(0, coins):
    options.append((coinler[i])["name"])
secim2 = st.selectbox("", options)

secilen2 = None
for x in coinler:
    if x["name"] == secim2:
        secilen2 = dict(x)

fiyat2=(float(secilen2["price_usd"]))

st.write((fiyat1*adet)/fiyat2)

