# Comment fonctionne ce repo
Il s'agit du site vitrine d'Aratech
Il est possible de lancer le projet en local et de le déployer sur une Infra OVH. 
Le déploiement peut être effectué en recette ou en production.

L'infrastructure est basée sur le service VPS d'OVH derrière un reverse proxy Traefik

## Developpement local
Pour lancer le projet en local il faut adapter le fichier .env.conf avec les bonnes valeurs et le nommer .env
C'est ce fichier .env qui sera utilisé par le docker compose.
Ensuite il faut lancer le docker compose :

    cd docker-local
    ./start-local.sh

Le site est disponible à l'adresse: http://localhost:8000

L'image docker est build en local et elle est tag aratechia/vitrine:local

Attention, la commande python manage runserver ne reproduit pas le fonctionnement correct sur site car c'est le serveur
Uvicorn asynchrone qui est utilisé en production alors que manage.py lance un serveur synchrone.
Il est donc très important de lancer le projet via un docker compose pour développer.

En cas d'utilisation d'une base de données, il faudra lancer les makemigrations depuis le container.
La commande migrate permettra de mettre à jour la struture BDD.

Le repository github doit donc contenir les __migrations__ si il y a une base de données.

Les migrations ont besoin d'être dans le repo git pour pouvoir éxécuter la commande `python manage.py migrate`

## Déployer en RE7
La RE7 est un site de test qui permet de valider le fonctionnement avec de passer sur de la PROD.

Pour déployer en RE7, il suffit de push ou de merge sur la branche main. C'est la CI/CD qui va déployer automatiquement
avec les bonnes variables d'environnement sur l'infra OVH. En particulier, la variable ENV passe à RE7.
Les valeurs des variables d'environnement sont stockées dans les secrets Doppler.

Le site est disponible à l'adresse : https://re7.aratech.fr

L'image docker est push sur le registry Docker Hub et elle est tag avec le numéro de commit.

## Déployer en production
Pour déployer en production, il convient de créer une release sur la branche main.
Le site sera alors disponible sur https://aratech.fr

L'image docker est push sur le registry Docker Hub et elle est tag avec le numéro de release.
