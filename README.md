# Vous aussi, votez Gisèle !

## Préambule
Afin de pouvoir exécuter correctement ce script, assurez-vous d'avoir Git, Python et Chromium installé sur votre machine.
Vous pouvez vérifier ceci via ces commandes :
`git --version`
> git version 2.30.2

`python --version` OU `python3 --version` (selon votre version)
> Python 3.9.2

`chromium --version`
> Chromium 120.0.6099.109 built on Debian 11.8, running on Debian 11.8

## Installer ce script sur votre machine
* Vous pouvez cloner ce dépôt via `git clone https://github.com/ZentaAeros/voter_gisele.git`
* Allez à la racine du projet via `cd voter_gisele`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv venv` OU `python3 -m venv env` (selon la version de python installée)
* Activez l'environnement virtuel via `source venv/bin/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt` OU `python3 -m pip install -r requirements.txt` (selon la version de python installée)

## Executer ce script sur votre machine via SSH
* Ouvrez un terminal
* `ssh root@server_ip` puis entrez votre mot de passe lorsque vous y êtes invité. (remplacez server_ip par l'IP de votre serveur).
* Suivre l'étape "Préambule" ET "Installer ce script sur votre machine" si ce n'est pas déjà fait.
* Ouvrez une nouvelle fenêtre de votre terminal via cette commande : `screen -S voter-gisele`
* A la racine du dossier "voter_gisele", executez cette commande : `python script.py` OU `python3 script.py`(selon la version de python installée)
* Une fois le script lancé vous devriez voir en quelques secondes les premiers résultats :
> Grâce à toi, Gisèle a gagné x votes

* Pour se déconnecter du serveur et laisser le script en arrière-plan veuillez faire ces combinaisons de touches : Ctrl + A ET Ctrl + D
* Vous reviendrez sur la fenêtre précédente
* Entrez ensuite `exit`, cela vous déconnectera du serveur.

## Suivre l'avancée du script sur votre machine via SSH
* Ouvrez un terminal
* `ssh root@server_ip` puis entrez votre mot de passe lorsque vous y êtes invité. (remplacez server_ip par l'IP de votre serveur).
* Revenez sur la fenêtre de votre terminal créé précédemment via cette commande : `screen -R voter-gisele`
* Vous pourrez ainsi suivre l'avancée ou dans le cas contraire une erreur en cas de soucis.

## Erreurs
Pour le moment il n'est pas censé y avoir d'erreurs particulières cependant si vous rencontrez un problème durant l'execution du script je vous invite à réaliser un bon vieux HARD REBOOT (vous ne serez pas jugé promis) et relancer le script en suivant la partie "Executer ce script sur votre machine via SSH"

