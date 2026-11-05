from fpdf import FPDF
import os

def generar_pdf(nombre_negocio, rubro, cliente, fecha, nombres, cantidades, precios, subtotal, descuento, iva, total, forma_pago):
    pdf = FPDF()
    pdf.add_page()
    
    
    ruta_logo = os.path.join(os.path.dirname(__file__), "loguito.png")
    pdf.image(ruta_logo, 10, 10, 30)
    
   
    pdf.set_y(12)
    
  
    pdf.set_font("helvetica", "B", 16)
    pdf.set_x(110)
    pdf.cell(90, 8, f"{nombre_negocio}", 0, 1, "R")
    
    
    pdf.set_font("helvetica", "", 10)
    pdf.set_x(110)
    pdf.cell(90, 6, f"Rubro: {rubro}", 0, 1, "R")
    pdf.set_x(110)
    pdf.cell(90, 6, f"Fecha: {fecha}", 0, 1, "R")
    pdf.set_x(110)
    pdf.cell(90, 6, f"Forma de pago: {forma_pago}", 0, 1, "R")
    
    # Dejamos espacio hacia abajo para la sección de cliente y la tabla
    pdf.set_y(48)
    
    # DATOS DEL CLIENTE
    pdf.set_font("helvetica", "", 12)
    pdf.cell(0, 8, f"Cliente: {cliente}", 0, 1)
    pdf.ln(5)
    
 
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(80, 8, "Producto", 1)
    pdf.cell(20, 8, "Cant", 1, 0, "C")
    pdf.cell(40, 8, "P. Unitario", 1, 0, "R")
    pdf.cell(40, 8, "Importe", 1, 1, "R")
    
    pdf.set_font("helvetica", "", 11)
    for i in range(len(nombres)):
        imp = cantidades[i] * precios[i]
        pdf.cell(80, 8, str(nombres[i]), 1)
        pdf.cell(20, 8, str(cantidades[i]), 1, 0, "C")
        pdf.cell(40, 8, f"${precios[i]:.2f}", 1, 0, "R")
        pdf.cell(40, 8, f"${imp:.2f}", 1, 1, "R")
        
  
    pdf.ln(5)
    pdf.set_font("helvetica", "", 11)
    pdf.cell(140, 6, f"Subtotal: ${subtotal:.2f}", 0, 1, "R")
    pdf.cell(140, 6, f"Descuento: -${descuento:.2f}", 0, 1, "R")
    pdf.cell(140, 6, f"IVA (21%): +${iva:.2f}", 0, 1, "R")
    
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(140, 8, f"TOTAL: ${total:.2f}", 0, 1, "R")
    
    return bytes(pdf.output())
