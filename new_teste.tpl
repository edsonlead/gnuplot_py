
set title 'Título do Gráfico' font '20'
set xlabel 'Label do Eixo X'
set ylabel 'Label do Eixo Y' font '14'
set terminal pngcairo  size '300', '280'
set output 'graphlog.png'
set style line 1 linetype '1' linecolor 'cyan'
set style function lines
plot 'graphlog.txt' with lines ls 1