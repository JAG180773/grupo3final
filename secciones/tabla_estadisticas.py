# secciones/tabla_estadisticas.py
import streamlit as st
import pandas as pd
import folium
import numpy as np
import plotly.express as px
from folium.plugins import HeatMap

def generar_tabla_estadisticas(df3, region_seleccionada, provincia_seleccionada, distrito_seleccionado):
    if df3.empty:
        st.warning("No hay datos disponibles para mostrar estadísticas.")
        return  # No mostrar tabla si no hay datos disponibles

    # Título centrado con fondo naranja y letras negras en negrita
    st.markdown("""
        <style>
            .titulo-estadisticas {
                background-color: orange;
                color: black;
                font-weight: bold;
                padding: 10px;
                text-align: center;
                font-size: 22px;  # Ajustado al tamaño de fuente de "Entidad Administradora"
                border-radius: 10px;
                margin-bottom: 20px;
                margin-top: 20px;  # Añadido margen superior
            }
        </style>
        <div class="titulo-estadisticas">Estadísticas Resumidas</div>
    """, unsafe_allow_html=True)
    
    # Crear el diccionario con las estadísticas
    estadisticas = {
        "Total de Centros en Región": df3[df3['region'] == region_seleccionada].shape[0],
        "Total de Centros en Provincia": df3[(df3['region'] == region_seleccionada) & (df3['provincia'] == provincia_seleccionada)].shape[0],
        "Total de Centros en Distrito": df3[(df3['region'] == region_seleccionada) & (df3['provincia'] == provincia_seleccionada) & (df3['distrito'] == distrito_seleccionado)].shape[0]
    }

    # Añadir la sección de estadísticas con fondo gris y texto blanco
    st.markdown("""
        <style>
            .estadisticas-box {
                background-color: #808080;
                color: white;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            .estadisticas-box .metric {
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Mostrar las métricas dentro del marco con fondo gris
    for key, value in estadisticas.items():
        if value > 0:
            st.markdown(f"""
                <div class="estadisticas-box">
                    <div class="metric"><strong>{key}:</strong> {value}</div>
                </div>
            """, unsafe_allow_html=True)
