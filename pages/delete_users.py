import streamlit as st 
import requests


email=st.text_input("email",placeholder="enter email to do delete opn")
if st.button("confirm_delete"):
    res=requests.delete(f"https://fastapi-jpk3.onrender.com/delete_user/{email}") 
    if res.status_code==200:
        res_json=res.json()
        st.success(res_json)