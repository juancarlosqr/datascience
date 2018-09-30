# Conda

## Environments

```shell
conda env list
```

```shell
# create new environment
conda create -n [env_name] [python version] [list of packages]

# install most recent python version
conda create -n my_proyect python=3
conda create -n py3 python=3

# install specific python version
conda create -n my_proyect python=3.3

# install legacy python version
conda create -n my_proyect python=2
conda create -n py2 python=2

conda create -n my_proyect python=3 numpy pandas matplotlib

conda create -n my_proyect numpy pandas matplotlib
```

```shell
conda activate my_proyect
```

```shell
conda deactivate
```

```shell
# list installed packages
conda list
```

```shell
conda update -n base -c defaults conda
```

```shell
conda upgrade conda
```

```shell
# update all packages in the environment
conda upgrade --all
```

```shell
# export environment
conda env export > environment.yaml
```

```shell
# import environment
conda env create -f environment.yaml
```

```shell
conda env remove -n env_name
```

## Packages 

```shell
conda install numpy
```

```shell
conda install numpy=1.10
```

```shell
conda install numpy scipy pandas
conda install jupyter notebook
```

```shell
conda remove numpy
```

```shell
conda update numpy
```

```shell
conda search *search_term*
```

```shell
# To avoid the shell expanding the use of wildcard *
# wrap the search string in single or double quotes like
conda search '*beautifulsoup*'
```

## zsh

export PATH="/Users/username/anaconda/bin:$PATH" to your .zsh_config file.

## pip

```shell
pip freeze > requirements.txt
pip install -r requirements.txt
```