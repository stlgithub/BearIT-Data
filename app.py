import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from datetime import datetime

def get_db_connection(username, password):
    connection = mysql.connector.connect(
        host='localhost',
        user=username,
        password=password,
        database='popup_myynti'
    )
    return connection

def validate_login(username, password):
    try:
        connection = get_db_connection(username, password)
        connection.close()
        return True
    except mysql.connector.Error as err:
        return False

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.use_csv = False

if not st.session_state.logged_in and not st.session_state.use_csv:
    st.title("Input username and password or skip login")
    tunnus = st.text_input("Username")
    salasana = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if validate_login(tunnus, salasana):
                st.session_state.logged_in = True
                st.session_state.username = tunnus
                st.session_state.password = salasana
                st.success("Login successful")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")
    with col2:
        if st.button("Skip Login"):
            st.session_state.use_csv = True
            st.success("Skipped login")
            st.experimental_rerun()

def insert_data(query, values):
    connection = get_db_connection(st.session_state.username, st.session_state.password)
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
    connection = get_db_connection(st.session_state.username, st.session_state.password)
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data(query):
    if st.session_state.use_csv:
        if "asiakas" in query.lower():
            return pd.read_csv('asiakas.csv')
        elif "myynti" in query.lower():
            return pd.read_csv('myynti.csv')
        elif "tuotekategoriat" in query.lower():
            return pd.read_csv('tuotekategoriat.csv')
        elif "tuotteet" in query.lower():
            return pd.read_csv('tuotteet.csv')
    else:
        connection = get_db_connection(st.session_state.username, st.session_state.password)
        df = pd.read_sql(query, connection)
        connection.close()
        return df

def update_data(table_name, record_id, values):
    connection = get_db_connection(st.session_state.username, st.session_state.password)
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

if st.session_state.logged_in or st.session_state.use_csv:
    st.sidebar.title("Navigaatio")
    page = st.sidebar.selectbox("Valitse sivu:", ["Asiakas", "Myynti", "Datan Syöttö", "Datan Poisto", "Datan Muokkaus", "Tietokannat"])

    def page_asiakas():
        st.dataframe('asiakas.csv')
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
        pv_myynti = df2.groupby('pvm').size().reset_index(name='sales_count')
        month_myynti = df2.groupby(df2['aika'].dt.to_period('M')).size().reset_index(name='sales_count')
        dayofweek_myynti = df2.groupby(df2['aika'].dt.day_name()).size().reset_index(name='sales_count')
        busiest_day = dayofweek_myynti.loc[dayofweek_myynti['sales_count'].idxmax()]

        col1, col2, col3 = st.columns(3)
        with col1:
            fig = px.line(pv_myynti, x='pvm', y='sales_count', title='Myyntien kehitys päivittäin')
            st.plotly_chart(fig)
        with col2:
            fig = px.line(month_myynti, x='aika', y='sales_count', title='Myyntien kehitys kuukausittain')
            st.plotly_chart(fig)
        with col3:
            fig = px.bar(dayofweek_myynti, x='aika', y='sales_count', title='Myyntien kehitys viikonpäivittäin')
            st.plotly_chart(fig)
            st.write("Busiest day of the week for sales:", busiest_day['aika'])
            st.write("Number of sales on busiest day:", busiest_day['sales_count'])

    def page_datan_syotto():
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name:
            columns = [col.strip() for col in insert_queries[table_name].split('(')[1].split(')')[0].split(',')]
            inputs = {}
            for column in columns:
                inputs[column] = st.text_input(column)

            if st.button("Insert data"):
                values = tuple(inputs[col] for col in columns)
                insert_data(insert_queries[table_name], values)
                st.success(f'Data inserted into {table_name}')

    def page_datan_poisto():
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name:
            record_id = st.text_input(f"Anna poistettavan tietueen ID ({list(delete_queries[table_name].split()[3])[-2]}):")
            if st.button("Poista data"):
                delete_data(delete_queries[table_name], (record_id,))
                st.success(f'Data deleted from {table_name}')

    def page_datan_muokkaus():
        table_name = st.selectbox("Valitse taulu:", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        if table_name:
            record_id = st.text_input(f"Anna muokattavan tietueen ID ({list(update_queries[table_name].split()[1])[-2]}):")
            columns = [col.strip() for col in insert_queries[table_name].split('(')[1].split(')')[0].split(',')]
            updates = {}
            for column in columns:
                updates[column] = st.text_input(column)
            if st.button("Päivitä data"):
                values = tuple(updates[col] for col in columns)
                update_data(table_name, record_id, values)

    def page_tietokannat():
        tables = ["asiakas", "myynti", "tuotekategoriat", "tuotteet"]
        for table in tables:
            st.write(f"Table: {table}")
            query = f"SELECT * FROM {table}"
            df = fetch_data(query)
            st.write(df)

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
        page_tietokannat()
