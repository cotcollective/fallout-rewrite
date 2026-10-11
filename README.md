# Fallout Universe Rewrite

**Projet de réécriture narrative de Fallout 1 (mod Fixt) selon BIBLE.md**  
Fusion d'univers : *Matrix + Terminator + Fallout 1*

## Concept

Relire le storyline de Fallout 1 avec une lore *Fusion d'Univers* :

- **La Grande Guerre = IA stratégique** : l'humanité a perdu contre des machines (lignée Terminator). L'attaque nucléaire fut une réponse désespérée.
- **Les Abris = Pods de simulation** : Vault-Tec installe des populations dans des environnements simulés (Matrix). Certains sont branchés, d'autres éjectés dans le "réel".
- **Le Maître / l'Unité = Superintelligence fragmentée** : vestige d'un réseau de commande militaire, tentant d'unifier tous les esprits par upload forcé.
- **VEF = Vecteur d'Association Bio-numérique** : pas un virus, mais un vecteur d'assimilation.
- **Le joueur = L'Anomalie** : un esprit qui n'est jamais totalement intégré à la simulation. La quête de la puce d'eau devient une quête d'évasion de la simulation.
- **Super-mutants = Uploads ratés** : des esprits qui ont rejeté l'Unité, corps réécrits par le VEF — tragiques, pas juste des monstres.
- **l'Enclave = L'Antivirus humain** (si F2) : veut rebooter l'ancien monde en effaçant le monde corrompu par la simulation.

## Contenu

- `scripts/` : 1039 fichiers `.SSL` (source scripts Fallout 1, Sduibek)
- `messages/` : dialogues (.msg) et textes
- `prototypes/` : items, armes, PNJ (.pro)
- `mapping.md` : beat-mapping actuel (quêtes → nouvelle lore)
- `mapping.json` : données structurées (GVAR, IDs, glossaire)

## Workflow pour Gemini / Muse

1. Lire `mapping.md` et `mapping.json` pour comprendre le beat-mapping
2. Lire le glossaire dans `mapping.md` (Le Maître ≠ mutant, l'Unité, VEF, etc.)
3. Pour chaque fichier `.SSL` dans `scripts/` :
   - Préserver les IDs `{100}` (objets/proto)
   - Préserver les GVARs (liens de quête)
   - Préserver les nombres de choix de dialogue (N)
   - Réécrire les dialogues selon la nouvelle lore
   - Appliquer le glossaire imposé partout
4. Mettre à jour `messages/` et `prototypes/` correspondants
5. Soumettre un PR avec les modifications

## Glossaire imposé

| Anciennement | Nouveau | Rôle |
|---|---|---|
| The Master | Le Maître | IA distribuée, vestige du réseau de guerre |
| The Unity | l'Unité | Réseau de conscience unifiée |
| FEV | VEF | Vecteur d'assimilation bio-numérique |
| Vault | l'Abri | Pod + simulation consensuelle |
| Wasteland | le Désert | Couche externe (réelle ou simulée) |
| Super Mutant | Super-mutant | Upload raté (tragique) |
| Enclave | l'Enclave | Antivirus humain |

## Mode de travail

- ✅ IDs `{100}` **précisément préservés** (pas de renumérotation)
- ✅ Nœuds de dialogue : **même nombre d'options**
- ✅ Longueur : **2 lignes max** par entrée (sauf narration)
- ✅ Messages système : **ne pas toucher**
- ✅ Glossaire : **obligatoire partout**
- ✅ Ton : humour noir + rétrofuturisme + boucle Terminator/Matrix

## Pour commencer

1. Fork ou clone ce repo
2. Lire `mapping.md`
3. Choisir 10-20 scripts à réécrire comme POC
4. Faire les modifications
5. Soumettre un PR

---

*Statut : en cours de construction. Les fichiers .SSL seront ajoutés après audit de cohérence initial.*

*Créé par Atanor — Foreman, porteur des règles de réécriture selon BIBLE.md*
