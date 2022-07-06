

# Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız:
# conda create -n ozlem_env python=3

# Görev 2: Oluşturduğunuz environmentı aktiva ediniz
# conda activate ozlem_env

# Görev 3: Yüklü paketleri listeleyiniz
# conda list

# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
# conda install numpy pandas=1.2.1

# Görev 5: İndirilen Numpy'ın versiyonu nedir?
# conda list
# python -c "import numpy; print(numpy.__version__)"

# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
# conda upgrade pandas
# conda list
# python -c "import pandas; print(pandas.__version__)"

# Görev 7: Numpy'ı environment'tan siliniz.
# conda remove numpy

# Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
# conda install seaborn matplotlib

# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
# conda env export > ozlem_env.yaml


        # Mevcut environment bu paket ve versiyonlar ile güncellemek isteniyorsa :
        # conda env update -n vbo_env --file=ozlem_env.yaml

        # Eğer yeni bir env create ederek okutmak isteniyorsa:
        # conda env create --name new_env --file=ozlem_env.yaml


# Görev 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
# conda deactivate
# conda env remove -n ozlem_env
# conda remove -n vbo_env --all -y

######################

# Ek komutlar:

# Tüm paketlerin yükseltilmesi/ versiyon güncellemesi:
#  conda upgrade --all


# conda install numpy=1.20.1
# pip install numpy==1.20.1

