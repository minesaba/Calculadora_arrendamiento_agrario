
import streamlit as st

def calcular_cuota(valor_tonelada_pizarra, cantidad_quintales):
   
    cuota = cantidad_quintales * (valor_tonelada_pizarra / 10)
    return cuota

st.title("Calculadora de Cuota de Arrendamiento Agrícola")

st.markdown("""
Esta herramienta permite calcular el **monto de la cuota de arrendamiento agrario** 
en base al valor de la tonelada según pizarra y la cantidad estipulada en quintales.
""")

# Entradas del usuario
valor_tonelada = st.number_input("Ingrese el valor de la tonelada según la pizarra", min_value=0.0, step=0.01)
quintales = st.number_input("Ingrese la cantidad de quintales", min_value=0.0, step=0.1)

# Botón para calcular
if st.button("Calcular cuota"):
    monto_cuota = calcular_cuota(valor_tonelada, quintales)
    st.success(f"El monto de la cuota es: **{monto_cuota:,.2f}**")

# Pie de página
st.markdown("---")
st.caption("Desarrollado por María Inés A. F.")

