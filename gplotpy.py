from subprocess import run

class Gplotpy(): 

    def title(title, font_size):
        st = ("\nset title '{}' font '{}'".format(title, font_size))
        return st

    def label(x_label, y_label, font_size):
        sl = ("\nset xlabel '{}'".format(x_label) +
                "\nset ylabel '{}' font '{}'".format(y_label, font_size))
        return sl

    def figure(filename, w_size, h_size):
        sf = ("\nset terminal pngcairo  size '{}', '{}'".format(w_size, h_size) +
                "\nset output '{}png'".format(filename[0:-3]))
        return sf

    def line(tipe, collor):
        line = ("\nset style line 1 linetype '{}' linecolor '{}'".format(tipe, collor) +
		"\nset style function lines")
        return line   

    def plot(filename):
        plt = ("\nplot '{}' with lines ls 1".format(filename))
        return plt

    def template(tpl, title, label, figure, line, plot):
        ctpl = open(tpl, 'w')
        ctpl.write(title)
        ctpl.write(label)
        ctpl.write(figure)
        ctpl.write(line)
        ctpl.write(plot)
        ctpl.close()

    def execute(ctpl,command="gnuplot"):
        etpl = run([command, ctpl])
        return etpl

