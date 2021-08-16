#!/bin/bash

cd ..

PDFs="Dirac Poisson BoseEinstein"

for PDF in $PDFs; do

cd Utilities
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
out_label = output_$PDF

EOF

cd ..

python Rabi.py

done