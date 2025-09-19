<script lang="ts">
	import "../app.css";
	import favicon_dark from "$lib/assets/GitGudStats_logo_dark.svg";
	import favicon_light from "$lib/assets/GitGudStats_logo_light.svg";
	// import "the-new-css-reset/css/reset.css"; <- Commented because it fucks up flowbite.
	import { theme } from "$lib/stores/theme";

	// Components
	import Header from "$lib/Header.svelte";
	import Footer from "$lib/Footer.svelte";

	let { children } = $props();

	const currentFavicon = $derived($theme === 'dark' ? favicon_light : favicon_dark);

</script>

<svelte:head>
	<link
		rel="icon"
		type="image/svg+xml"
		href={favicon_light}
		media="(prefers-color-scheme: light)"
	/>
	<link
		rel="icon"
		type="image/svg+xml"
		href={favicon_light}
		media="(prefers-color-scheme: no-preference)"
	/>
	<link
		rel="icon"
		type="image/svg+xml"
		href={favicon_dark}
		media="(prefers-color-scheme: dark)"
	/>
	<link rel="icon" type="image/svg+xml" href={currentFavicon} />
</svelte:head>
<div class="layout-container">
	<Header />
	<main class="main-content">
		{@render children?.()}
	</main>
	<Footer />
</div>

<style>
	.layout-container {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}
	.main-content {
		flex: 1 1 auto;
		min-height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
