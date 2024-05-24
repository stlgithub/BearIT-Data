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
        with col6:

            selected_date = st.selectbox('Valitse Päivä:', pv_myynti['pvm'].unique())

        filtered_df = pv_myynti[pv_myynti['pvm'] == selected_date]

        filtered_df = filtered_df.drop(columns=['pvm'])

        with col7:
            selected_hour = st.selectbox('Valitse Aika:', filtered_df['klo'].unique())
            checkbox_aika = st.checkbox('Käytä valittua kellonaikaa')
        with col8:
            selected_sale = st.selectbox('Valitse Ostotapahtuma:', filtered_df['ostotapahtuma_id'].unique())
            checkbox_osto = st.checkbox('Käytä valittua ostotapahtumaa')
        num_checked = sum([checkbox_aika, checkbox_osto])

        if checkbox_aika:
            st.write('Valittu ajankohta:', selected_date, selected_hour)
        elif checkbox_osto:
            st.write('Valittu ajankohta:', selected_date,"Valittu ostotapahtuma: ", selected_sale)
        else:
            st.write('Valittu ajankohta:', selected_date)

        filtered_df2 = filtered_df[filtered_df['klo'] == selected_hour]
        filtered_df2 = filtered_df2.drop(columns=['klo'])
        filtered_df3 = filtered_df[filtered_df['ostotapahtuma_id'] == selected_sale]
        filtered_df3 = filtered_df3.drop(columns=['ostotapahtuma_id'])
        col9, col10 = st.columns(2)
        with col9:
            if num_checked < 2:
                if checkbox_aika:
                    st.write('Ostotapahtumat:', filtered_df2)
                    sales_count = filtered_df2['tuote_id'].value_counts().reset_index()
                    sales_count.columns = ['Item', 'Sales Count']
                elif checkbox_osto:
                    sales_count = filtered_df3['tuote_id'].value_counts().reset_index()
                    sales_count.columns = ['Item', 'Sales Count']
                    st.write('Ostotapahtumat:', filtered_df3)

                else:
                    st.write('Ostotapahtumat:', filtered_df)
                    sales_count = filtered_df['tuote_id'].value_counts().reset_index()
                    sales_count.columns = ['Item', 'Sales Count']
                    fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                    st.plotly_chart(fig_treemap)
                with col10:
                    if checkbox_aika:
                        fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                        st.plotly_chart(fig_treemap)
                        fig_pie = px.pie(sales_count, values='Sales Count', names='Item', title='Ostot tuotteittain')
                        st.plotly_chart(fig_pie)
                    elif checkbox_osto:
                        fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                        st.plotly_chart(fig_treemap)
                        fig_pie = px.pie(sales_count, values='Sales Count', names='Item', title='Ostot tuotteittain')
                        st.plotly_chart(fig_pie)
                    else:
                        fig7 = px.histogram(filtered_df, x='klo')
                        st.plotly_chart(fig7)
                        df2['date'] = df2['aika'].dt.date
                        myynti_by_date = df2.groupby('date').size().reset_index(name='SalesCount')
                        fig6 = px.line(myynti_by_date, x='date', y='SalesCount', 
                                    title='Myynnin jakautuminen päivittäin')
                        st.plotly_chart(fig6)
            else:
                st.title("Valitse vain yksi: kellonaika tai ostotapahtuma.")

    def page_input():
        st.title("Syötä Dataa Tietokantaan")
        st.write("Valitse taulu johon haluat syöttää dataa:")

        table = st.selectbox("Valitse taulu", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        st.write(f"Syötetään dataa tauluun: {table}")
        
        if table == "Myynti":
            rivi_id = st.number_input("Rivi ID", min_value=0)
            ostotapahtuma_id = st.number_input("Ostotapahtuma ID", min_value=0)
            tuote_id = st.number_input("Tuote ID", min_value=0)
            asiakas_id = st.number_input("Asiakas ID", min_value=0)
            aika = st.text_input("Aika (YYYY-MM-DD HH:MM:SS)",  value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            values = (rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika)
        elif table == "Asiakas":
            asiakas_id = st.number_input("Asiakas ID", min_value=0)
            puhelinnumero = st.text_input("Puhelinnumero")
            sähköposti = st.text_input("Sähköposti")
            ikä = st.number_input("Ikä", min_value=0)
            sukupuoli = st.text_input("Sukupuoli")
            values = (asiakas_id, puhelinnumero, sähköposti, ikä, sukupuoli)
        elif table == "Tuotekategoriat":
            kategoria_id = st.number_input("Kategoria ID", min_value=0)
            pääkategoria_nimi = st.text_input("Pääkategoria nimi")
            alakategoria_nimi = st.text_input("Alakategoria nimi")
            alv = st.number_input("ALV", min_value=0)
            values = (kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
        elif table == "Tuotteet":
            kategoria_id = st.number_input("Kategoria ID", min_value=0)
            tuote_id = st.number_input("Tuote ID", min_value=0)
            tuote_nimi = st.text_input("Tuote nimi")
            tukkuhinta = st.number_input("Tukkuhinta", min_value=0)
            myyntihinta = st.number_input("Myyntihinta", min_value=0)
            values = (kategoria_id, tuote_id, tuote_nimi, tukkuhinta, myyntihinta)

        if st.button("Syötä data"):
            if all(values):
                insert_data(insert_queries[table], values)
                st.success('Datan syöttö onnistui!')
            else:
                st.error("Virhe! Muista täyttää kaikki kentät!")

    def page_delete():
        st.title("Poista Dataa Tietokannasta")
        st.write("Valitse taulu, josta haluat poistaa dataa:")

        table = st.selectbox("Valitse taulu", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        st.write(f"Poistetaan dataa taulusta: {table}")
        
        if table == "Myynti":
            rivi_id = st.number_input("Rivi ID", min_value=0)
            key_value = (rivi_id,)
        elif table == "Asiakas":
            asiakas_id = st.number_input("Asiakas ID", min_value=0)
            key_value = (asiakas_id,)
        elif table == "Tuotekategoriat":
            kategoria_id = st.number_input("Kategoria ID", min_value=0)
            key_value = (kategoria_id,)
        elif table == "Tuotteet":
            tuote_id = st.number_input("Tuote ID", min_value=0)
            key_value = (tuote_id,)
        
        if st.button("Poista data"):
            if key_value:
                delete_data(delete_queries[table], key_value)
                st.success('Datan poisto onnistui!')
            else:
                st.error("Virhe! Muista anntaa poistettava ID!")

    def page_update():
        st.title("Muokkaa Dataa Tietokannassa")
        st.write("Valitse taulu, jota haluat muokata:")

        table = st.selectbox("Valitse taulu", ["Myynti", "Asiakas", "Tuotekategoriat", "Tuotteet"])
        st.write(f"Muokataan dataa taulussa: {table}")
        
        if table == "Myynti":
            record_id = st.number_input("Rivi ID (muutettava)", min_value=0)
            rivi_id = st.number_input("Uusi Rivi ID", min_value=0)
            ostotapahtuma_id = st.number_input("Uusi Ostotapahtuma ID", min_value=0)
            tuote_id = st.number_input("Uusi Tuote ID", min_value=0)
            asiakas_id = st.number_input("Uusi Asiakas ID", min_value=0)
            aika = st.text_input("Uusi Aika (YYYY-MM-DD HH:MM:SS)",  value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            values = (rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika)
        elif table == "Asiakas":
            record_id = st.number_input("Asiakas ID (muutettava)", min_value=0)
            asiakas_id = st.number_input("Uusi Asiakas ID", min_value=0)
            puhelinnumero = st.text_input("Uusi Puhelinnumero")
            sähköposti = st.text_input("Uusi Sähköposti")
            ikä = st.number_input("Uusi Ikä", min_value=0)
            sukupuoli = st.text_input("Uusi Sukupuoli")
            values = (asiakas_id, puhelinnumero, sähköposti, ikä, sukupuoli)
        elif table == "Tuotekategoriat":
            record_id = st.number_input("Kategoria ID (muutettava)", min_value=0)
            kategoria_id = st.number_input("Uusi Kategoria ID", min_value=0)
            pääkategoria_nimi = st.text_input("Uusi Pääkategoria nimi")
            alakategoria_nimi = st.text_input("Uusi Alakategoria nimi")
            alv = st.number_input("Uusi ALV")
            values = (kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
        elif table == "Tuotteet":
            record_id = st.number_input("Tuote ID (muutettava)", min_value=0)
            kategoria_id = st.number_input("Uusi Kategoria ID", min_value=0)
            tuote_id = st.number_input("Uusi Tuote ID", min_value=0)
            tuote_nimi = st.text_input("Uusi Tuote nimi")
            tukkuhinta = st.number_input("Uusi Tukkuhinta", min_value=0)
            myyntihinta = st.number_input("Uusi Myyntihinta", min_value=0)
            values = (kategoria_id, tuote_id, tuote_nimi, tukkuhinta, myyntihinta)

        if st.button("Muokkaa dataa"):
            if all(values):
                update_data(table, record_id, values)
                st.success('Datan muokkaus onnistui!')
            else:
                st.error("Virhe! Muista täyttää kaikki kentät!")

    def page_tietokannat():
        st.title("Tietokantanäkymä")
        table_name = st.selectbox('Valitse taulukko:', ["Asiakas", "Myynti", "Tuotekategoriat", "Tuotteet"])  # Add your table names here
        if st.button('Lataa Data'):
            try:
                data = fetch_data(f"SELECT * FROM {table_name}")
                st.dataframe(data)
            except Exception as e:
                st.error(f'Virhe hakiessa dataa: {e}')

    # Page display logic
    if page == "Asiakas":
        page_asiakas()
    elif page == "Myynti":
        page_myynti()
    elif page == "Datan Syöttö":
        page_input()
    elif page == "Datan Poisto":
        page_delete()
    elif page == "Tietokannat":
        page_tietokannat()
    elif page == "Datan Muokkaus":
        page_update()