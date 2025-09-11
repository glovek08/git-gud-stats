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
