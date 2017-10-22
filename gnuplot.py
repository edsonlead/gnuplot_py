from subprocess import run


def cria_template(template, filename, x_label, y_label, w_size, h_size):
    """
    Escreve um template para o gnuplot

    Args:
        template: nome do template
        filename: nome do arquivo de dados para plotagem
        x_label: nome do eixo x
        y_label: nome do eixo y
        w_size: largura da figura
        h_size: altura da figura
    """
    template = open(template, 'w')
    template.write("set terminal pngcairo size '%s', '%s' \n" %(w_size, h_size))
    template.write("set xlabel '%s' \n" %(x_label))
    template.write("set ylabel '%s' \n" %(y_label))
    template.write("set output '" +filename[0:-3]+"png' \n")
    template.write("plot '%s' " %(filename))
    template.close()

def exec_gnuplot(command, template):
    """
    Executa um comando

    Args:
        command: ex. gnuplot
        template: ex. teste.plt
    """
    result = run([command, template])
    return result


cria_template("teste.plt","graphlog.txt","eixo x","eixo y","360","280")
exec_gnuplot("gnuplot","teste.plt")


