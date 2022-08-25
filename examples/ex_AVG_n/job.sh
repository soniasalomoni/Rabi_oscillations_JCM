#!/bin/bash

# This job launches 3 simulations with different average number of photons
# The other parameters are listed below

AVGn="10 30 50"

for n in $AVGn; do
cat > input.txt << EOF

[field]
avg_n = $n
pdf_n = Poisson
cut_n = 100

[atom]
Cg = 1
Ce = 0

[interaction]
int_coupling = 1
int_detuning = 0

[simulation]
time = 200
step = 0.01

[output]
save_txt = True
save_png = True
out_label = output_$n

EOF

python Rabi.py

done

echo "---------------------------------------"
echo "Job done."