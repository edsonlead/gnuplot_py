set terminal pngcairo font 'Times-Roman-Bold,20' size 1920,1280
set output 'gnuplot-py.png'
plot 'graphlog.txt' title 'Otimizacao' with points pointtype 7

