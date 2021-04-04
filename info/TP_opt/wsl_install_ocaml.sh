echo "--------------------------------------------------------------------------------------"
echo "Lancement de l'installation de JupyterLab et OCaml"
echo "Indiquez le mot de passe et partez boire une boisson chaude (ou fraîche, suivant la météo)"
echo "--------------------------------------------------------------------------------------"

# Mise à jour et installation des paquets requis
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip gcc binutils-dev make pkg-config libzmq3-dev libgmp-dev opam m4

# Initialisation de opam
opam init -y --disable-sandboxing
eval $(opam env)

# Mise à jour du PATH
export PATH=~/.local/bin:$PATH
echo "export PATH=~/.local/bin:\$PATH" |sudo tee -a /etc/profile

# Installation de JupyterLab
pip3 install jupyterlab

# Installation paquets opam
opam install -y ocp-indent merlin
opam -y user-setup install
opam install -y jupyter


# Ajout du noyau OCaml
ocaml-jupyter-opam-genspec
jupyter kernelspec install --user --name ocaml-jupyter ~/.opam/default/share/jupyter

# Téléchargement du fichier premiers pas
wget https://mpsilamartin.github.io/info/TP_opt/ocaml_premiers_pas.ipynb

echo "--------------------------------------------------------------------------------------"
echo "Vous pouvez désormais lancer JupyterLab à l'aide de la commande : jupyter lab --no-browser"
echo "Copiez ensuite le lien et ouvrez-le dans votre navigateur préféré."
echo "Le fichier 'Premiers pas' vous donnera quelques indications."
echo "--------------------------------------------------------------------------------------"