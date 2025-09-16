import { readable } from "svelte/store";
import { browser } from "$app/environment";

export type Mode = "light" | "dark";

function detect(): Mode {
    if (!browser) return "light";
    const html = document.documentElement;
    const body = document.body;
    const isDark =
        html.classList.contains("dark") ||
        html.getAttribute("data-theme") === "dark" ||
        body?.classList.contains("dark") ||
        body?.getAttribute("data-theme") === "dark";
    console.log("Theme changed, isDark?: " + isDark);
    return isDark ? "dark" : "light";
}

export const theme = readable<Mode>("light", (set) => {
    if (!browser) return () => { };

    set(detect());

    // update on class/attr changes
    const onMut = () => set(detect());
    const obs = new MutationObserver(onMut);
    obs.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ["class", "data-theme"],
    });
    if (document.body) {
        obs.observe(document.body, {
            attributes: true,
            attributeFilter: ["class", "data-theme"],
        });
    }

    // update when OS preference changes
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    const onMQ = () => set(detect());
    mq.addEventListener?.("change", onMQ);

    // update if some code writes localStorage 'theme'
    const onStorage = (e: StorageEvent) => {
        if (e.key === "theme") set(detect());
    };
    window.addEventListener("storage", onStorage);

    return () => {
        obs.disconnect();
        mq.removeEventListener?.("change", onMQ);
        window.removeEventListener("storage", onStorage);
    };
});