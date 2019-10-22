FROM jupyter/scipy-notebook:1386e2046833

# add pydub
RUN conda install --quiet --yes 'pydub=0.23.*' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
