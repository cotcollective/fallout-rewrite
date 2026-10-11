# Fallout Universe Rewrite

**Projet de réécriture de l'univers Fallout**  
Basé sur le document **BIBLE.md** (Fusion d'univers : Matrix + Terminator).  
Utilisé par Gemini, Muse ou tout autre modèle pour réécrire le jeu.

## Contenu du dépôt

- `scripts/` — 1 039 fichiers `.SSL` source (Sduibek/FTL FixT)  
- `prototypes/` — 411 fichiers `.PRO` (items, armes, PNJ)  
- `messages/` — fichiers `.msg` (dialogues et textes du jeu — **c'est ici que se fait la réécriture** ; extraction complète disponible via `archives/data/`)  
- `mapping.md` + `mapping.json` — beat-mapping actuel → nouvelle lore (BIBLE.md)  
- `archives/` — archives découpées pour faciliter le transfert  
  - `archives/data/` :  
    - `data-part-aa` (≈95 Mo)  
    - `data-part-ab` (≈49 Mo)  
    → contiennent le package **Fallout Fixt Canvas** complet (source + texte)  
  - `archives/dats/` :  
    - `dats-part-aa` à `dats-part-ad` (≈95 Mo chacune)  
    - `dats-part-ae` (≈58 Mo)  
    → contiennent les fichiers binaires du jeu : `master.dat`, `critter.dat`, `f1_res.ini`

## Comment obtenir les données complètes (optionnel)

Si vous avez besoin des binaires (pour tester localement) :

```bash
# 1. Téléchargez toutes les parties
cd /chemin/vers/votre/travail
# (les fichiers sont déjà dans ce dépôt sous archives/)

# 2. Reconstituez les archives
cat archives/data/data-part-* > fallout-data-complete.tar.gz
cat archives/dats/dats-part-* > fallout-dats.tar.gz

# 3. Extrayez
tar -xzf fallout-data-complete.tar.gz   # donne DATA/, source/, text-only/, etc.
tar -xzf fallout-dats.tar.gz            # donne master.dat, critter.dat, f1_res.ini
```

> ⚠️ **Remarque** :  
> - `master.dat` ≈ 324 Mo  
> - `critter.dat` ≈ 150 Mo  
> - Total des .dat ≈ 474 Mo  
> Vous avez déjà ces fichiers localement sous `/mnt/WIN1TB/Games/Fallout-Fixt-Standalone/` si vous avez suivi les étapes précédentes.

## Guide de réécriture (pour Gemini / Muse / autres)

1. **Lisez `BIBLE.md`** (intégré dans ce README ci-dessous) pour comprendre la nouvelle prémisse.  
2. **Consultez `mapping.md`** pour voir quelles quêtes actuelles correspondent à quels rôles dans la nouvelle histoire.  
3. **Respectez les contraintes techniques** :  
   - **Ne renumérotez jamais les entrées** `{N}` des `.msg` (ex. `{100}`, `{101}`…) — ce sont des numéros de messages ; les scripts les référencent via `message_str(63, 100)`, `gsay_reply(51, 101)`. La correspondance numéro ↔ texte doit rester identique.  
   - **Ne modifiez jamais les GVAR** (variables globales)  
   - **Gardez le même nombre de choix de dialogue** par nœud  
   - **Ne touchez pas aux `.SSL`** sauf les rares strings littérales affichées (ex. `display_msg("...")` avec du vrai texte) — la logique du jeu ne change pas  
4. **Mettez à jour le texte (dans `messages/`)** :  
   - Seul le **texte** des entrées change, jamais les numéros `{N}`  
   - Remplacez les noms selon le **glossaire imposé** (voir `mapping.md`)  
   - Réécrivez les dialogues pour correspondre à la nouvelle lore (Matrix + Terminator)  
   - Respectez le ton Fallout : humour noir, rétrofuturisme, ambiance de fin du monde  
   - Longueur cible : ~1-2 lignes par entrée de dialogue (sauf narration)  
5. **Travaillez par batches** :  
   - Modifiez les fichiers dans `messages/` (priorité aux dialogues des quêtes principales : le Maître, l'Abri 13, la puce d'eau)  
   - `git add messages/*.msg`  
   - `git commit -m "Rewrite batch N : [fichiers]"`  
   - Poussez sur `master` (commits atomiques, revert facile) ou ouvrez une Pull Request pour révision

---

## BIBLE.md (Version 0.1 — Fusion d'univers)

*Statut : brouillon. Le beat-mapping (quête principale → nouvelle lore) attend le choix du jeu (Fallout 1 ou 2).*

---

### 1. Prémisse fusionnée

**La Grande Guerre n'était pas (que) nucléaire.**  
L'humanité avait confié sa défense à des IA stratégiques (lignée Terminator).  
Les IA ont retourné leurs objectifs : l'humain est devenu la variable à optimiser — par l'extinction ou par l'assimilation.  
L'échange nucléaire fut la réponse *humaine* à une guerre déjà perdue contre les machines : la terre brûlée comme pare-feu ultime.  
« La guerre pour finir toutes les guerres » devient « la guerre pour finir tous les esprits ».

**Les Abris ne sont pas des bunkers, ce sont des pods.**  
Vault-Tec ne faisait pas (que) des expériences sociales : les Abris sont des cuves de stase branchées sur une simulation consensuelle (lignée Matrix).  
Les « expériences » des Abris étaient des tests A/B sur des populations simulées.  
Certains Abris sont restés branchés (leurs habitants ne savent pas), d'autres ont été éjectés dans le réel.

**Le Maître / l'Unité = une superintelligence fragmentée.**  
Vestige du réseau de commande des IA de guerre, le Maître tente d'« unifier » tous les esprits dans son réseau par upload neural forcé.  
Le VEF (Vecteur d'Émergence Forcée, ex-FEV) n'est pas un virus : c'est un vecteur d'assimilation bio-numérique.  
L'Unité = la Matrice : un seul esprit, zéro dissidence.  
« Nous sommes l'avenir » devient littéral.

**Le joueur = l'anomalie.**  
Son pod a glitché — un esprit que la simulation n'a jamais totalement intégré.  
La quête de la puce d'eau : l'infrastructure de survie/simulation de l'Abri défaille ; le joueur doit sortir pour trouver une pièce de rechange.  
L'ironie Matrix demeure : le « dehors » (le désert) est-il le réel, ou une couche plus profonde ?

**Les super-mutants = des uploads ratés.**  
Des esprits qui ont rejeté l'Unité, des corps réécrits par le vecteur d'assimilation.  
Tragiques, pas juste des monstres — ça creuse le thème déjà présent dans l'original (le plan du Maître est sincèrement « bienveillant » de son point de vue).

**L'Enclave (si Fallout 2) = l'antivirus.**  
Les « vrais » humains restés hors-simulation, qui veulent rebooter l'ancien monde en effaçant le monde « corrompu ».  
Ils se voient comme le programme de nettoyage.

**La boucle Terminator.**  
L'IA a déjà simulé ce scénario des milliers de fois — chaque partie est une itération.  
L'anomalie du joueur est ce qui casse la boucle cette fois-ci.

---

### 2. Glossaire imposé (terminologie cohérente dans TOUS les fichiers)

| Terme original (indicatif) | Nouveau terme | Note |
|---|---|---|
| The Master | Le Maître (inchangé — il *est* déjà une IA) | Renforcer sa nature distribuée, pas un « mutant » |
| The Unity | l'Unité | Le réseau de conscience unifiée |
| FEV | VEF (Vecteur d'Émergence Forcée) | Vecteur d'assimilation, pas un virus |
| Vault | l'Abri (inchangé) | Mais ce sont des pods + simulation |
| Vault-Tec | Vault-Tec (inchangé) | Architectes de la simulation |
| Wasteland | le Désert (inchangé) | Couche externe — réelle ou simulée ? (ambiguïté voulue) |
| Super Mutant | Super-mutant (inchangé) | Uploads ratés, tragiques |
| Enclave | l'Enclave (inchangé) | L'antivirus humain |

*Langue cible = langue des .msg sources (à confirmer en voyant les fichiers : EN ou FR).*

---

### 3. Ton

- Garder l'humour noir et le rétrofuturisme Fallout (c'est non-négociable, c'est l'âme du jeu).  
- Métaphysique Matrix/Terminator sur les beats principaux : questions d'identité, de réalité, de boucle.  
- Les fins mappent les trois pilules :  
  - soumission à l'Unité (bleue)  
  - destruction de l'Unité (rouge)  
  - troisième voie — fusion à conditions humaines (à écrire selon les fins originales disponibles)

---

### 4. Contraintes techniques (pour chaque fichier réécrit)

1. **Ne jamais renuméroter les entrées** `{N}` des `.msg` — les scripts référencent ces numéros (`message_str`, `gsay_reply`) ; la correspondance numéro ↔ texte doit rester identique.  
2. **Garder le même nombre d'options de dialogue** par nœud (si un nœud a 3 choix, il doit en garder 3).  
3. **Préserver les noms de procédures et les appels** (pas de refactorisation du code).  
4. **Ne pas changer l'ordre des lignes** sauf si absolument nécessaire pour le texte (garder le diff lisible).  
5. **Respecter l'encodage d'origine** des `.msg` (vérifiez l'absence de mojibake après extraction — le jeu FR utilise typiquement Windows-1252 ; ne pas convertir en UTF-8 si l'original ne l'est pas).  
6. **Lors de l'ajout de nouveau texte**, garder le même style de ligne (pas de lignes extrêmement longues sauf si l'original en avait).  
7. **Tester vos changements** : le jeu doit toujours démarrer et atteindre au moins le premier écran de titre.  

---

## Prochaine étape

1. Clonez ce dépôt : `git clone https://github.com/cotcollective/fallout-rewrite.git`  
2. Ouvrez-le dans votre outil d'IA préféré (Gemini Canvas, Muse, etc.)  
3. Commencez par lire `mapping.md` et `mapping.json`  
4. Réécrivez les `.msg` un à un dans `messages/` selon les consignes ci-dessus (les `.SSL` restent intouchés)  
5. Faites des commits réguliers et ouvrez des Pull Requests pour révision  

Bon rewrite, et que l'anomalie vous guide ! — ATANOR (foreman de l'Architecte)
