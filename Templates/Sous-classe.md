---
parent_class: "[[<% tp.system.prompt("Classe parente") %>]]"
subclass_name: "<% tp.system.prompt("Nom de la sous-classe") %>"
---

# <% tp.file.title %>

## Classe parente

<%*
const parentClass = await tp.system.prompt("Chemin de la classe parente (ex: Glossary/Classes/Barbare)");
const parentFile = tp.file.find_tfile(parentClass);
if (parentFile) {
  const parent = await app.vault.read(parentFile);
  tR += "Informations héritées de la classe parente:\n\n";
  tR += "```dataview\n";
  tR += "TABLE WITHOUT ID\n";
  tR += '  hit_dice as "Dé de vie",\n';
  tR += '  saving_throws as "Jets de sauvegarde",\n';
  tR += '  armor_proficiencies as "Armures",\n';
  tR += '  weapon_proficiencies as "Armes"\n';
  tR += `FROM "${parentClass}"\n`;
  tR += "```\n";
}
%>

## Capacités de sous-classe

Capacités spécifiques à cette sous-classe...
