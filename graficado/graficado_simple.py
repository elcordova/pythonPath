from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
  output_file('graficado_simple.html')
  fig = figure()
  
  totals = int(input('Cuantos valores quieres graficar?'))
  x_values = list(range(totals))
  y_values = []

  for x in x_values:
    val = int(input(f'Valor y para {x}'))
    y_values.append(val)

  fig.line(x_values, y_values, line_width=2)
  show(fig)