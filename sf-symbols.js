const SF_SYMBOLS_MAP = require('./res.min.json')

async function getIcon(name) {
  return { path: SF_SYMBOLS_MAP[name.replace(/_/g,'-')] };
}

async function getIconList() {
  return Object.keys(SF_SYMBOLS_MAP).map(icon => ({name: icon}));
}

if (!window.frontendVersion || window.frontendVersion <= 20211027.0){
  window.customIconsets = window.customIconsets || {};
  window.customIconsets["sf-symbols"] = getIcon;
} else {
  window.customIcons = window.customIcons || {};
  window.customIcons["sf-symbols"] = { getIcon, getIconList };
}