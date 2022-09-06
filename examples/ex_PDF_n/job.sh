#!/bin/bash

# This job launches 3 simulations with different distribution of probability
# (Dirac, Poisson, BoseEinstein)
# The other parameters are listed below

PDFs="Dirac Poisson BoseEinstein"

for PDF in $PDFs; do
cat > input.txt << EOF

[field]
avg_n = 10
pdf_n = $PDF
cut_n = 100

[atom]
Cg = 1
Ce = 0

[interaction]
int_coupling = 1
int_detuning = 0

[simulation]
time = 100
step = 0.01

[output]
save_txt = True
save_png = True
out_label = output_${PDF}

EOF

python rabi.py

done

echo "---------------------------------------"
echo "Job done."