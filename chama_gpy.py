from gplotpy import Gplotpy as gp

title = gp.title("Título do Gráfico", "20")
label = gp.label("Label do Eixo X", "Label do Eixo Y", "14")
figure = gp.figure("graphlog.txt", "300", "280")
plot = gp.plot("graphlog.txt")
tpl = "new_teste.tpl"

gp.template(tpl, title, label, figure, plot)
gp.execute(tpl)
