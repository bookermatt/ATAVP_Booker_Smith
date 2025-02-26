import numpy as np

# Define range of Mach numbers
M_values = np.arange(0.0, 4.01, 0.01)
gamma_range = [1.4, 1.33, 1.3]

# Compressible flow equations
def t_ttotal(M, gamma):
    return (1 + (gamma - 1) / 2 * M**2) ** -1

def p_ptotal(M, gamma):
    return (1 + (gamma - 1) / 2 * M**2) ** (-gamma / (gamma - 1))

def rho_rhototal(M, gamma):
    return (1 + (gamma - 1) / 2 * M**2) ** (-1 / (gamma - 1))

def a_astar(M, gamma):
    return ((1 / M) * ((2 / (gamma + 1)) * (1 + (gamma - 1) / 2 * M**2)) ** ((gamma + 1) / (2 * (gamma - 1))))

def mfp(M, gamma):
    return (M / np.sqrt((gamma + 1) / 2)) * ((1 + (gamma - 1) / 2 * M**2) ** (-((gamma + 1) / (2 * (gamma - 1)))))

# Open file to create the LaTeX table
latex_filename = "compressible_flow_tables.tex"

# General formatting stuff
with open(latex_filename, "w") as file:
    file.write(r"""\documentclass{article}
\usepackage{longtable}  % Allows tables to continue across pages
\usepackage{tabularx}   % Adjusts column widths
\usepackage{geometry}   % Sets 1-inch margins
\usepackage{booktabs}   % Improve table formatting
\geometry{margin=1in}   % 1-inch margins
\begin{document}
""")

    for gamma in gamma_range:
        file.write(f"\\section*{{Compressible Flow Table for $\\gamma = {gamma}$}}\n")
        file.write(r"""\begin{longtable}{cccccc}

\toprule
$M$ & $T/T_t$ & $P/P_t$ & $\rho/\rho_t$ & $A/A^*$ & $MFP\sqrt{R/g_c}$ \\
\midrule
\endfirsthead
\multicolumn{6}{c}{~} \\
\toprule
$M$ & $T/T_t$ & $P/P_t$ & $\rho/\rho_t$ & $A/A^*$ & $MFP\sqrt{R/g_c}$ \\
\midrule
\endhead
""")

        # Generate table rows
        for M in M_values:
            try:
                t_ratio = t_ttotal(M, gamma)
                p_ratio = p_ptotal(M, gamma)
                rho_ratio = rho_rhototal(M, gamma)
                a_ratio = a_astar(M, gamma)
                mfp_value = mfp(M, gamma)
                
                file.write(f"{M:.2f} & {t_ratio:.4f} & {p_ratio:.4f} & {rho_ratio:.4f} & {a_ratio:.4f} & {mfp_value:.4f} \\\\\n")
            except ZeroDivisionError:
                continue  # Skip values where calcs are undefined

        # Close LaTeX table
        file.write(r"""\bottomrule
\caption{Compressible flow properties for $\gamma = """ + f"{gamma}" + r"""$.}
\end{longtable}


""")

    # Close document
    file.write(r"\end{document}")

print(f"LaTeX table successfully written to {latex_filename}")
