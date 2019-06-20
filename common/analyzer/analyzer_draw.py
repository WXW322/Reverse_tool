import matplotlib.pyplot as  plt

class drawer:
    def draw_line(self, X, Y):
        plt.plot(X, Y)

    def plot_linefigureone(file_to, x_lable, y_lable, datas_X, datas_Y, colors, labels, makers, xranges=None, yranges=None):
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        t_len = len(datas_X)
        i = 0
        while (i < t_len):
            plt.plot(datas_X[i], datas_Y[i], colors[i], label=labels[i], marker=makers[i])
            i = i + 1
        plt.show()