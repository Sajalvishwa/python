# ============================================================
# ANACONDA / CONDA INSTALLATION & SETUP
# ============================================================

# Anaconda Python ka ek distribution hai jo mainly
# Data Science, Machine Learning aur AI ke liye use hota hai.
#
# Anaconda ke saath commonly used tools/libraries jaise:
# NumPy, Pandas, Matplotlib, Scikit-learn aur Jupyter
# ko manage karna easy hota hai.


# ------------------------------------------------------------
# 1. ANACONDA INSTALLATION
# ------------------------------------------------------------
# Windows par Anaconda official website se download karke
# install karo.
#
# Installation ke baad Anaconda Prompt ya PowerShell open karo.


# ------------------------------------------------------------
# 2. CHECK CONDA INSTALLATION
# ------------------------------------------------------------
# Terminal mein run karo:
#
# conda --version
#
# Agar version aa jaye, example:
# conda 25.x.x
# to Conda successfully install hai.


# ------------------------------------------------------------
# 3. CHECK PYTHON
# ------------------------------------------------------------
# Terminal mein:
#
# python --version
#
# Example:
# Python 3.x.x


# ------------------------------------------------------------
# 4. CREATE A NEW ENVIRONMENT
# ------------------------------------------------------------
# Alag Python environment banane ke liye:
#
# conda create --name myenv python=3.12


# ------------------------------------------------------------
# 5. ACTIVATE ENVIRONMENT
# ------------------------------------------------------------
# conda activate myenv


# ------------------------------------------------------------
# 6. INSTALL COMMON DATA SCIENCE LIBRARIES
# ------------------------------------------------------------
# NumPy:
# conda install numpy
#
# Pandas:
# conda install pandas
#
# Matplotlib:
# conda install matplotlib
#
# Scikit-learn:
# conda install scikit-learn


# ------------------------------------------------------------
# 7. JUPYTER NOTEBOOK
# ------------------------------------------------------------
# Install:
#
# conda install jupyter
#
# Run:
#
# jupyter notebook


# ------------------------------------------------------------
# 8. CHECK INSTALLED PACKAGES
# ------------------------------------------------------------
# conda list


# ------------------------------------------------------------
# 9. DEACTIVATE ENVIRONMENT
# ------------------------------------------------------------
# conda deactivate


# ------------------------------------------------------------
# IMPORTANT
# ------------------------------------------------------------
# Anaconda ko pip se install karne ki zarurat nahi hoti.
#
# Anaconda = Python distribution
# Conda    = Package + Environment Manager
#
# Example:
# (base) PS C:\Users\Sajal>
#
# "(base)" ka matlab hai ki Conda ka base environment
# currently active hai.