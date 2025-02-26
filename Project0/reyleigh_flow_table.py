import numpy as np

# Define range of Mach numbers
M_values = np.arange(0.01, 4.01, 0.01)
gamma = 1.4

# Rayleigh flow equations
def phi(M, gamma):
    return (1 / M) * ((1 + gamma) / (1 + gamma * M**2))

def Tt_Tt_star(M, gamma):
    return ((gamma + 1) ** 2 * M**2) / (4 * gamma * M**2 - 2 * (gamma - 1))

def T_T_star(M, gamma):
    return (gamma + 1) / (1 + gamma * M**2)

def Pt_Pt_star(M, gamma):
    return ((gamma + 1) / (1 + gamma * M**2)) ** (1 / (gamma - 1))

def P_P_star(M, gamma):
    return (1 / M) * ((gamma + 1) / (1 + gamma * M**2))

# Open file to create LaTeX table
filename = "rayleigh_flow_table.tex"

with open(filename, "w") as file:
    file.write(r"""\documentclass{article}
\usepackage{longtable}  % Allows tables to continue across pages
\usepackage{tabularx}   % Adjusts column widths
\usepackage{geometry}   % Sets 1-inch margins
\usepackage{booktabs}   % Improve table formatting
\geometry{margin=1in}   % 1-inch margins
\begin{document}
""")

    file.write("\\section*{Rayleigh Flow Table for $\\gamma = 1.4$}\n")
    file.write(r"""\begin{longtable}{ccccc}

\toprule
$M$ & $\phi(M^2)$ & $T_t/T_t^*$ & $T/T^*$ & $P_t/P_t^*$ & $P/P^*$ \\
\midrule
\endfirsthead
\multicolumn{6}{c}{~} \\
\toprule
$M$ & $\phi(M^2)$ & $T_t/T_t^*$ & $T/T^*$ & $P_t/P_t^*$ & $P/P^*$ \\
\midrule
\endhead
""")

    # Generate table rows
    for M in M_values:
        try:
            file.write(f"{M:.2f} & {phi(M, gamma):.4f} & {Tt_Tt_star(M, gamma):.4f} & {T_T_star(M, gamma):.4f} & {Pt_Pt_star(M, gamma):.4f} & {P_P_star(M, gamma):.4f} \\\\\n")
        except ZeroDivisionError:
            continue  # Skip values where calcs are undefined

    # Close LaTeX table
    file.write(r"""\bottomrule
\caption{Rayleigh line flow properties for $\gamma = 1.4$.}
\end{longtable}

\end{document}""")

print(f"LaTeX table successfully written to {filename}")
