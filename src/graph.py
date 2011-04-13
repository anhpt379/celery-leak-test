#! coding: utf-8
# pylint: disable-msg=W0311
import os
import CairoPlot


def graph(filename, data, h_labels):
  data = {"objects in memory" : data}
  h_labels = h_labels
  CairoPlot.dot_line_plot(filename, data, 800, 300, 
                          border=20, h_labels=h_labels, 
                          axis=True, grid=True, dots=True)


if __name__ == "__main__":
  files = os.listdir(os.path.dirname(__file__))
  data_files = [f for f in files if f.endswith('.txt')]
  for f in data_files:
    lines = open(f).read().split('\n')
    data = [] 
    h_labels = []
    for line in lines:
      if line != '':
        count, objects_in_memory = line.split('\t')
        data.append(int(objects_in_memory))
        h_labels.append(count)
    graph(f.replace('.txt', '.png'), data, h_labels)
    print '%s\t\tdone' % f
  