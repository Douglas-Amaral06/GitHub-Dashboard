import streamlit as st
import pandas as pd
import plotly.express as px

# Fullpage config CSS com tema escuro
st.set_page_config(page_title="Dashboard de Pendências", layout="wide")

# Bendito seja quem criou o CSS
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #c9d1d9 !important; }
    </style>
    """, unsafe_allow_html=True)

# 1. Dados Iniciais (Onde você pode alterar os números)
data_faltam = {
    "TAM LINHAS AEREAS S/A": 125,
    "CET": 108,
    "PEPSICO": 37,
    "COCA COLA": 14,
    "Outros": 171
}

# Confirmados / Problemas com VT
confirmados = 7 
analises = 1   

# Cálculo automatizado do Total
total_pendencias = sum(data_faltam.values())
total_geral = total_pendencias + confirmados + analises

# Título Principal
st.title("📊 Relatório Executivo de Pendências")
st.markdown("---")

# 2. Métricas de Destaque (Cards no topo)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Geral", total_geral)
col2.metric("Pendentes", total_pendencias, delta_color="inverse")
col3.metric("Confirmados", confirmados)
col4.metric("Em Análise", analises)

st.markdown("##")

# DataFrame para os gráficos
df = pd.DataFrame(list(data_faltam.items()), columns=['Empresa', 'Quantidade'])

# 3. Layout dos Gráficos
col_left, col_right = st.columns(2)

with col_left:
    # Gráfico de Pizza/Donut
    st.subheader("Distribuição Percentual")
    fig_donut = px.pie(
        df, values='Quantidade', names='Empresa', 
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_donut.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_donut, use_container_width=True)

with col_right:
    # Gráfico de Barras
    st.subheader("Pendências por Empresa")
    fig_bar = px.bar(
        df.sort_values(by='Quantidade', ascending=True), 
        x='Quantidade', y='Empresa', 
        orientation='h',
        text='Quantidade',
        color='Quantidade',
        color_continuous_scale='Blues'
    )
    fig_bar.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Qtd de Pendências",
        yaxis_title=""
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.info("Dados atualizados automaticamente via script Python.")

#CSV Salvar CSV para gerenciamento

df_report = pd.DataFrame({
    'Categoria': ['confirmados', 'analises', 'Faltam (TAM LINHAS AEREAS S/A)', 'Faltam (CET)', 'Faltam (PEPSICO)', 'Faltam(COCA COLA)', 'Faltam(Outros)'],
    'Quantidade': [7, 1, 125, 108, 37, 14, 171] 
})
#plt.show()
df_report.to_csv('relatorio_gestao_vt.csv', index=False)