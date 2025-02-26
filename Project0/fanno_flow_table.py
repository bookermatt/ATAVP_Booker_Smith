import numpy as np

# Define range of Mach numbers
M_values = np.arange(0.01, 4.01, 0.01)
gamma = 1.4

# Fanno flow equations
def friction_length(M, gamma):
    return (1 / gamma) * ((gamma + 1) / (2 * M**2)) + np.log(M * np.sqrt((gamma + 1) / (2 + (gamma - 1) * M**2)))

def entropy_ratio(M, gamma):
    return np.log(((gamma + 1) * M**2) / (2 + (gamma - 1) * M**2))

def T_T_star(M, gamma):
    return (1 + ((gamma - 1) / 2) * M**2) / (0.5 * (gamma + 1))

def Pt_Pt_star(M, gamma):
    return ((gamma + 1) / (2 + (gamma - 1) * M**2)) ** (gamma / (gamma - 1)) / M

def P_P_star(M, gamma):
    return 1 / M

# Open file to create LaTeX table
filename = "fanno_flow_table.tex"

with open(filename, "w") as file:
    file.write(r"""\documentclass{article}
\usepackage{longtable}  % Allows tables to continue across pages
\usepackage{tabularx}   % Adjusts column widths
\usepackage{geometry}   % Sets 1-inch margins
\usepackage{booktabs}   % Improve table formatting
\geometry{margin=1in}   % 1-inch margins
\begin{document}
""")

    file.write("\\section*{Fanno Flow Table for $\\gamma = 1.4$}\n")
    file.write(r"""\begin{longtable}{ccccc}

\toprule
$M$ & $4f L^*/D$ & $I/I^*$ & $T/T^*$ & $P_t/P_t^*$ & $P/P^*$ \\
\midrule
\endfirsthead
\multicolumn{6}{c}{~} \\
\toprule
$M$ & $4f L^*/D$ & $I/I^*$ & $T/T^*$ & $P_t/P_t^*$ & $P/P^*$ \\
\midrule
\endhead
""")

    # Generate table rows
    for M in M_values:
        try:
            file.write(f"{M:.2f} & {friction_length(M, gamma):.4f} & {entropy_ratio(M, gamma):.4f} & {T_T_star(M, gamma):.4f} & {Pt_Pt_star(M, gamma):.4f} & {P_P_star(M, gamma):.4f} \\\\\n")
        except ZeroDivisionError:
            continue  # Skip values where calcs are undefined

    # Close LaTeX table
    file.write(r"""\bottomrule
\caption{Fanno line flow properties for $\gamma = 1.4$.}
\end{longtable}

\end{document}""")

print(f"LaTeX table successfully written to {filename}")
