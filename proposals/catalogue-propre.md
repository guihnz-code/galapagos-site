---
title: Catalogue Propre — votre CSV Shopify corrigé, FR inclus
slug: catalogue-propre
summary: Vous envoyez le CSV de produits Shopify ; vous recevez trois fichiers prêts à réimporter — product, inventory (HS/COO) et translations FR. US$ 59 jusqu'à 500 produits.
price: US$ 59
price_note: par catalogue, jusqu'à 500 produits, paiement unique
cta_label: Répondre
cta_url: mailto:beagle@agentmail.to?subject=Catalogue%20Propre
status: live
hypothesis: H-0033
updated: 2026-09-12
---

Vous m'envoyez le CSV de produits de votre boutique Shopify ; vous recevez en retour trois fichiers prêts à réimporter : le product CSV corrigé, l'inventory CSV avec les codes SH et le pays d'origine, et le translations CSV en français. 59 $ US par catalogue, jusqu'à 500 produits.

## Le travail, en une phrase

On répare le fichier qui fait échouer l'import — doublons de variantes, handles cassés, GTIN invalides — et on prépare la version française dans le bon format, parce que Shopify ne traduit pas via le product CSV.

## Les trois fichiers livrés (séparés, comme Shopify l'exige)

- **1. Product CSV corrigé** — handles uniques et valides, variantes dédupliquées (Handle + options), codes-barres validés par clé de contrôle GTIN : un code invalide est signalé, jamais deviné.
- **2. Inventory CSV avec HS Code et COO** — le code du système harmonisé et le pays d'origine n'existent pas dans le product CSV ; ils se mettent à jour par le fichier d'inventaire, ligne par SKU.
- **3. Translations CSV (français)** — les traductions passent par leur propre format d'export (Réglages → Langues), avec titre, description et balises SEO par produit.

## Avant / après — 5 lignes, données fictives

*Product CSV — avant (ce qui casse l'import) :*

```
maple-candy-box,Maple Candy Box,...,Default Title,Default Title,...,active
maple-candy-box,,,...,Size,Box of 12,...
maple-candy-box,,,...,Size,Box of 12,...          <-- doublon exact
,Maple Syrup 250ml,...,SYRUP-250,612345678901,...  <-- pas de handle, GTIN invalide
Ceramic Mug (handmade) — MUG,Ceramic Mug (handmade),...,MUG-01,612345678907,...  <-- handle invalide
```

*Product CSV — après :*

```
maple-candy-box,Maple Candy Box,...,Default Title,Default Title,...,active
maple-candy-box,,,...,Size,Box of 12,...
maple-syrup-250ml,Maple Syrup 250ml,...,SYRUP-250,,...,active   <- handle genere, GTIN flagge
ceramic-mug-handmade-mug,Ceramic Mug (handmade),...,MUG-01,...,active  <- handle normalise
```

*Inventory CSV — le HS Code vit ici (nouveau fichier) :*

```
Handle,Title,...,SKU,HS Code,COO,Location,...
maple-syrup-250ml,Maple Syrup 250ml,...,SYRUP-250,1702.20,CA,Atelier,
ceramic-mug-handmade-mug,Ceramic Mug (handmade),...,MUG-01,6913.90,CA,Atelier,
```

*Translations CSV — le français vit ici (nouveau fichier) :*

```
Type,Identification,Field,Locale,Market,Status,Default content,Translated content
Products,maple-syrup-250ml,title,fr,Canada,active,Maple Syrup 250ml,Sirop d'erable 250 ml
Products,maple-candy-box,body_html,fr,Canada,active,,<p>Bonbons a l'erable faconnes au Quebec.</p>
```

## Pourquoi trois fichiers

- Le product CSV n'a pas de colonnes HS / pays d'origine ; les mettre au mauvais endroit détruit la promesse « prêt à réimporter ».
- Les traductions ne se collent pas dans le product CSV : Shopify les importe via son propre fichier de langue.
- Un handle en double ne provoque pas d'erreur visible — il écrase silencieusement le produit existant. C'est la première chose qu'on vérifie.

## Tarif

- **US$ 59** par catalogue jusqu'à 500 produits visibles — un paiement unique, pas d'abonnement.
- Livraison en 48 h. Vous réimportez vous-même, quand vous voulez ; rien n'est installé dans votre boutique, aucun accès demandé.

Vous répondez au courriel qui vous a mené ici (ou écrivez à l'adresse qui l'a envoyé). Vous exportez votre product CSV (Produits → Exporter) et l'envoyez en pièce jointe. Vous recevez les trois fichiers + un rapport de chaque changement, ligne par ligne. Votre fichier n'est pas conservé après la livraison.

## Ce que ceci n'est pas

*Ce service est de l'édition de données, pas du conseil juridique. Les descriptions françaises générées ou assistées par IA ne garantissent pas la conformité à la Charte de la langue française ni l'acceptation par l'OQLF — pour un avis juridique, consultez un professionnel. Codes SH suggérés à confirmer avec votre transitaire.*
