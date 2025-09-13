# sv

Everything you need to build a Svelte project, powered by [sv](https://github.com/sveltejs/cli).

![SvelteKit](https://img.shields.io/badge/SvelteKit-2.22-FF3E00?logo=svelte&logoColor=white&style=for-the-badge)
![Svelte](https://img.shields.io/badge/Svelte-5.0.0-FF3E00?logo=svelte&logoColor=white&style=for-the-badge)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.1.0-38B2AC?logo=tailwindcss&logoColor=white&style=for-the-badge)
![Vite](https://img.shields.io/badge/Vite-7.0.4-646CFF?logo=vite&logoColor=white&style=for-the-badge)
![Flowbite](https://img.shields.io/badge/Flowbite-3.1.2-0E7490?logo=flowbite&logoColor=white&style=for-the-badge)


### Flowbite Integration

Flowbite uses Tailwind to customize components.

* <strong><i>Note!</i></strong> If you see the error `Unknown at rule @tailwind css(unknownAtRules)`:
    1) Create `.vscode/settings.json`
    2) Add this to ensure VSCode uses Tailwind with CSS files:
        ```css
        {
            "files.associations": {
                "*.css": "tailwindcss"
            }
        }
        ```

## Building

To create a production version of this app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

# Front-end features

### Index:

1) [Theme Subscribable](#Theme_Subscribable)

## Theme Subscribable

A read-only Svelte store that reflects the current page theme ("light" | "dark") by observing the `.dark` class or `data-theme="dark"` on `<html>`/`<body>`.

- Location: `src/lib/stores/theme.ts`
- Export: `theme` (readable<'light' | 'dark'>)
- Source of truth: presence of `.dark` or `data-theme="dark"`

Usage
```ts
<script lang="ts">
  import { theme } from '$lib/stores/theme';
</script>

<p>Current theme: {$theme}</p>
```

Notes
- SSR: defaults to "light" during SSR and updates on mount.
- Tailwind v4: tokens defined in `@theme` and `@theme .dark` auto-switch with `.dark` — use utilities like `bg-bg-primary`, `text-primary-500` without needing `dark:` variants.
- Ensure your toggle sets/removes `.dark` on `<html>` (Flowbite’s DarkMode or your own logic).

Example (Tailwind token usage)
```html
<div class="bg-bg-primary text-primary-900 p-4 rounded">
  Theme is {$theme}
</div>
```
