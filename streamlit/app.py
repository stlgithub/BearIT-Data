import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#------------------------------------------------------------
df = pd.read_csv("asiakas.csv")
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
st.write("Asiakkaita yhteensä:")
st.write(overall_total)
col1, col2 = st.columns(2)
with col1:
    st.write("Sukupuolijakauma:")
    st.write(gender_counts)
with col2:
    st.write("Asiakasmäärä ikäryhmittäin:")
    st.write(age_group_summary)

fig = px.scatter(ika_sukupuoli, x='sukupuoli', y='ikä', color='sukupuoli', title='Yksilölliset iät sukupolittain')
st.plotly_chart(fig)
fig1 = px.violin(ika_sukupuoli, x='sukupuoli', y='ikä', color='sukupuoli', box=True, 
                title='Ikäjakauma sukupuolittain',
                category_orders={"Gender": ["Male", "Female", "Other"]})
st.plotly_chart(fig1)
fig2 = px.histogram(ika_sukupuoli, x='ikä', color='sukupuoli', facet_col='sukupuoli', 
                   title='Ikäjakauma sukupuolittain', 
                   category_orders={"Gender": ["Male", "Female", "Other"]})
st.plotly_chart(fig2)
fig3 = px.box(df, x='sukupuoli', y='ikä', color='sukupuoli', 
             title='Ikäjakauma sukupuolittain',
             category_orders={"Gender": ["Male", "Female", "Other"]})
st.plotly_chart(fig3)

fig4 = px.histogram(ika_sukupuoli, x='AgeGroup', color='sukupuoli', barmode='stack',
                   title='Ikäjakauma sukupuolittain',
                   category_orders={'AgeGroup': labels, 'sukupuoli': ['M', 'F', 'O']})
st.plotly_chart(fig4)

fig5 = px.histogram(ika_sukupuoli, x='AgeGroup', color='sukupuoli', barmode='group',
                   title='Ikäjakauma sukupuolittain',
                   category_orders={'AgeGroup': labels, 'sukupuoli': ['M', 'F', 'O']})
st.plotly_chart(fig5)

#------------------------------------------------------------
st.title("Myynti")
df2 = pd.read_csv("myynti.csv")
df2['aika'] = pd.to_datetime(df2['aika'])
df2['pvm'] = df2['aika'].dt.date
df2['klo'] = df2['aika'].dt.time
pv_myynti = df2[["tuote_id", "ostotapahtuma_id", "pvm", "klo"]]

# Create a dropdown menu to select a value from the 'Date' column
selected_date = st.selectbox('Valitse Päivä:', pv_myynti['pvm'].unique())
# Optionally, show the dataframe filtered by the selected date
filtered_df = pv_myynti[pv_myynti['pvm'] == selected_date]
# Drop the 'Date' column from the filtered dataframe
filtered_df = filtered_df.drop(columns=['pvm'])
# Create a dropdown menu to select a value from the 'Date' column
selected_hour = st.selectbox('Valitse Aika:', filtered_df['klo'].unique())
# Display the selected datapoint
st.write('Valittu ajankohta:', selected_date, selected_hour)
# Optionally, show the dataframe filtered by the selected date
filtered_df2 = filtered_df[filtered_df['klo'] == selected_hour]
# Drop the 'Date' column from the filtered dataframe
filtered_df2 = filtered_df2.drop(columns=['klo'])
# Display the filtered data without the 'Date' column
#st.write('Filtered Data:', filtered_df) 
# Display the filtered data without the 'Date' column
st.write('Myyntitapahtumat:', filtered_df2)

fig6 = px.histogram(filtered_df, x='klo', title='Myyntitapahtumat tunneittain')
st.plotly_chart(fig6)

# Anna valita per ostotapahtuma / päivä. Kun päivä valittu printtaa kaikki ja anna vaihtoehto tarkentaa tunnittain.
# Parempi fig? -> ehkä kattoo joka tunnin päivältä ja siihen line graph + Kato tuote nimi ja matchaa se tuote id:hen toisesta csv:Stä?
#------------------------------------------------------------

#df3 = pd.read_csv("tuotekategoriat.csv")
#st.write(df3)
#df4 = pd.read_csv("tuotteet.csv")
#st.write(df4)
#------------------------------------------------------------
# FILUJEN UPLOADAUS - JOS HALUU?
#uploaded_file = st.file_uploader("Upload your file here")
#if uploaded_file:
#    df = pd.read_csv(uploaded_file)
#    st.write(df)
#------------------------------------------------------------