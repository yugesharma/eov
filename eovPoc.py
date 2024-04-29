import streamlit as st
st.set_page_config(page_title="EOV Extraction")

def main():
    st.header("Get yo EOV")
    query = st.text_input("Ask a question here:")
    st.write("I said "+query)


if __name__ == '__main__':
     main()