# Propuestas · Playing Camp

Repo de propuestas comerciales servidas vía GitHub Pages.

Cada cliente vive en su propia carpeta `/cliente/index.html` y se sirve en:

`https://playingcamp.github.io/propuestas-pc/<cliente>/`

Todas las propuestas llevan `<meta name="robots" content="noindex,nofollow">` para evitar indexación en buscadores. El repo es público (limitación de GitHub Pages free), las URLs no son adivinables a través de Google pero sí accesibles si se conocen.

## Editar y desplegar cambios

```bash
cd ~/propuestas-pc
# editar archivos
git add -A
git commit -m "update <cliente>: <qué cambia>"
git push
```

GitHub Pages republica en 30-90 segundos.
