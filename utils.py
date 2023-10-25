import os
import json
from datetime import datetime
import pytz
import streamlit as st
from password_strength import PasswordPolicy
from cryptography.fernet import Fernet


def pretty_title(title: str) -> None:
    """Make a centered title, and give it a red line. Adapted from
    'streamlit_extras.colored_headers' package.
    Parameters:
    -----------
    title : str
        The title of your page.
    """
    st.markdown(
        f"<h2 style='text-align: center'>{title}</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        (
            '<hr style="background-color: #ff4b4b; margin-top: 0;'
            ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">'
        ),
        unsafe_allow_html=True,
    )


def get_time():
    """return time in GMT"""
    now = datetime.now()
    g_timezone = pytz.timezone('GMT')
    g_time = now.astimezone(g_timezone)
    return g_time


def eval_password(password: str):
    """
    evaluate password according its policy
    :param password:
    :return:
    """
    policy = PasswordPolicy.from_names(length=12, uppercase=2, numbers=2, special=2)
    eval_psw = policy.test(password)
    eval_str = ','.join([str(ele) for ele in eval_psw])
    res = ""
    if 'Length' in eval_str:
        res += "Length not satisfied, "
    if 'Uppercase' in eval_str:
        res += "Uppercase not satisfied, "
    if 'Numbers' in eval_str:
        res += "Numbers not satisfied, "
    if 'Special' in eval_str:
        res += "Special not satisfied, "

    if len(eval_psw) > 0:
        return False, res
    else:
        return True, ""


def encode_payload(payload: list) -> dict:
    """
    encode payload before sending it to DB
    :param payload:
    :return:
    """
    # encrypt data
    key = Fernet(st.secrets["encryption_key"])
    current_time = get_time()

    obj = {"name": payload["name"],
           "username": payload["username"],
           "login_connection_time": str(payload["login_connection_time"]),
           "messages_QA": payload["messages_QA"],
           "messages_chat": payload["messages_chat"],
           "life_insurance_model": payload["life_insurance_model"].dict(),
           "created_at": str(current_time)}

    d_bytes = json.dumps(obj).encode('utf-8')
    # then encode dictionary using the key
    d_token = key.encrypt(d_bytes)
    payload = {"username": st.session_state["username"], "data": d_token, "created_at": str(current_time)}
    return payload