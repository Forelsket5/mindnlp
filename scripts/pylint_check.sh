
NUM_CORES=$(nproc)
pylint --jobs=$NUM_CORES --rcfile=.github/pylint.conf mindnlp
