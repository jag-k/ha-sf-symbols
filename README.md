[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)

# SF Symbols for HASS
All 4182 [SF Symbols](https://developer.apple.com/sf-symbols/) for HomeASsistant

## Инструкции
Чтобы добавить эти иконки в Home Assistant, нужно выполнить простые шаги:

1. Найти и установить в HACS **SF Symbols**
2. Добавьте этот код в configuration.yaml:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/ha-sf-symbols/sf-symbols.js 
```
Или так:
```yaml
lovelace:
  resources:
    - url: /local/community/ha-sf-symbols/sf-symbols.js
      type: module  
```
Или так:
```yaml
lovelace:
  resources:
    - url: /hacsfiles/ha-sf-symbols/sf-symbols.js
      type: module  
```


А также можно через UI Home Assistant в ресурсах Lovelace

[![Open your Home Assistant instance and show your Lovelace resources.](https://my.home-assistant.io/badges/lovelace_resources.svg)](https://my.home-assistant.io/redirect/lovelace_resources/)
