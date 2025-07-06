import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Carregar o dataset
dataset_path = "/Users/pires/Desktop/Mestrado/AVI/Momento1/airbnb_dataset_merged.csv"
dataset = pd.read_csv(dataset_path)

# Garantir que a coluna 'City' não contém valores nulos
dataset["City"] = dataset["City"].fillna("Desconhecida").str.title()  # Padronizar com inicial maiúscula

# Criar um mapeamento numérico para as cidades
cities = dataset["City"].unique()  # Obter todas as cidades únicas
city_mapping = {city: i for i, city in enumerate(cities)}
dataset["city_numeric"] = dataset["City"].map(city_mapping)  # Mapear as cidades para números

# Nova paleta de cores ajustada
color_palette = {
    "Amsterdam": "#1f77b4",  # Azul
    "Paris": "#e377c2",      # Rosa
    "London": "#7f7f7f",     # Cinzento
    "Barcelona": "#ff7f0e",  # Laranja
    "Berlin": "#2ca02c",     # Verde médio
    "Vienna": "#9467bd",     # Roxo
    "Lisbon": "#8c564b",     # Castanho
    "Rome": "#bcbd22",       # Amarelo
    "Budapest": "#264653",   # Verde escuro
    "Athens": "#2a9d8f"      # Verde claro
}

# Criar aplicação Dash
app = Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Gráfico de Coordenadas Paralelas - Airbnb", style={"textAlign": "center"}),

    # Dropdown para selecionar cidades
    html.Div([
        html.Label("Selecione as Cidades:", style={"fontSize": "16px", "marginRight": "10px"}),
        dcc.Dropdown(
            id="city-filter",
            options=[{"label": city, "value": city} for city in cities],
            value=cities.tolist(),  # Todas as cidades selecionadas por defeito
            multi=True,
            placeholder="Filtrar por cidade..."
        )
    ], style={"width": "50%", "margin": "0 auto", "padding": "10px"}),

    # Gráfico interativo
    dcc.Graph(id="parallel-coordinates-graph"),

    # Legenda das cores por cidade (com retângulos coloridos)
    html.Div([
        html.Label("Legenda das Cidades:", style={"fontSize": "16px", "fontWeight": "bold", "marginTop": "20px"}),
        html.Ul(
            [
                html.Li([
                    html.Span(style={
                        "display": "inline-block",
                        "width": "20px",
                        "height": "20px",
                        "backgroundColor": color_palette[city],
                        "marginRight": "10px",
                        "border": "1px solid black"
                    }),
                    city
                ], style={"fontSize": "14px", "marginBottom": "5px"})
                for city in cities
            ],
            style={"listStyleType": "none", "padding": "0"}
        )
    ], style={"width": "50%", "margin": "0 auto", "padding": "10px"})
])

# Callback para atualizar o gráfico com base nas cidades selecionadas
@app.callback(
    Output("parallel-coordinates-graph", "figure"),
    Input("city-filter", "value")
)
def update_graph(selected_cities):
    # Verifica se o filtro está vazio
    if not selected_cities:
        return px.parallel_coordinates(pd.DataFrame(), title="Sem dados para exibir")

    # Filtrar o dataset com base nas cidades selecionadas
    filtered_dataset = dataset[dataset["City"].isin(selected_cities)]

    # Criar gráfico de coordenadas paralelas
    fig = px.parallel_coordinates(
        filtered_dataset,
        dimensions=[
            "realSum",
            "dist",
            "metro_dist",
            "attr_index_norm",
            "rest_index_norm",
            "cleanliness_rating",
            "guest_satisfaction_overall",
        ],
        color=filtered_dataset["city_numeric"],  # Reduzido ao dataset filtrado
        color_continuous_scale=list(color_palette.values()),  # Aplicar nova paleta de cores
        labels={
            "realSum": "Preço (€)",
            "dist": "Distância ao Centro (km)",
            "metro_dist": "Distância ao Metro (km)",
            "attr_index_norm": "Índice de Atrações",
            "rest_index_norm": "Índice de Restaurantes",
            "cleanliness_rating": "Limpeza",
            "guest_satisfaction_overall": "Satisfação Geral",
            "city_numeric": "Cidade"
        },
        title="Gráfico de Coordenadas Paralelas - Comparação por Cidade"
    )

    # Remover barra de cores contínuas
    fig.update_layout(coloraxis_showscale=False)

    return fig

# Executar a aplicação
if __name__ == "__main__":
    app.run_server(debug=True)
