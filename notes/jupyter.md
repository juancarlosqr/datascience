# Jupyter

```shell
# launch jupyter in current directory
jupyter notebook
```

```shell
# to manage the conda environments from within Jupyter
conda install nb_conda
```

## Shortcuts

- save notebook: `s`
- enter edit mode: `enter`
- exit edit mode (command mode): `esc`
- command palette: `shift + control/command + p`
- help (show keyboard shortcuts): `h`
- new cell above: `a`
- new cell below: `b`
- run cell: `shift + enter`
- delete cell: `d`
- show lines: `l`
- switch cell to markdown: `m`
- switch cell to python: `y`

## Magic keywords

- matplotlib: `%matplotlib inline`
- to render higher resolution images: `%config InlineBackend.figure_format = 'retina'`
- debugging: `%pdb`
- `timeit` line: `%timeit my_function()`
- `timeit` cell: `%%timeit`
- [complete list of magic keywords](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

## Convert notebooks

- to HTML: `jupyter nbconvert --to html notebook.ipynb`
- [docs](https://nbconvert.readthedocs.io/en/latest/usage.html)

## Docs

- [Jupyter](https://jupyter.readthedocs.io/en/latest/)
- [IPython](https://ipython.readthedocs.io/en/stable/)
- [Notebook](http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb)

## Markdown

- [getting-started-with-writing-and-formatting-on-github](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github/)
- [markdown-cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## LaTex

- [A Primer on Using LaTeX in Jupyter Notebooks](http://data-blog.udacity.com/posts/2016/10/latex-primer/)

## Practice

- [working-with-code-cells.ipynb](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/December/58474202_working-with-code-cells/working-with-code-cells.ipynb)
- [keyboard-shortcuts.ipynb](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/April/58e412d0_keyboard-shortcuts/keyboard-shortcuts.ipynb)