import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import mysql.connector
from datetime import datetime
#------------------------------------------------------------
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

# Login form
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
    cursor.execute(query, values)
    connection.commit()
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
    
# Function to update data in the database
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
    VALUES (%s, %s, %s, %s, %s)
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
    # Add additional queries for other databases/tables here
}

update_queries = {
    "Myynti": """
        UPDATE myynti SET rivi_id = %s, ostotapahtuma_id = %s, tuote_id = %s, asiakas_id = %s, aika = %s WHERE rivi_id = %s
    """,
    "Asiakas": """
        UPDATE asiakas SET asiakas_id = %s, puhelinnumero = %s, sähköposti = %s, sukupuoli = %s = %s WHERE asiakas_id = %s
    """,
    "Tuotekategoriat": """
        UPDATE tuotekategoriat SET kategoria_id = %s, pääkategoria_nimi = %s, alakategoria_nimi = %s, alv = %s WHERE kategoria_id = %s
    """,
    "Tuotteet": """
        UPDATE tuotteet SET kategoria_id = %s, tuote_id = %s, tuote_nimi = %s, tukkuhinta = %s, myyntihinta = %s WHERE tuote_id = %s
    """
    # Add additional queries for other databases/tables here
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

        # Fetch the data
        df2 = fetch_data(query_myynti)
        st.title("Myyntidata")
        df2['aika'] = pd.to_datetime(df2['aika'])
        df2['pvm'] = df2['aika'].dt.date
        df2['klo'] = df2['aika'].dt.time
        pv_myynti = df2[["tuote_id", "ostotapahtuma_id", "pvm", "klo"]]
        col6, col7, col8 = st.columns([2,2,2])
        with col6:
        # Create a dropdown menu to select a value from the 'Date' column
            selected_date = st.selectbox('Valitse Päivä:', pv_myynti['pvm'].unique())
        # Optionally, show the dataframe filtered by the selected date
        filtered_df = pv_myynti[pv_myynti['pvm'] == selected_date]
        # Drop the 'Date' column from the filtered dataframe
        filtered_df = filtered_df.drop(columns=['pvm'])
        # Create a dropdown menu to select a value from the 'Date' column
        with col7:
            selected_hour = st.selectbox('Valitse Aika:', filtered_df['klo'].unique())
            checkbox_aika = st.checkbox('Käytä valittua kellonaikaa')
        with col8:
            selected_sale = st.selectbox('Valitse Ostotapahtuma:', filtered_df['ostotapahtuma_id'].unique())
            checkbox_osto = st.checkbox('Käytä valittua ostotapahtumaa')
        num_checked = sum([checkbox_aika, checkbox_osto])
        # Display the selected datapoint
        if checkbox_aika:
            st.write('Valittu ajankohta:', selected_date, selected_hour)
        elif checkbox_osto:
            st.write('Valittu ajankohta:', selected_date,"Valittu ostotapahtuma: ", selected_sale)
        else:
            st.write('Valittu ajankohta:', selected_date)
        # Optionally, show the dataframe filtered by the selected date
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
                    fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                    st.plotly_chart(fig_treemap)
                elif checkbox_osto:
                    sales_count = filtered_df3['tuote_id'].value_counts().reset_index()
                    sales_count.columns = ['Item', 'Sales Count']
                    st.write('Ostotapahtumat:', filtered_df3)
                    fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                    st.plotly_chart(fig_treemap)
                else:
                    st.write('Ostotapahtumat:', filtered_df)
                    sales_count = filtered_df['tuote_id'].value_counts().reset_index()
                    sales_count.columns = ['Item', 'Sales Count']
                    fig_treemap = px.treemap(sales_count, path=['Item'], values='Sales Count', title='Ostot tuotteittain')
                    st.plotly_chart(fig_treemap)
                with col10:
                    if checkbox_aika:
                        fig_pie = px.pie(sales_count, values='Sales Count', names='Item', title='Ostot tuotteittain')
                        st.plotly_chart(fig_pie)
                    elif checkbox_osto:
                        fig_pie = px.pie(sales_count, values='Sales Count', names='Item', title='Ostot tuotteittain')
                        st.plotly_chart(fig_pie)
                    else:
                        fig7 = px.histogram(filtered_df, x='klo')
                        st.plotly_chart(fig7)
                        fig_pie = px.pie(sales_count, values='Sales Count', names='Item', title='Ostot tuotteittain')
                        st.plotly_chart(fig_pie)
            else:
                st.title("Valitse vain yksi: kellonaika tai ostotapahtuma.")

    def page_input():
        st.title("Syötä Dataa Tietokantaan")
        selected_database = st.selectbox('Valitse taulukko:', list(insert_queries.keys()))

        if selected_database:
            st.header(f"Syötä dataa taulukkoon {selected_database}")
            if selected_database == "Myynti":
                rivi_id = st.number_input("Rivi ID", min_value=0)
                ostotapahtuma_id = st.number_input('Ostotapahtuma ID', min_value=0)
                tuote_id = st.number_input('Tuote ID', min_value=0)
                asiakas_id = st.number_input("Asiakas ID", min_value=0)
                aika = st.text_input('Aika (YYYY-MM-DD HH:MM:SS)',  value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                if st.button('Syötä Data'):
                    try:
                        aika_datetime = datetime.strptime(aika, '%Y-%m-%d %H:%M:%S')
                        values = (rivi_id, ostotapahtuma_id, tuote_id, asiakas_id, aika_datetime)
                        insert_data(insert_queries, values)
                        st.success('Datan syöttö onnistui!')
                    except Exception as e:
                        st.error(f'Virhe syöttäessä dataa: {e}')

            if selected_database == "Asiakas":
                asiakas_id2 = st.number_input("Asiakas ID", min_value=0)
                puhelinnumero = st.number_input('Puhelinnumero', min_value=0)
                sähköposti = st.text_input('Sähköposti')
                ikä = st.number_input("Ikä", min_value=0)
                sukupuoli = st.text_input("Sukupuoli")
                if st.button('Syötä Data'):
                    try:
                        values = (asiakas_id2, puhelinnumero, sähköposti, ikä, sukupuoli)
                        insert_data(insert_queries, values)
                        st.success('Datan syöttö onnistui!')
                    except Exception as e:
                        st.error(f'Virhe syöttäessä dataa: {e}')
            
            if selected_database == "Tuotekategoriat":
                kategoria_id = st.number_input("Kategoria_id", min_value=0)
                pääkategoria_nimi = st.text_input('Pääkategoria')
                alakategoria_nimi = st.text_input('Alakategoria')
                alv = st.number_input("ALV", min_value=0)
                if st.button('Syötä Data'):
                    try:
                        values = (kategoria_id, pääkategoria_nimi, alakategoria_nimi, alv)
                        insert_data(insert_queries, values)
                        st.success('Datan syöttö onnistui!')
                    except Exception as e:
                        st.error(f'Virhe syöttäessä dataa: {e}')

            if selected_database == "Tuotteet":
                kategoria_id2 = st.number_input("Kategoria ID", min_value=0)
                tuote_id = st.number_input('Tuote ID', min_value=0)
                tuote_nimi = st.text_input('Tuote Nimi')
                tukkuhinta = st.number_input("Tukkuhinta", min_value=0)
                myyntihinta = st.number_input("Myyntihinta", min_value=0)
                if st.button('Syötä Data'):
                    try:
                        values = (kategoria_id2, tuote_id, tuote_nimi, tukkuhinta, myyntihinta)
                        insert_data(insert_queries, values)
                        st.success('Datan syöttö onnistui!')
                    except Exception as e:
                        st.error(f'Virhe syöttäessä dataa: {e}')
        
    def page_delete():
        st.title(f"Poista Dataa tietokannasta.")
        selected_database = st.selectbox('Valitse tietokanta:', list(insert_queries.keys()))
        delete_id = st.number_input("Poistettavan tiedon ID", min_value=0)

        if st.button(f'Poista Data taulusta {selected_database}'):
            try:
                values = (delete_id,)
                delete_data(delete_queries[selected_database], values)
                st.success(f'Data poistettu taulusta {selected_database}')
            except Exception as e:
                        st.error(f'Virhe poistaessa dataa: {e}')
    
    def page_tietokannat():
        st.title("Tietokantanäkymä")
        table_name = st.selectbox('Valitse taulukko:', ["Asiakas", "Myynti", "Tuotekategoriat", "Tuotteet"])  # Add your table names here
        if st.button('Lataa Data'):
            try:
                data = fetch_data(f"SELECT * FROM {table_name}")
                st.dataframe(data)
            except Exception as e:
                st.error(f'Virhe hakiessa dataa: {e}')

    def page_update():
        st.title("Päivitä Dataa Tietokannassa")
        selected_table = st.selectbox('Valitse taulu:', list(update_queries.keys()))
        record_id = st.number_input("Syötä muokattavan rivin ensimmäinen ID", min_value=0)

        # Display input fields for updating data
        st.write(f"Päivitä Data taulussa {selected_table}:")
        values = {}
        for column_name in update_queries[selected_table].split("SET")[1].split(","):
            column_name = column_name.strip().split("=")[0].strip()
            values[column_name] = st.text_input(f"{column_name.capitalize()}")

        if st.button('Päivitä Data'):
            try:
                # Convert input values to appropriate types if needed
                values_to_update = tuple(values.values())
                update_data(selected_table, record_id, values_to_update)
            except Exception as e:
                st.error(f'Virhe päivittäessä dataa: {e}')
        # Parempi fig? -> ehkä kattoo joka tunnin päivältä ja siihen line graph + Kato tuote nimi ja matchaa se tuote id:hen toisesta csv:Stä?

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
    ############################Sivu joka vaan printtaa koko databaset?############################