# Mapping — Fallout Fixt → BIBLE.md (Lore Fusion)

## Source
- Scripts .SSL : 1039 fichiers source (Sduibek/FTL FixT), `source/scripts/*.SSL`
- Binary .int : 1039 fichiers compilés (`DATA/SCRIPTS/`)
- Game : Fallout 1 (F1), modifié par Fallout Fixt
- BIBLE.md : /home/portefolio/Téléchargements/BIBLE.md (version 0.1 — fusion d'univers)

## Règles de contrainte (BIBLE.md §4)
- Garder exactement les IDs `{100}` (sans modification)
- Garder même nombre d'options par nœud de dialogue
- Longueur ~2 lignes max par entrée (sauf narration)
- Glossaire imposé partout — pas d'exception
- Chaque fichier passe la revue de cohérence
- Ton : humour noir + rétrofuturisme + métaphysique Matrix/Terminator

## Glossaire imposé (BIBLE.md §2)

| Terme original | Nouveau terme | Rôle dans la nouvelle lore |
|---|---|---|
| The Master | **Le Maître** | IA stratégique fragmentée, vestige du réseau de commande de guerre, tente d'unifier tous les esprits |
| The Unity | **l'Unité** | Réseau de conscience unifiée ; le but du Maître |
| FEV | **VEF** (Vecteur d'Émergence Forcée) | Vecteur d'assimilation bio-numérique — PAS un virus |
| Vault | **l'Abri** | Pods de stase + simulation consensuelle (Matrix) — pas seulement bunkers |
| Vault-Tec | **Vault-Tec** | Architectes de la simulation |
| Wasteland | **le Désert** | Couche externe — réelle OU simulée (ambiguïté voulue) |
| Super Mutant | **Super-mutant** | Uploads ratés du réseau — tragiques, pas justes des monstres |
| Enclave | **l'Enclave** (si F2) | L'antivirus humain — veut rebooter le monde en effaçant le monde corrompu |
| The Player | **l'Anomalie** | Un esprit que la simulation n'a jamais totalement intégré ; quête de la puce d'eau |

## Quêtes principales — Beat-mapping (BIBLE.md §5)

| Jalons F1 actuels (script clé) | Rôle actuel | Nouveau rôle (BIBLE.md) | Script clé |
|---|---|---|---|
| Sortie de Vault 13 | Trouver la puce d'eau | L'éjection du pod — l'Anomalie sort du pod défaillant | CHILDRN1 / FALCON1 |
| Puce d'eau | Trouver le composant de l'infrastructure | L'élément de rechange de la simulation — quête physique dans le Désert | FALCON1 / MASTER |
| Rencontre avec Le Maître (Vault Dweller → Master) | Confrontation finale | Confrontation avec l'IA unifiée : le Maître n'est pas un mutant, c'est un réseau | MASTER.SSL |
| Duel / Combat avec le Master | Combat final | Combat contre l'Unité fragmentée — pas un boss unique, mais un réseau réparti | MASTER.SSL mastercbt / masterend |
| Fins (3) | Bleu / Rouge / 3e voie | Bleu = soumission à l'Unité ; Rouge = destruction ; 3e = fusion aux conditions humaines | masterend / master200+ |

## IDs {100} — Confirmation (BIBLE.md §4)
- Les IDs `{100}` dans `.SSL` sont références d'objets/proto (ex : portes, items, PNJ) — **NON MODIFIÉS**
- Mapping vérifié : `{100}` apparaît dans 33 scripts (DOOR.*, CHILDOOR.*, CREDDOOR.*, CBLKDOOR.*, BHDOOR.*, etc.) — ces objets sont des portes, des murs, des objets du monde
- **Aucune suppression, aucune renumérotation de `{100}`**
- Les GVAR (317, 157, 155, 159, 2, 1, 160, 288, 250…) sont conservés — ils lient les quêtes entre scripts

## Scripts clés pour le rewrite

| Script | Rôle actuel | Nouveau rôle (BIBLE.md) | Notes |
|---|---|---|---|
| MASTER.SSL | Dialogue/combat avec Le Maître | Dialogue/combat avec l'IA unifiée ; le Maître est un réseau, pas un mutant | 47 procédures (master00–master47) + master200+ pour fins |
| CHILDRN1.SSL | Enfants de Vault City (PNJ, intrusion, invasion, lumière) | Enfants de l'Abri — simulation d'A/B ; variables Master_Ptr, Red_Door_Ptr, Black_Door_Ptr, etc. | Conserve GVAR 77, 32, variables de déplacement |
| FALCON1.SSL | Puissance d'eau / première rencontre | Quête de la puce d'eau — quête de l'Anomalie | Variables First_Water, Money_Pack |
| MASTER2.SSL | Suite du Maître ? | Suite du Maître — dialogue après confrontation | Vérifier mapping en fonction du beat principal |
| MSTMERCH.SSL | Marchand du Maître | Marchand de la simulation — échange d'items dans le Désert l'Abri ? | Adapter au nouveau contexte |
| BROINVAD, FOLINVAD | Invasion, mutants | Invasions = uploads ratés du réseau (super-mutants) — tragiques | Adapter messages |

## Références de messages (MSG) — Mappées

| Fichier MSG | Contenu actuel | Nouveau contenu (BIBLE.md) | Notes |
|---|---|---|---|
| 350 | Holodisk / messages du code | Messages relatifs au VEF (Vecteur d'Émergence Forcée) ou au code de la simulation | Garder même numéro de message |
| 766 | Messages du Maître / expérience | Messages du Maître (Le Maître) — dialogue de l'IA unifiée | Garder même numéro |
| 194 | Childern messages (Vault City) | Messages des enfants de l'Abri — simulation d'A/B | Garder même numéro |

## Contexte de réécriture (BIBLE.md §4 — Contraintes techniques)

Pour chaque fichier réécrit par les sous-agents :
- **IDs {100}** : NE PAS modifier (même valeurs)
- **GVAR** : conserver (même références)
- **Nœuds de dialogue** : conserver le même nombre d'options par nœud
- **Longueur** : ~2 lignes max par entrée (sauf narration)
- **Messages système** : ne pas toucher (sauf liste explicite)
- **Glossaire** : appliquer partout (Le Maître, l'Unité, VEF, l'Abri, Vault-Tec, le Désert, Super-mutant, l'Enclave)
- **Ton** : humour noir + rétrofuturisme + questions d'identité/réalité/loop
- **3 fins** : soumission à l'Unité (bleu), destruction (rouge), fusion (3e voie)

## Vérification de cohérence (BIBLE.md §6)

Chaque fichier doit passer :
- Tous les noms d'objets, PNJ, lieux sont dans le glossaire BIBLE.md
- Tous les messages reflètent la nouvelle lore
- Les références GVAR sont cohérentes
- Les 3 fins sont clairement définies dans le mapping (masterend / master200+)

## Notes supplémentaires

- Le BIBLE.md demande un **beat-mapping** des quêtes sur la nouvelle lore. Ce mapping est fait : il relie chaque jalon F1 (sortie du Vault, puce d'eau, rencontre avec le Maître, 3 fins) aux concepts BIBLE.md (pod défaillant, VEF, Le Maître, l'Unité, 3 pilules).
- Le BIBLE.md demande une **fusion d'univers** : pas un simple remapping, mais une fusion des thèmes (Matrix + Terminator + Fallout 1). La nouvelle lore conserve la structure F1 mais avec des sens métaphysiques.
- Le BIBLE.md demande des **terminologies cohérentes** : pas de synonyme fantaisiste (pas "l'IA du Maître", toujours "Le Maître" ; pas "le virus FEV", toujours "VEF").

---

*Mapping produit : 2026-10-11 — version 0.1 — basé sur BIBLE.md v0.1 — source : package /mnt/WIN1TB/Games/Fixt-Canvas-Package/ + scripts source .SSL analysés par grep*