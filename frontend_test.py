import streamlit as st #importing streamlit pasckage
import Trilio_Blockchain_Main_Test as tbm #importing Trilio_Blockchain_Main.py

st. set_page_config(layout="wide") # full screen width for streamlit

st.title('Trilio Blockchain')

st.subheader('Addresses of Wallet 1')
if st.button('Get Private Key of wallet 1'):
    st.text(tbm.address['pve'])

if st.button('Get Public Key of wallet 1'):
    st.text(tbm.address['pbc'])

address = tbm.address
blockchain = tbm.blockchain

if st.button('click'):
    create_wallet = blockchain.Wallet.create_wallet()
    tbm.all_wallets.append(create_wallet)

st.text(tbm.all_wallets)

credit_amount = st.number_input('enter amount')
credit = blockchain.Wallet.credit_wallet(public_key=address["pbc"], amount=credit_amount)
balance = blockchain.Wallet.get_balance(private_key=address["pve"], public_key=address["pbc"])


if st.button('balance'):
    st.text(balance)
