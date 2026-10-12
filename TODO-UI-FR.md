# TODO — UI FR (reste à faire, session 2026-10-12)

## Ce qui est fait (670 files, ~28k entrées)
- Dialogues PNJ : messages/*.MSG — FR, terminologie standardisée, validée.

## Ce qui reste
1. messages/game-ui/ — 28 fichiers UI (INTRO non inclus ci-dessous) à traduire EN→FR :
   COMBATAI, COMBAT, DBOX, EDITOR, INTRFACE, INVENTRY, ITEM, LSGAME, MAP, MISC,
   OPTIONS, PERK, PIPBOY, PRO_CRIT, PRO_ITEM, PRO_MISC, PRO_SCEN, PRO_TILE,
   PROTO, PRO_WALL, SCRIPT, SCRNAME, SKILLDEX, SKILL, STAT, TRAIT, WORLDMAP
   → Contraintes : IDs/labels intacts, CRLF, ~2 lignes/entrée, cp1252 final.
2. INTRFACE.MSG + INTRO (intro cinématique) — DANS master.dat, à extraire :
   `fallout2-ce`/utilities ou `datexpl`; sinon python-fallout-dat.
3. ScrnSet.msg — la copie repo = RUSSE. Remettre la version EN du jeu
   (/mnt/WIN1TB/Games/Fallout/fallout-ce/DATA/TEXT/ENGLISH/GAME/ScrnSet.msg est ASCII/EN ok)
   pis la traduire FR.
4. Font test — vérifier accents FR dans la fonte du jeu (é, è, à, ç).
5. Deploy test — copier les GAME traduits dans
   /mnt/WIN1TB/Games/Fallout/fallout-ce/DATA/TEXT/ENGLISH/GAME/, relancer fallout-ce-launcher.

## Config jeu
- fallout.cfg : language=english (FIX: était spanish)
- Launcher : /home/portefolio/.local/bin/fallout-ce-launcher (WINDOWED=1 forcé)
