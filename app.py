import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from datetime import datetime

def get_db_connection():
    connection = mysql.connector.connect(
        host=st.secrets["database"]["host"],
        user=st.secrets["database"]["user"],
        password=st.secrets["database"]["password"],
        database=st.secrets["database"]["database"]
    )
    return connection

def validate_login(username, password):
    try:
        # Assuming you want to validate against a specific username and password
        return username == st.secrets["database"]["user"] and password == st.secrets["database"]["password"]
    except KeyError:
        return False

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Input username and password")
    tunnus = st.text_input("Username")
    salasana = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_login(tunnus, salasana):
            st.session_state.logged_in = True
            st.session_state.username = tunnus
            st.session_state.password = salasana
            st.success("Login successful")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def insert_data(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        st.error(f'Error inserting data: {e}')
    finally:
        cursor.close()
        connection.close()

def delete_data(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data(query):
    connection = get_db_connection()
    df = pd.read_sql(query, connection)
    connection.close()
    return df

def update_data(table_name, record_id, values):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(update_queries[table_name], values + (record_id,))
        connection.commit()
        st.success(f'Data updated successfully in {table_name}')
    except Exception as e:
        st.error(f'Error updating data: {e}')
    finally:
        cursor.close()
        connection.close()

insert_queries = {
    "Myynti": """
    INSERT INTO myynti (rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika)
    VALUES (%s, %s, %s, %s, %s)
    """,
    "Asiakas": """
    INSERT INTO asiakas (asiakas_id, puhelinnumero, sähköposti, ikä, sukupuoli)
    VALUES (%s, %s, %s, %s, %s)
    """,
    "Tuotekategoriat": """
    INSERT INTO tuotekategoriat (kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
    VALUES (%s, %s, %s, %s)
    """,
    "Tuotteet": """
    INSERT INTO tuotteet (kategoria_id, tuote_id, tuote_nimi, tukkuhinta, myyntihinta)
    VALUES (%s, %s, %s, %s, %s)
    """
}

delete_queries = {
    "Myynti": """
        DELETE FROM myynti WHERE rivi_id = %s
    """,
    "Asiakas": """
        DELETE FROM asiakas WHERE asiakas_id = %s
    """,
    "Tuotekategoriat": """
        DELETE FROM tuotekategoriat WHERE kategoria_id = %s
    """,
    "Tuotteet": """
        DELETE FROM tuotteet WHERE tuote_id = %s
    """
}

update_queries = {
    "Myynti": """
        UPDATE myynti SET rivi_id = %s, ostotapahtuma_id = %s, tuote_id = %s, asiakas_id = %s, aika = %s WHERE rivi_id = %s
    """,
    "Asiakas": """
        UPDATE asiakas SET asiakas_id = %s, puhelinnumero = %s, sähköposti = %s, ikä = %s, sukupuoli = %s WHERE asiakas_id = %s
    """,
    "Tuotekategoriat": """
        UPDATE tuotekategoriat SET kategoria_id = %s, pääkategoria_nimi = %s, alakategoria_nimi = %s, alv = %s WHERE kategoria_id = %s
    """,
    "Tuotteet": """
        UPDATE tuotteet SET kategoria_id = %s, tuote_id = %s, tuote_nimi = %s, tukkuhinta = %s, myyntihinta = %s WHERE tuote_id = %s
    """
}

if st.session_state.logged_in:
    st.sidebar.title("Navigaatio")
    page = st.sidebar.selectbox("Valitse sivu:", ["Asiakas", "Myynti", "Datan Syöttö", "Datan Poisto", "Datan Muokkaus", "Tietokannat"])

    def page_asiakas():
        query_ika_sukupuoli = "SELECT ikä, sukupuoli FROM asiakas"
        df = fetch_data(query_ika_sukupuoli)
        gender_counts = df['sukupuoli'].value_counts()
        overall_total = df['sukupuoli'].count()
        ika_sukupuoli = df[["ikä", "sukupuoli"]]

        bins = [0, 20, 30, 40, 50, 60, 70, 80, 90]
        labels = ['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90']
        ika_sukupuoli['AgeGroup'] = pd.cut(ika_sukupuoli['ikä'], bins=bins, labels=labels, right=False)
        age_group_counts = ika_sukupuoli['AgeGroup'].value_counts().sort_index()
        age_group_summary = pd.DataFrame({
            'AgeGroup': age_group_counts.index,
            'CustomerCount': age_group_counts.values
        })
        st.title('Asiakasdata')
        st.write("Kanta-asiakkaita yhteensä:")
        st.write(overall_total)

        col1, col2, col3 = st.columns([1, 2, 3], gap="small")
        with col1:
            st.write("Kanta-asiakkaat ikäryhmittäin:")
            st.write(age_group_summary)
        with col2:
            st.write("Kanta-asiakkaat sukupuolittain:")
            st.write(gender_counts)
        with col3:
            fig4 = px.histogram(ika_sukupuoli, x='AgeGroup', color='sukupuoli', barmode='stack',
                            title='Ikäryhmät sukupuolittain',
                            category_orders={'AgeGroup': labels, 'sukupuoli': ['F', 'M', 'O']})
            st.plotly_chart(fig4)

        col4, col5 = st.columns(2)
        with col4:
                fig = px.scatter(ika_sukupuoli, x='sukupuoli', y='ikä', color='sukupuoli', title='Yksilölliset iät sukupolittain')
                st.plotly_chart(fig)   
        with col5:
            fig3 = px.box(df, x='sukupuoli', y='ikä', color='sukupuoli', 
                        title='Ikäryhmät sukupuolittain',
                        category_orders={"Gender": ["Male", "Female", "Other"]})
            st.plotly_chart(fig3)

    def page_myynti():
        query_myynti = "SELECT tuote_id, ostotapahtuma_id, aika FROM myynti"


        df2 = fetch_data(query_myynti)
        st.title("Myyntidata")
        df2['aika'] = pd.to_datetime(df2['aika'])
        df2['pvm'] = df2['aika'].dt.date
        df2['klo'] = df2['aika'].dt.time
        pv_myynti = df2[["tuote_id", "ostotapahtuma_id", "pvm", "klo"]]
        pv_myynti = pv_myynti.dropna(subset=['pvm'])
        col6, col7, col8 = st.columns([2,2,2])
        col9, col10 = st.columns([2,2])
        with col6:
            st.write(pv_myynti)
        with col7:
            days_counts = pv_myynti['pvm'].value_counts()
            fig1 = px.histogram(pv_myynti, x='pvm', title='Myynti päivittäin', labels={'pvm': 'Päivämäärä', 'count': 'Ostotapahtumia'})
            st.plotly_chart(fig1)
        with col8:
            time_counts = pv_myynti['klo'].value_counts().nlargest(10)
            fig2 = px.histogram(pv_myynti, x='klo', title='Myynti kelloaikojen mukaan', labels={'klo': 'Kelloaika', 'count': 'Ostotapahtumia'})
            st.plotly_chart(fig2)
        with col9:
            fig5 = px.box(df2, x='tuote_id', y='ostotapahtuma_id', color='tuote_id', 
                        title='Myynnit tuotekategorioittain',
                        category_orders={"Gender": ["Male", "Female", "Other"]})
            st.plotly_chart(fig5)
        with col10:
                st.title("")

    def page_datan_syotto():
        st.title("Syötä dataa")
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name == "Myynti":
            rivi_id = st.text_input("Rivi ID")
            ostotapahtuma_id = st.text_input("Ostotapahtuma ID")
            tuote_id = st.text_input("Tuote ID")
            asiakas_id = st.text_input("Asiakas ID")
            aika = st.text_input("Aika")

            if st.button("Tallenna Myynti"):
                values = (rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika)
                insert_data(insert_queries[table_name], values)

        elif table_name == "Asiakas":
            asiakas_id = st.text_input("Asiakas ID")
            puhelinnumero = st.text_input("Puhelinnumero")
            sähköposti = st.text_input("Sähköposti")
            ikä = st.text_input("Ikä")
            sukupuoli = st.selectbox("Sukupuoli", ["F", "M", "O"])

            if st.button("Tallenna Asiakas"):
                values = (asiakas_id, puhelinnumero, sähköposti, ikä, sukupuoli)
                insert_data(insert_queries[table_name], values)

        elif table_name == "Tuotekategoriat":
            kategoria_id = st.text_input("Kategoria ID")
            pääkategoria_nimi = st.text_input("Pääkategoria Nimi")
            alakategoria_nimi = st.text_input("Alakategoria Nimi")
            alv = st.text_input("ALV")

            if st.button("Tallenna Tuotekategoria"):
                values = (kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
                insert_data(insert_queries[table_name], values)

        elif table_name == "Tuotteet":
            kategoria_id = st.text_input("Kategoria ID")
            tuote_id = st.text_input("Tuote ID")
            tuote_nimi = st.text_input("Tuote Nimi")
            tukkuhinta = st.text_input("Tukkuhinta")
            myyntihinta = st.text_input("Myyntihinta")

            if st.button("Tallenna Tuote"):
                values = (kategoria_id, tuote_id, tuote_nimi, tukkuhinta, myyntihinta)
                insert_data(insert_queries[table_name], values)

    def page_datan_poisto():
        st.title("Poista dataa")
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name == "Myynti":
            rivi_id = st.text_input("Rivi ID")

            if st.button("Poista Myynti"):
                delete_data(delete_queries[table_name], (rivi_id,))

        elif table_name == "Asiakas":
            asiakas_id = st.text_input("Asiakas ID")

            if st.button("Poista Asiakas"):
                delete_data(delete_queries[table_name], (asiakas_id,))

        elif table_name == "Tuotekategoriat":
            kategoria_id = st.text_input("Kategoria ID")

            if st.button("Poista Tuotekategoria"):
                delete_data(delete_queries[table_name], (kategoria_id,))

        elif table_name == "Tuotteet":
            tuote_id = st.text_input("Tuote ID")

            if st.button("Poista Tuote"):
                delete_data(delete_queries[table_name], (tuote_id,))

    def page_datan_muokkaus():
        st.title("Muokkaa dataa")
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name == "Myynti":
            record_id = st.text_input("Rivi ID")
            new_rivi_id = st.text_input("Uusi Rivi ID")
            ostotapahtuma_id = st.text_input("Ostotapahtuma ID")
            tuote_id = st.text_input("Tuote ID")
            asiakas_id = st.text_input("Asiakas ID")
            aika = st.text_input("Aika")

            if st.button("Muokkaa Myynti"):
                values = (new_rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika)
                update_data(table_name, record_id, values)

        elif table_name == "Asiakas":
            record_id = st.text_input("Asiakas ID")
            new_asiakas_id = st.text_input("Uusi Asiakas ID")
            puhelinnumero = st.text_input("Puhelinnumero")
            sähköposti = st.text_input("Sähköposti")
            ikä = st.text_input("Ikä")
            sukupuoli = st.selectbox("Sukupuoli", ["F", "M", "O"])

            if st.button("Muokkaa Asiakas"):
                values = (new_asiakas_id, puhelinnumero, sähköposti, ikä, sukupuoli)
                update_data(table_name, record_id, values)

        elif table_name == "Tuotekategoriat":
            record_id = st.text_input("Kategoria ID")
            new_kategoria_id = st.text_input("Uusi Kategoria ID")
            pääkategoria_nimi = st.text_input("Pääkategoria Nimi")
            alakategoria_nimi = st.text_input("Alakategoria Nimi")
            alv = st.text_input("ALV")

            if st.button("Muokkaa Tuotekategoria"):
                values = (new_kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
                update_data(table_name, record_id, values)

        elif table_name == "Tuotteet":
            record_id = st.text_input("Tuote ID")
            new_tuote_id = st.text_input("Uusi Tuote ID")
            kategoria_id = st.text_input("Kategoria ID")
            tuote_nimi = st.text_input("Tuote Nimi")
            tukkuhinta = st.text_input("Tukkuhinta")
            myyntihinta = st.text_input("Myyntihinta")

            if st.button("Muokkaa Tuote"):
                values = (new_tuote_id, kategoria_id, tuote_nimi, tukkuhinta, myyntihinta)
                update_data(table_name, record_id, values)

    if page == "Asiakas":
        page_asiakas()
    elif page == "Myynti":
        page_myynti()
    elif page == "Datan Syöttö":
        page_datan_syotto()
    elif page == "Datan Poisto":
        page_datan_poisto()
    elif page == "Datan Muokkaus":
        page_datan_muokkaus()
    elif page == "Tietokannat":
        page_asiakas()
        page_myynti()