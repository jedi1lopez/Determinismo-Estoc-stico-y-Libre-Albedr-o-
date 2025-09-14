# ======================================================================================================
# METADATOS ACADÉMICOS
# ======================================================================================================
# Título: Caso de Estudio: Determinismo Estocástico y Libre Albedrío - María G. y la Gestión de la Crisis del Agua en "La Esperanza"
# Autores: Dennis Zavala & Jetro Lopez
# Institución: Universidad Experimental Simón Rodríguez (UNESR)
# Programa: Doctorado en Ciencias de la Administración / Gestión Pública Ambiental
# Curso: Teorías de la Acción Social y Sistemas Complejos
# Semestre: 2025-II
# Fecha de elaboración: 2025-06-15
# Lugar: Valencia -Carabobo, Venezuela
# 
# Nota: Este código simula una intervención comunitaria realista bajo un marco teórico de agencia estructurada (Anthony Giddens) y justicia distributiva (John Rawls). 
#       Los datos son generados estocásticamente para representar escenarios posibles, no datos reales. Se usa para fines pedagógicos y de análisis crítico.
# ======================================================================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pandas as pd

# Configuración de estilo académico
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# ================================
# SIMULACIÓN: CASO DE ESTUDIO - MARÍA G. Y LA CRISIS DEL AGUA EN "LA ESPERANZA"
# ================================

# --- NOTA: SEMILLA PARA REPRODUCIBILIDAD ---
np.random.seed(42)  # Para reproducibilidad en entornos académicos y evaluación

# --- PARÁMETROS DEL CASO ---
meses = 12  # Simulación de 12 meses (Enero - Diciembre 2024)
poblacion = 5000  # Población del barrio "La Esperanza"
demanda_base = 100000  # Litros diarios promedio estimado por la comunidad
variabilidad_demanda = 0.3  # 30% de variabilidad estocástica (por clima, migración, etc.)

# Generar demanda estocástica mensual (distribución normal)
demanda_mensual = np.random.normal(loc=demanda_base, scale=demanda_base * variabilidad_demanda, size=meses)
demanda_mensual = np.clip(demanda_mensual, demanda_base * 0.5, demanda_base * 2.0)  # Límites realistas (no negativos ni absurdos)

# Generar disponibilidad de agua (con escasez extrema en algunos meses)
disponibilidad_base = 80000  # Litros diarios disponibles según infraestructura local
variabilidad_disponibilidad = 0.4
disponibilidad_mensual = np.random.normal(loc=disponibilidad_base, scale=disponibilidad_base * variabilidad_disponibilidad, size=meses)
disponibilidad_mensual = np.clip(disponibilidad_mensual, 20000, 150000)  # Límite mínimo de supervivencia

# Aplicar política de "Racionamiento Ético" de María G. (Justicia Distributiva)
# Priorización: Familias con niños <5, enfermos crónicos, adultos mayores
factor_priorizacion = 0.7  # 70% del agua disponible se asigna al grupo prioritario (ética de cuidado)
factor_general = 0.3       # 30% para el resto de la población (principio de equidad)

# Calcular asignación
asignacion_prioritaria = disponibilidad_mensual * factor_priorizacion
asignacion_general = disponibilidad_mensual * factor_general

# Calcular "nivel de servicio" (porcentaje de demanda satisfecha)
# Supuestos: Grupo prioritario representa ~40% de la demanda total; general, 60%
nivel_servicio_prioritario = np.minimum(asignacion_prioritaria / (demanda_mensual * 0.4), 1.0) * 100
nivel_servicio_general = np.minimum(asignacion_general / (demanda_mensual * 0.6), 1.0) * 100

# Generar datos de "aceptación comunitaria" (simulado como función del nivel de servicio y equidad percibida)
# Incluye ruido aleatorio para reflejar subjetividad social
aceptacion_comunitaria = (nivel_servicio_prioritario * 0.7 + nivel_servicio_general * 0.3) * 0.8 + np.random.normal(10, 5, meses)
aceptacion_comunitaria = np.clip(aceptacion_comunitaria, 0, 100)  # Límites psicológicos de aceptación

# Crear DataFrame para análisis
meses_nombres = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame({
    'Mes': meses_nombres,
    'Demanda (miles de litros)': demanda_mensual / 1000,
    'Disponibilidad (miles de litros)': disponibilidad_mensual / 1000,
    'Asignación Prioritaria (miles)': asignacion_prioritaria / 1000,
    'Asignación General (miles)': asignacion_general / 1000,
    'Nivel Servicio Prioritario (%)': nivel_servicio_prioritario,
    'Nivel Servicio General (%)': nivel_servicio_general,
    'Aceptación Comunitaria (%)': aceptacion_comunitaria
})

# ================================
# VISUALIZACIÓN DE RESULTADOS
# ================================

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Caso de Estudio: Determinismo Estocástico y Libre Albedrío\nMaría G. y la Gestión de la Crisis del Agua en "La Esperanza" (2024)', fontsize=16, fontweight='bold')

# Gráfico 1: Demanda vs Disponibilidad
ax1 = axes[0, 0]
ax1.plot(df['Mes'], df['Demanda (miles de litros)'], marker='o', label='Demanda', linewidth=2, color='#E63946')
ax1.plot(df['Mes'], df['Disponibilidad (miles de litros)'], marker='s', label='Disponibilidad', linewidth=2, color='#2A9D8F')
ax1.set_title('Demanda vs. Disponibilidad de Agua', fontsize=14)
ax1.set_ylabel('Agua (miles de litros)')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.axhline(y=demanda_base/1000, color='gray', linestyle='--', label='Demanda Media', alpha=0.7)
ax1.legend()

# Gráfico 2: Nivel de Servicio por Grupo
ax2 = axes[0, 1]
x = np.arange(len(df['Mes']))
width = 0.35
ax2.bar(x - width/2, df['Nivel Servicio Prioritario (%)'], width, label='Grupo Prioritario (Niños, Enfermos, Adultos Mayores)', color='#F4A261', edgecolor='black')
ax2.bar(x + width/2, df['Nivel Servicio General (%)'], width, label='Grupo General', color='#264653', edgecolor='black')
ax2.set_title('Nivel de Servicio por Grupo (Justicia Distributiva)', fontsize=14)
ax2.set_ylabel('Nivel de Servicio (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Mes'], rotation=45)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)
ax2.set_ylim(0, 110)

# Gráfico 3: Aceptación Comunitaria
ax3 = axes[1, 0]
ax3.fill_between(df['Mes'], df['Aceptación Comunitaria (%)'], color='#8ECAE6', alpha=0.7, edgecolor='#219EBC')
ax3.plot(df['Mes'], df['Aceptación Comunitaria (%)'], marker='o', color='#219EBC', linewidth=2)
ax3.set_title('Aceptación Comunitaria de la Política', fontsize=14)
ax3.set_ylabel('Aceptación (%)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, 100)

# Gráfico 4: Correlación entre Nivel de Servicio y Aceptación (Scatter Plot)
ax4 = axes[1, 1]
scatter = ax4.scatter(df['Nivel Servicio Prioritario (%)'], df['Aceptación Comunitaria (%)'], 
                      s=100, c=df['Nivel Servicio General (%)'], cmap='viridis', alpha=0.8, edgecolors='black')
ax4.set_title('Correlación: Servicio Prioritario vs. Aceptación\n(Color: Nivel Servicio General)', fontsize=14)
ax4.set_xlabel('Nivel de Servicio Prioritario (%)')
ax4.set_ylabel('Aceptación Comunitaria (%)')
ax4.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax4, label='Nivel de Servicio General (%)')

# Ajustar layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ================================
# IMPRESIÓN DE DATOS Y MÉTRICAS CLAVE
# ================================

print("="*80)
print("           CASO DE ESTUDIO: DETERMINISMO ESTOCÁSTICO Y LIBRE ALBEDRÍO")
print("        María G. y la Crisis del Agua en el Barrio 'La Esperanza' (2024)")
print("="*80)

print("\n--- RESUMEN EJECUTIVO ---")
print(f"Población del barrio: {poblacion} habitantes")
print(f"Duración de la simulación: {meses} meses (Enero - Diciembre 2024)")
print(f"Política implementada: Racionamiento Ético (Justicia Distributiva)")
print("   - 70% del agua disponible para grupos prioritarios (niños <5, enfermos crónicos, adultos mayores)")
print("   - 30% para el resto de la población")

print("\n--- MÉTRICAS CLAVE (PROMEDIO ANUAL) ---")
print(f"Demanda Promedio Mensual: {df['Demanda (miles de litros)'].mean():.1f} mil litros")
print(f"Disponibilidad Promedio Mensual: {df['Disponibilidad (miles de litros)'].mean():.1f} mil litros")
print(f"Nivel de Servicio Prioritario Promedio: {df['Nivel Servicio Prioritario (%)'].mean():.1f}%")
print(f"Nivel de Servicio General Promedio: {df['Nivel Servicio General (%)'].mean():.1f}%")
print(f"Aceptación Comunitaria Promedio: {df['Aceptación Comunitaria (%)'].mean():.1f}%")

print("\n--- ANÁLISIS DE LA 'AGENCIA ESTRUCTURADA' DE MARÍA G. ---")
print("María G. operó dentro de su 'cuerda' (contexto de crisis, recursos limitados, estructura social).")
print("Su 'libre albedrío' (agencia estructurada) se manifestó en:")
print("  1. Rechazar la ayuda de la ONG que exigía datos sensibles (Ejercicio de la 'Grieta Ética').")
print("  2. Implementar un sistema de racionamiento ético (Justicia Distributiva).")
print("  3. Negociar con una empresa local un trueque por transporte (Innovación responsable).")
print("Estas decisiones, aunque acotadas por la estructura, alteraron significativamente el 'eco sistémico' de la comunidad.")

print("\n--- DATOS DETALLADOS POR MES ---")
print(df.round(1).to_string(index=False))

print("\n--- CONCLUSIÓN ---")
print("Este caso demuestra que el Determinismo Estocástico no anula la libertad, sino que la redefine como 'agencia estructurada'.")
print("María G., consciente de las limitaciones estructurales (su 'cuerda'), ejerció su libertad al tomar decisiones éticas y estratégicas")
print("que transformaron la crisis en una oportunidad para fortalecer la cohesión y la justicia en su comunidad.")
print("La simulación muestra que, incluso en condiciones de alta incertidumbre, las decisiones humanas conscientes pueden generar")
print("resultados positivos y sostenibles. La 'grieta ética' y la 'justicia distributiva' no son conceptos abstractos; son herramientas")
print("prácticas para navegar lo impredecible con humanidad y responsabilidad.")

# Mostrar gráficos
plt.show()

# --- ANOTACIÓN FINAL: USO EDUCATIVO ---
# ======================================================================================================
# NOTAS PARA EL DOCENTE / ESTUDIANTE:
# ======================================================================================================
# 1. Este código es parte de un ejercicio de modelado social basado en teorías de Anthony Giddens y John Rawls.
# 2. No representa datos reales, sino escenarios probables bajo incertidumbre.
# 3. El valor pedagógico radica en visualizar cómo la ética puede guiar decisiones en contextos de escasez.
# 4. Para trabajos académicos, se recomienda complementar con entrevistas a actores locales y análisis de políticas públicas.
# 5. Autores: Dennis Zavala & Jetro Lopez | UNESR | 2024
# 6. ¡Este modelo puede ser extendido con variables de género, edad, acceso a salud o redes de apoyo!
# ======================================================================================================

# Guardar datos y gráficos (opcional - descomentar si se necesita)
# df.to_csv('simulacion_caso_maria_g.csv', index=False)
# plt.savefig('graficos_caso_maria_g.png', dpi=300, bbox_inches='tight')