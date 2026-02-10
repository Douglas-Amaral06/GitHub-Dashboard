import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuração da Página (Full HD / Wide) --- (Streamlit, Pandas e Plotly para gráficos interativos)
st.set_page_config(page_title="Dashboard RH - Status", layout="wide", initial_sidebar_state="collapsed")

# Estilização CSS para dar o visual "Maturo e Tecnológico"
st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 1rem;}
        div[data-testid="stMetricValue"] {font-size: 28px; color: #e0e0e0;}
        div[data-testid="stMetricLabel"] {font-size: 14px; color: #888;}
        .stDataFrame {border: 1px solid #333; border-radius: 5px;}
    </style>
""", unsafe_allow_html=True)

# --- 1. Dados Iniciais (Baseados no seu pedido) ---
data = {
    'Empresa / Projeto': ['C.E.T', 'Latam', 'Coca Cola', 'Pepsico'],
    'Total Jovens': [125, 266, 21, 74],
    'Confirmados': [58, 166, 15, 34],
    'Não Confirmados': [65, 100, 6, 40],
    'Tel. Não Encontrado': [2, 20, 1, 8]
}

df_inicial = pd.DataFrame(data)

# --- Título ---
st.title("📊 Painel de Controle RH - Acompanhamento de Jovens")
st.markdown("---")

# --- Layout Principal ---
# Dividindo a tela: Tabela na esquerda (ou topo) e Gráfico no centro/direita
col_table, col_graph = st.columns([1, 1])

with col_table:
    st.subheader("📝 Dados Detalhados (Rê é TOP)")
    st.caption("Gráfico Automatizado.")
    
    # Tabela Editável
    df_editado = st.data_editor(
        df_inicial,
        column_config={
            "Total Jovens": st.column_config.ProgressColumn(
                "Total na Base",
                format="%d",
                min_value=0,
                max_value=300,
            ),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic"
    )

    # Cálculos Totais baseados na tabela editada
    total_base = df_editado['Total Jovens'].sum()
    total_conf = df_editado['Confirmados'].sum()
    total_pend = df_editado['Não Confirmados'].sum()
    total_error = df_editado['Tel. Não Encontrado'].sum()

    # Cards de KPI (Indicadores) logo abaixo da tabela
    st.markdown("### Resumo Global")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total na Base", total_base)
    k2.metric("Confirmados", total_conf, delta_color="normal")
    k3.metric("Pendentes", total_pend, delta_color="off")
    k4.metric("Telefone Não Encontrado", total_error, delta_color="inverse")

with col_graph:
    st.subheader("🎯 Distribuição Percentual")
    
    # Preparando dados para o Donut
    # Vamos somar os totais gerais das categorias de status
    labels = ['Confirmados', 'Não Confirmados', 'Tel. Não Encontrado']
    values = [total_conf, total_pend, total_error]
    
    # Cores inspiradas no tema Dark/Tech (Verde Neon, Laranja, Roxo/Cinza)
    colors = ['#00E396', '#FEB019', '#FF4560']

    # Criando o Gráfico Donut Moderno
    fig = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        hole=.6, # Tamanho do buraco (Donut)
        textinfo='percent',
        insidetextorientation='horizontal',
        marker=dict(colors=colors, line=dict(color='#0e1117', width=3))
    )])

    # Texto central no Donut (Total)
    fig.add_annotation(
        text=f"{total_base}",
        x=0.5, y=0.5,
        font_size=40,
        showarrow=False,
        font_color="white",
        yshift=10
    )
    fig.add_annotation(
        text="Total",
        x=0.5, y=0.5,
        font_size=14,
        showarrow=False,
        font_color="gray",
        yshift=-15
    )

    # Ajustes finos de layout do gráfico
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5, font=dict(color="white")),
        margin=dict(t=20, b=20, l=20, r=20),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

# --- Rodapé com Análise Rápida ---
st.markdown("---")
with st.expander("🔎 Análise Rápida por Empresa"):
    # Gráfico de Barras Horizontal para complementar
    fig_bar = px.bar(
        df_editado, 
        x=['Confirmados', 'Não Confirmados'], 
        y='Empresa / Projeto', 
        orientation='h',
        barmode='group',
        color_discrete_sequence=['#00E396', '#FEB019'],
        template="plotly_dark"
    )
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300)
    st.plotly_chart(fig_bar, use_container_width=True)