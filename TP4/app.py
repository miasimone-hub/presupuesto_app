import streamlit as st
from datetime import datetime
import mi_negocio
import calculos
import pdf_presupuesto

st.title("Kiosquin :3")
st.write(f"Rubro: despensa y kiosco")

cliente = st.text_input("Nombre del cliente:")
st.subheader("Seleccione sus productos")

nombres = []
cantidades = []
precios_unitarios = []

col1, col2 = st.columns(2)
p1 = col1.selectbox("Producto 1", mi_negocio.productos, key="p1")
c1 = col2.number_input("Cantidad 1", min_value=0, step=1, key="c1")
if c1 > 0:
    pos = calculos.buscar_posicion(mi_negocio.productos, p1)
    nombres.append(p1)
    cantidades.append(c1)
    precios_unitarios.append(mi_negocio.precios[pos])

col3, col4 = st.columns(2)
p2 = col3.selectbox("Producto 2", mi_negocio.productos, key="p2")
c2 = col4.number_input("Cantidad 2", min_value=0, step=1, key="c2")
if c2 > 0:
    pos = calculos.buscar_posicion(mi_negocio.productos, p2)
    nombres.append(p2)
    cantidades.append(c2)
    precios_unitarios.append(mi_negocio.precios[pos])


col5, col6 = st.columns(2)
p3 = col5.selectbox("Producto 3", mi_negocio.productos, key="p3")
c3 = col6.number_input("Cantidad 3", min_value=0, step=1, key="c3")
if c3 > 0:
    pos = calculos.buscar_posicion(mi_negocio.productos, p3)
    nombres.append(p3)
    cantidades.append(c3)
    precios_unitarios.append(mi_negocio.precios[pos])

forma_pago = st.radio("Forma de pago", [calculos.EFECTIVO, calculos.TRANSFERENCIA])

if len(cantidades) > 0:
    subtotal = calculos.calcular_subtotal(cantidades, precios_unitarios)
    descuento = calculos.calcular_descuento(subtotal, forma_pago)
    monto_desc = subtotal - descuento
    iva = calculos.calcular_iva(monto_desc)
    total = calculos.calcular_total(subtotal, descuento, iva)

    st.subheader("Resumen")
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Descuento: ${descuento:.2f}")
    st.write(f"IVA: ${iva:.2f}")
    st.write(f"TOTAL: ${total:.2f}")

    if cliente.strip() == "":
        st.warning("Ingrese el nombre del cliente para descargar el PDF.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        pdf_bytes = pdf_presupuesto.generar_pdf(
            mi_negocio.NOMBRE_NEGOCIO,
            mi_negocio.RUBRO,
            cliente,
            fecha,
            nombres,
            cantidades,
            precios_unitarios,
            subtotal,
            descuento,
            iva,
            total,
            forma_pago
        )
        st.download_button("Descargar PDF", data=pdf_bytes, file_name="presupuesto.pdf", mime="application/pdf")
else:
    st.info("Seleccione al menos un producto con cantidad mayor a 0.")

    