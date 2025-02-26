import numpy as np

# Define range of Mach numbers
M_x_values = np.arange(1.0, 4.01, 0.01)
gamma = 1.4

# total pressure ratio equation
def total_pressure_ratio(M_x, gamma):
    term1 = ((gamma + 1) * M_x**2) / ((gamma - 1) * M_x**2 + 2)
    term2 = (gamma + 1) / (2 * gamma * M_x**2 - (gamma - 1))
    P_ty_P_tx = (term1 ** (gamma / (gamma - 1))) * (term2 ** (1 / (gamma - 1)))
    return P_ty_P_tx

# normal shock relations
def normal_shock_relations(M_x, gamma):
    M_y = np.sqrt((1 + ((gamma - 1) / 2) * M_x**2) / (gamma * M_x**2 - (gamma - 1) / 2))
    P_y_P_x = (1 + 2 * gamma / (gamma + 1) * (M_x**2 - 1))
    rho_y_rho_x = ((gamma + 1) * M_x**2) / ((gamma - 1) * M_x**2 + 2)
    T_y_T_x = P_y_P_x / rho_y_rho_x
    P_ty_P_tx = total_pressure_ratio(M_x, gamma)
    return [M_x, M_y, P_ty_P_tx, P_y_P_x, rho_y_rho_x, T_y_T_x]

# Open file to create LaTeX table
filename = "normal_shock_table.tex"

with open(filename, "w") as file:
    file.write(r"""\documentclass{article}
\usepackage{longtable}  % Allows tables to continue across pages
\usepackage{tabularx}   % Adjusts column widths
\usepackage{geometry}   % Sets 1-inch margins
\usepackage{booktabs}   % Improve table formatting
\geometry{margin=1in}   % 1-inch margins
\begin{document}
""")

    file.write("\\section*{Normal Shock Table for $\\gamma = 1.4$}\n")
    file.write(r"""\begin{longtable}{cccccc}

\toprule
$M_x$ & $M_y$ & $P_{ty}/P_{tx}$ & $P_y/P_x$ & $\rho_y/\rho_x$ & $T_y/T_x$ \\
\midrule
\endfirsthead
\multicolumn{6}{c}{~} \\
\toprule
$M_x$ & $M_y$ & $P_{ty}/P_{tx}$ & $P_y/P_x$ & $\rho_y/\rho_x$ & $T_y/T_x$ \\
\midrule
\endhead
""")

    # Generate table rows
    for M_x in M_x_values:
        try:
            values = normal_shock_relations(M_x, gamma)
            file.write(f"{values[0]:.2f} & {values[1]:.4f} & {values[2]:.4f} & {values[3]:.4f} & {values[4]:.4f} & {values[5]:.4f} \\\\\n")
        except ZeroDivisionError:
            continue  # Skip values where calcs are undefined

    # Close LaTeX table
    file.write(r"""\bottomrule
\caption{Normal shock properties for $\gamma = 1.4$.}
\end{longtable}

\end{document}""")

print(f"LaTeX table successfully written to {filename}")